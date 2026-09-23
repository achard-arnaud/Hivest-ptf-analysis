"""Structural validation plus bounded, fail-closed epistemic invariants."""
import hashlib
import json
import sys
from datetime import date
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]

def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()

def check(condition, message):
    if not condition:
        raise ValueError(message)

def schema(data, name):
    spec = json.loads((ROOT / 'contracts' / name).read_text())
    Draft202012Validator.check_schema(spec)
    Draft202012Validator(spec, format_checker=FormatChecker()).validate(data)

def index(items):
    result = {x['id']: x for x in items}
    check(len(result) == len(items), 'duplicate IDs')
    return result

def refs(values, registry):
    check(all(x in registry for x in values), 'dangling references')

def validate_package(data):
    schema(data, 'company-package.schema.json')
    sources, fragments, claims = [index(data[k]) for k in ('sources','fragments','claims')]
    cutoff = date.fromisoformat(data['cutoff'])
    for s in sources.values():
        if s['published_at']:
            check(date.fromisoformat(s['published_at']) <= cutoff, 'source after cutoff')
        check(date.fromisoformat(s['accessed_at']) >= date.fromisoformat(s['published_at'] or s['accessed_at']), 'access before publication')
    for f in fragments.values():
        refs([f['source_id']], sources)
        check(sources[f['source_id']]['access_status'] != 'inaccessible', 'unread source used')
        check(hashlib.sha256(f['excerpt'].encode()).hexdigest() == f['sha256'], 'fragment hash mismatch')
    for c in claims.values():
        refs(c['fragment_refs'], fragments)
        refs(c['basis_claim_refs'] + c['contradiction_refs'], claims)
        if c['scope'] == 'company':
            check(c['entity_id'] == data['entity_id'], 'cross-company claim')
        if c['observed_at']:
            check(date.fromisoformat(c['observed_at']) <= cutoff, 'claim after cutoff')
        if c['status'] == 'fact':
            check(bool(c['fragment_refs']), 'fact without direct evidence')
            if c['scope'] == 'company':
                check(any(sources[fragments[f]['source_id']]['scope']=='company' and c['entity_id'] in sources[fragments[f]['source_id']]['entity_ids'] for f in c['fragment_refs']), 'sector laundering')
        if c['status'] in ('inference','recommendation'):
            check(bool(c['fragment_refs'] or c['basis_claim_refs']), 'inference without basis')
    def origins(cid, visiting=None):
        visiting = set() if visiting is None else visiting
        check(cid not in visiting, 'cyclic claim basis')
        c=claims[cid]
        result={fragments[f]['source_id'] for f in c['fragment_refs']}
        for b in c['basis_claim_refs']:
            result |= origins(b, visiting | {cid})
        return result
    for c in claims: origins(c)
    check(len({x['id'] for x in data['maturity']['dimensions']}) == 8, 'missing/duplicate maturity dimension')
    for d in data['maturity']['dimensions']:
        refs(d['claim_refs'] + d['counter_evidence'], claims)
        check((d['score'] is None) == (d['status']=='unknown'), 'unknown must be null')
        if d['score'] is not None:
            check(bool(d['claim_refs']), 'maturity score without evidence')
            for cid in d['claim_refs']:
                c=claims[cid]
                check(c['scope']=='company' and c['status'] in ('fact','inference'), 'maturity needs company evidence')
                check(not c['valid_until'] or date.fromisoformat(c['valid_until']) >= cutoff, 'stale maturity evidence')
                check(set(c['contradiction_refs']) <= set(d['counter_evidence']), 'counter-evidence dropped')
            ss={sid for cid in d['claim_refs'] for sid in origins(cid)}
            for cid in d['claim_refs']:
                check(any(sources[s]['scope']=='company' and data['entity_id'] in sources[s]['entity_ids'] and sources[s]['source_type'] not in ('job','social') for s in origins(cid)), 'scored claim needs non-job company evidence')
            if d['score'] >= 3:
                check(len({sources[s]['origin_id'] for s in ss}) >= 2, 'production score lacks independent corroboration')
            if d['id']=='delivery' and d['score'] >= 3:
                check(any(claims[c]['status']=='fact' and claims[c]['deployment_stage'] in (('scaled',) if d['score']==4 else ('production','scaled')) for c in d['claim_refs']), 'announcement is not production')
    activities=index(data['value_chain']); ucs=index(data['use_cases'])
    for a in activities.values():
        refs(a['claim_refs'],claims); refs(a['ai_opportunity_refs'],ucs)
    for u in ucs.values():
        refs(u['company_claim_refs']+u['sector_claim_refs'],claims)
        for cid in u['company_claim_refs']:
            check(claims[cid]['scope']=='company', 'sector evidence in company list')
        for cid in u['sector_claim_refs']:
            check(claims[cid]['scope']=='sector', 'company evidence in sector list')
        if u['status']=='fact':
            check(any(claims[c]['status']=='fact' for c in u['company_claim_refs']), 'observed UC lacks company fact')
        gates=[g['status'] for g in u['gates']]
        gate_names=[g['name'] for g in u['gates']]
        check(len(set(gate_names))==len(gate_names), 'duplicate hard gate')
        check(set(gate_names)=={'data_rights','security_ot','human_control','ownership','feasibility'}, 'required hard gates missing')
        expected='blocked' if 'fail' in gates else 'validation_required' if 'unknown' in gates else 'eligible'
        check(u['priority_state']==expected, 'hard gate cannot be compensated')
        for g in u['gates']:
            refs(g['claim_refs'],claims)
            if g['status']=='pass':
                check(bool(g['claim_refs']), 'gate pass without evidence')
                check(all(claims[c]['status']=='fact' and claims[c]['scope']=='company' for c in g['claim_refs']), 'gate pass requires company facts')
        check({'quick_win':'0-6','structural':'6-18','transformation':'18-36'}[u['family']]==u['horizon'], 'family/horizon mismatch')
    for p in data['strategic_positions']:
        refs([p['activity_id']],activities);refs(p['claim_refs'],claims)
    return True

