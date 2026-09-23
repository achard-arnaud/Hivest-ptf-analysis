"""NRT on the actual company dossier, plus mutations of decision-critical fields."""
import json,sys,tempfile,shutil,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from validate_bundle import validate_bundle
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
    def test_bcg_requires_market_axes(self):self.change(lambda d:d['segments'][0].update(bcg='star'));self.rejected()
    def test_subsidiary_not_group(self):self.change(lambda d:d['leaders'][0].update(person='Synthetic',status='verified_group',scope='subsidiary'));self.rejected()
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
        d=json.loads((ROOT/'program/leadership_register.json').read_text());self.assertEqual(len(d['rows']),22)
        for x in d['rows']:
            if x['person'] is not None:self.assertNotEqual(x['scope'],'groupe')
if __name__=='__main__':unittest.main()
