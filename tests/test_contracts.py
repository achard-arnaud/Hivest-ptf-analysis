import copy
import hashlib
import importlib.util
import json
import unittest
from pathlib import Path
from jsonschema import ValidationError

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('validator',ROOT/'scripts/validate.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)

def package():
    """Synthetic fixture only. No assertion about any portfolio company."""
    src=dict(id='S1',url='https://example.org/fixture',scope='company',entity_ids=['fixture'],published_at='2026-01-01',accessed_at='2026-09-23',grade='B',origin_id='origin1',source_type='corporate',access_status='read',snapshot_uri='fixture://source1',sha256='a'*64,rights='synthetic')
    frag=dict(id='F1',source_id='S1',locator='paragraph 1',excerpt='Synthetic evidence',sha256=hashlib.sha256(b'Synthetic evidence').hexdigest())
    claim=dict(id='C1',entity_id='fixture',scope='company',statement='Synthetic workflow',status='fact',confidence='medium',fragment_refs=['F1'],basis_claim_refs=[],contradiction_refs=[],observed_at='2026-01-01',valid_until=None,owner='research',validation_question='Verify operating scope',deployment_stage='experiment')
    dims=[dict(id=x,score=None,status='unknown',confidence='low',claim_refs=[],counter_evidence=[],unknowns=['Not researched'],rationale='No observed capability',scope='group') for x in ['strategy_value','operating_model','data_knowledge','technology_platform','delivery','people_adoption','security_risk','breadth']]
    uc=dict(id='UC1',title='Synthetic opportunity',vertical='operations',workflow='Inspect sample',problem='Unknown defect baseline',value_mechanism='Reduce repeat inspection',status='hypothesis',company_claim_refs=['C1'],sector_claim_refs=[],business_owner_hypothesis='Quality lead',data_dependencies=['labelled samples'],technology_dependencies=[],adoption_dependencies=['validation by operators'],gates=[dict(name='data_access',status='unknown',claim_refs=[],reason='Unconfirmed')],priority_state='validation_required',ratings={k:'unknown' for k in ['economic_value','strategic_value','feasibility','time_to_value','repeatability','adoption','risk','portfolio_reuse']},family='quick_win',horizon='0-6',sourcing_posture='NO-ACTION',baseline_without_ai='Manual inspection',reversibility='Stop before integration',unknowns=['baseline'],validation_question='Is there a measurable defect cost?')
    uc['gates']=[dict(name=n,status='unknown',claim_refs=[],reason='Unconfirmed') for n in ['data_rights','security_ot','human_control','ownership','feasibility']]
    return dict(version='0.1.0',entity_id='fixture',cutoff='2026-09-23',sources=[src],fragments=[frag],claims=[claim],maturity=dict(dimensions=dims,summary='Unknown',bottlenecks=['No diagnosis'],applicable_domains=['operations'],excluded_domains_rationale=['Synthetic fixture only']),value_chain=[],use_cases=[uc],strategic_positions=[],contradictions=[],unknowns=['No research'])

def content(p):
    item=dict(text='Not established',status='unknown',claim_refs=[])
    payload=dict(entity_id='fixture',cutoff=p['cutoff'],page1=dict(title='Synthetic context',identity=[item],financials=[item],business_thesis=[item],seven_s=[item]*7,swot={k:[item] for k in ['strengths','weaknesses','opportunities','threats']},maturity=[item]*8),page2=dict(title='Synthetic chain',activities=[item],supports=[item],handoffs=[item]),page3=dict(title='Synthetic decision',strategic_positions=[item],use_case_ids=[f'UC{i}' for i in range(1,7)],horizons=[item],sourcing=[item],equity_thesis=item,next_validation=item),source_ids=['S1'])
    run=dict(version='0.1.0',entity_id='fixture',stage='FROZEN',analysis_dimension='business',package_sha256=v.digest(p),source_refs=['S1'],claim_refs=['C1'],contradictions=[],unknowns=[],rejected_alternatives=[],hard_gates=[],versions=dict(workflow='0.1.0',template='0.1.0',fixture='0.1.0'),red_team_verdict='SURVIVES_WITH_NARROWING',repair_count=0,hitl=dict(decision='GO_DRAFT',actor='fixture_human',decided_at='2026-09-23',decision_ref='fixture://approval',package_sha256=v.digest(p)),next_action='Render fixture')
    payload['use_cases']=copy.deepcopy(p['use_cases'])
    payload['sources']=copy.deepcopy(p['sources'])
    return dict(version='0.1.0',template='THREE_PAGER_PORTFOLIO_AI',payload=payload,payload_sha256=v.digest(payload),run_context=run)

class Contracts(unittest.TestCase):
    def setUp(self): self.p=package()
    def reject(self):
        with self.assertRaises((ValueError,ValidationError)):v.validate_package(self.p)
    def test_valid_unknown(self):self.assertTrue(v.validate_package(self.p))
    def test_zero_is_not_unknown(self):self.p['maturity']['dimensions'][0]['score']=0;self.reject()
    def test_duplicate_dimension(self):self.p['maturity']['dimensions'][1]['id']='strategy_value';self.reject()
    def test_sector_laundering(self):self.p['sources'][0]['scope']='sector';self.reject()
    def test_wrong_company(self):self.p['sources'][0]['entity_ids']=['other'];self.reject()
    def test_missing_source(self):self.p['fragments'][0]['source_id']='missing';self.reject()
    def test_fragment_tampering(self):self.p['fragments'][0]['excerpt']='Changed';self.reject()
    def test_future_source(self):self.p['sources'][0]['published_at']='2027-01-01';self.reject()
    def test_unread_source(self):self.p['sources'][0]['access_status']='inaccessible';self.reject()
    def test_duplicate_id(self):self.p['claims'].append(copy.deepcopy(self.p['claims'][0]));self.reject()
    def test_circular_claim(self):self.p['claims'][0]['basis_claim_refs']=['C1'];self.reject()
    def test_hard_gate_compensation(self):self.p['use_cases'][0]['priority_state']='eligible';self.reject()
    def test_failed_gate(self):self.p['use_cases'][0]['gates'][0]['status']='fail';self.reject()
    def test_gate_pass_without_evidence(self):self.p['use_cases'][0]['gates'][0]['status']='pass';self.p['use_cases'][0]['priority_state']='eligible';self.reject()
    def score(self,n=1):self.p['maturity']['dimensions'][4].update(score=n,status='observed',claim_refs=['C1'])
    def test_observed_experiment(self):self.score();self.assertTrue(v.validate_package(self.p))
    def test_job_is_not_capability(self):self.score();self.p['sources'][0]['source_type']='job';self.reject()
    def test_announcement_is_not_production(self):
        self.score(3)
        s=copy.deepcopy(self.p['sources'][0]);s.update(id='S2',origin_id='origin2');self.p['sources'].append(s)
        f=copy.deepcopy(self.p['fragments'][0]);f.update(id='F2',source_id='S2');self.p['fragments'].append(f)
        self.p['claims'][0]['fragment_refs'].append('F2');self.p['claims'][0]['deployment_stage']='announcement';self.reject()
    def test_copied_press_release_not_independent(self):self.score(3);self.p['claims'][0]['deployment_stage']='production';self.reject()
    def test_counter_evidence_preserved(self):
        self.score();c=copy.deepcopy(self.p['claims'][0]);c['id']='C2';self.p['claims'].append(c);self.p['claims'][0]['contradiction_refs']=['C2'];self.reject()
    def test_stale_score(self):self.score();self.p['claims'][0]['valid_until']='2026-01-02';self.reject()
    def test_inferred_sector_laundering(self):
        self.score();self.p['sources'][0]['scope']='sector';self.p['claims'][0]['status']='inference';self.reject()
    def test_job_plus_sector_is_not_company_capability(self):
        self.score();self.p['sources'][0]['source_type']='job';self.p['claims'][0]['status']='inference'
        s=copy.deepcopy(self.p['sources'][0]);s.update(id='S2',scope='sector',source_type='research');self.p['sources'].append(s)
        f=copy.deepcopy(self.p['fragments'][0]);f.update(id='F2',source_id='S2');self.p['fragments'].append(f)
        self.p['claims'][0]['fragment_refs'].append('F2');self.reject()
    def test_incomplete_gate_set(self):self.p['use_cases'][0]['gates']=self.p['use_cases'][0]['gates'][:1];self.reject()
    def test_hypothesis_cannot_clear_gates(self):
        self.p['claims'][0]['status']='hypothesis'
        for g in self.p['use_cases'][0]['gates']:g.update(status='pass',claim_refs=['C1'])
        self.p['use_cases'][0]['priority_state']='eligible';self.reject()
    def test_schema_forbids_global_average(self):self.p['maturity']['global_score']=2.5;self.reject()
    def prepare_content(self):
        for i in range(2,7):
            uc=copy.deepcopy(self.p['use_cases'][0]);uc['id']=f'UC{i}';self.p['use_cases'].append(uc)
        return content(self.p)
    def test_valid_frozen_fixture(self):self.assertTrue(v.validate_content(self.prepare_content(),self.p))
    def test_missing_hitl(self):
        c=self.prepare_content();c['run_context']['hitl']=None
        with self.assertRaises(ValueError):v.validate_content(c,self.p)
    def test_dangling_run_refs(self):
        c=self.prepare_content();c['run_context']['claim_refs']=['missing']
        with self.assertRaises(ValueError):v.validate_content(c,self.p)
    def test_changed_frozen_content(self):
        c=self.prepare_content();c['payload']['page1']['title']='Tampered'
        with self.assertRaises(ValueError):v.validate_content(c,self.p)
    def test_changed_package_after_hitl(self):
        c=self.prepare_content();self.p['unknowns'].append('New critical uncertainty')
        with self.assertRaises(ValueError):v.validate_content(c,self.p)
    def test_frozen_uc_projection(self):
        c=self.prepare_content();c['payload']['use_cases'][0]['title']='Changed recommendation';c['payload_sha256']=v.digest(c['payload'])
        with self.assertRaises(ValueError):v.validate_content(c,self.p)
    def test_frozen_source_projection(self):
        c=self.prepare_content();c['payload']['sources'][0]['url']='https://example.org/other';c['payload_sha256']=v.digest(c['payload'])
        with self.assertRaises(ValueError):v.validate_content(c,self.p)
    def test_done_is_not_content_validation(self):
        c=self.prepare_content();c['run_context']['stage']='DONE'
        with self.assertRaises(ValueError):v.validate_content(c,self.p)

if __name__=='__main__':unittest.main()