def validate_content(content, package):
    validate_package(package)
    schema(content,'three-pager.schema.json')
    run=content['run_context']; payload=content['payload']; hitl=run['hitl']
    check(run['entity_id']==payload['entity_id']==package['entity_id'],'entity mismatch')
    check(payload['cutoff']==package['cutoff'],'cutoff mismatch')
    check(run['package_sha256']==digest(package),'package changed after review')
    check(run['stage']=='FROZEN','this validator accepts FROZEN input only; rendered/DONE need separate QA')
    check(run['red_team_verdict'] in ('SURVIVES_RED_TEAM','SURVIVES_WITH_NARROWING'),'unresolved red-team')
    check(hitl is not None and hitl['decision']=='GO_DRAFT','missing human GO_DRAFT')
    check(hitl['package_sha256']==digest(package),'HITL does not cover package')
    check(content['payload_sha256']==digest(payload),'frozen content changed')
    claims=index(package['claims']); sources=index(package['sources']); ucs=index(package['use_cases'])
    refs(run['source_refs'],sources);refs(run['claim_refs'],claims)
    refs(payload['source_ids'],sources); refs(payload['page3']['use_case_ids'],ucs)
    check(payload['use_cases']==[ucs[x] for x in payload['page3']['use_case_ids']], 'frozen UC projection differs from package')
    check(payload['sources']==[sources[x] for x in payload['source_ids']], 'frozen source projection differs from package')
    def walk(value):
        if isinstance(value,dict):
            if 'claim_refs' in value:
                refs(value['claim_refs'],claims)
                if value['status']!='unknown': check(bool(value['claim_refs']),'content lacks lineage')
                if value['status']=='fact':
                    check(all(claims[c]['status']=='fact' for c in value['claim_refs']),'hypothesis promoted by composition')
            for x in value.values():walk(x)
        elif isinstance(value,list):
            for x in value:walk(x)
    walk(payload)
    return True

if __name__=='__main__':
    try:
        validate_package(json.loads(Path(sys.argv[1]).read_text()))
        print('PASS: schema + epistemic invariants (source truth still requires review)')
    except (ValueError,IndexError,KeyError) as exc:
        raise SystemExit(str(exc))
