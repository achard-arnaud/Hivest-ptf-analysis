"""NRT on the actual company dossier, plus mutations of decision-critical fields."""
import json,sys,tempfile,shutil,unittest
from pathlib import Path
from jsonschema import ValidationError
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from validate_bundle import validate_bundle
from compose_dossier import compose
from check_prehitl import check as check_prehitl
from research_graph import context,affected
class SphereBundle(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.c=Path(self.tmp.name)/'sphere';shutil.copytree(ROOT/'companies/sphere',self.c)
    def tearDown(self):self.tmp.cleanup()
    def change(self,fn):
        p=self.c/'strategic_context.json';d=json.loads(p.read_text());fn(d);p.write_text(json.dumps(d))
    def rejected(self):
        with self.assertRaises(ValueError):validate_bundle(self.c)
    def test_actual_company_package(self):self.assertEqual(validate_bundle(self.c)['status'],'PASS')
    def test_material_captures_still_block_hitl(self):
        result=check_prehitl('sphere')
        self.assertEqual(result['status'],'FAIL')
        self.assertTrue(all(any(source in issue for issue in result['missing']) for source in ('S02','S03','S06')))
    def test_bcg_requires_market_axes(self):self.change(lambda d:d['segments'][0].update(bcg='star'));self.rejected()
    def test_monetary_estimates_are_decimal_strings(self):
        self.change(lambda d:d['segments'][0].update(revenue_estimate_meur=297.18))
        with self.assertRaises(ValidationError):validate_bundle(self.c)
    def test_compose_reads_identity_and_cutoff_from_manifest(self):
        manifest=self.c/'manifest.json';d=json.loads(manifest.read_text());d.update(entity_id='example',cutoff='2026-01-01');manifest.write_text(json.dumps(d))
        out=self.c/'compiled.md';compose(self.c,out)
        self.assertIn('# EXAMPLE',out.read_text())
        self.assertIn('Cutoff : 2026-01-01',out.read_text())
    def test_subsidiary_not_group(self):self.change(lambda d:d['leaders'][0].update(person='Synthetic',status='verified_group',scope='subsidiary'));self.rejected()
    def test_group_role_requires_legal_or_corporate_source(self):
        self.change(lambda d:d['leaders'].append(dict(role='DG',person='Synthetic',exact_title='DG',scope='group',status='verified_group',source_refs=['S-P02'],next_question='')))
        self.rejected()
    def test_proposed_ml_not_observed(self):self.change(lambda d:d['ml_strategy'].update(observed_status='observed'));self.rejected()
    def test_prerequisite_not_ai_case(self):self.change(lambda d:d['prerequisites'][0].update(former_id='UC-S03'));self.rejected()
    def test_driver_link_required(self):self.change(lambda d:d['opportunity_links'][0].update(driver_id='missing'));self.rejected()
    def test_artifact_tampering(self):
        p=self.c/'analysis/02_market.md';p.write_text(p.read_text()+'\nSynthetic changed conclusion');self.rejected()
    def test_hash_coverage_cannot_drop(self):self.change(lambda d:d['artifact_hashes'].pop('analysis/02_market.md'));self.rejected()
    def test_path_escape(self):self.change(lambda d:d['frameworks'].update(porter='../../README.md'));self.rejected()
    def test_graph_bound(self):
        g=json.loads((self.c/'research_graph.json').read_text());self.assertLessEqual(len(context(g,'page3')),12)
        with self.assertRaises(ValueError):context(g,'page3',2)
    def test_changed_source_invalidates_outputs(self):
        g=json.loads((self.c/'research_graph.json').read_text());self.assertTrue({'page1','page2','page3'}<=set(affected(g,'evidence')))
    def test_no_global_leader_substitution(self):
        d=json.loads((ROOT/'program/leadership_register.json').read_text())
        entities={x['entity'] for x in d['rows']}
        for entity in entities:
            requested={x['role_requested'] for x in d['rows'] if x['entity']==entity}
            self.assertTrue({'COO','DSI'} <= requested)
        for x in d['rows']:
            if x['person'] is not None and x['scope']=='groupe':
                self.assertEqual(x['status'],'verified_group')
                self.assertIn(x.get('source_type'),('legal_register','corporate'))
                self.assertTrue(x.get('source_url'))
if __name__=='__main__':unittest.main()
