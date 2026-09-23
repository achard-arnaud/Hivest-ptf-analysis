"""Structural validation plus bounded, fail-closed epistemic invariants."""
import hashlib
import json
import sys
import unicodedata
from urllib.parse import urlsplit, urlunsplit
from datetime import date
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker, ValidationError

ROOT = Path(__file__).resolve().parents[1]
REQUIRE_GROUNDED_INFERENCE = True

def excerpt_hash(value):
    return hashlib.sha256(unicodedata.normalize('NFC', value).encode('utf-8')).hexdigest()

def normalized_url(value):
    parts = urlsplit(value)
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip('/') or '/', parts.query, ''))

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
    for key in ('url', 'sha256'):
        seen = {}
        for s in sources.values():
            value = normalized_url(s[key]) if key == 'url' else s[key]
            check(value not in seen or seen[value] == s['origin_id'], 'duplicate source has different origin_id')
            seen[value] = s['origin_id']
    for f in fragments.values():
        refs([f['source_id']], sources)
        check(sources[f['source_id']]['access_status'] != 'inaccessible', 'unread source used')
        check(excerpt_hash(f['excerpt']) == f['sha256'], 'fragment hash mismatch')
    for c in claims.values():
        refs(c['fragment_refs'], fragments)
        refs(c['basis_claim_refs'] + c['contradiction_refs'], claims)
        if c['scope'] == 'company':
            check(c['entity_id'] == data['entity_id'], 'cross-company claim')
        if c['observed_at']:
            check(date.fromisoformat(c['observed_at']) <= cutoff, 'claim after cutoff')
            publications = [sources[fragments[f]['source_id']]['published_at'] for f in c['fragment_refs']]
            check(all(p is None or p <= c['observed_at'] for p in publications), 'claim observed before source publication')
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
    for c in claims.values():
        if REQUIRE_GROUNDED_INFERENCE and c['status'] == 'inference':
            check(bool(origins(c['id'])), 'inference lacks source anchor')
        if c['status'] == 'fact' and origins(c['id']):
            check(not (c['confidence'] == 'high' and all(sources[s]['access_status'] == 'partial' for s in origins(c['id']))), 'partial-only fact cannot have high confidence')
    def fresh(cid):
        expiry = claims[cid]['valid_until']
        return expiry is None or date.fromisoformat(expiry) >= cutoff
    def company_origin(cid):
        return any(sources[s]['scope']=='company' and data['entity_id'] in sources[s]['entity_ids'] and sources[s]['source_type'] not in ('job','social') for s in origins(cid))
    check(len({x['id'] for x in data['maturity']['dimensions']}) == 8, 'missing/duplicate maturity dimension')
    for d in data['maturity']['dimensions']:
        refs(d['claim_refs'] + d['counter_evidence'], claims)
        check((d['score'] is None) == (d['status']=='unknown'), 'unknown must be null')
        if d['score'] is not None:
            check(bool(d['claim_refs']), 'maturity score without evidence')
            for cid in d['claim_refs']:
                c=claims[cid]
                check(c['scope']=='company' and c['status'] in ('fact','inference'), 'maturity needs company evidence')
                check(fresh(cid), 'stale maturity evidence')
                check(set(c['contradiction_refs']) <= set(d['counter_evidence']), 'counter-evidence dropped')
            ss={sid for cid in d['claim_refs'] for sid in origins(cid)}
            for cid in d['claim_refs']:
                check(company_origin(cid), 'scored claim needs non-job company evidence')
            if d['score'] >= 3:
                check(len({sources[s]['origin_id'] for s in ss}) >= 2, 'production score lacks independent corroboration')
            if d['score'] >= 3:
                check(any(claims[c]['status']=='fact' and claims[c]['scope']=='company' and company_origin(c) and fresh(c) and claims[c]['deployment_stage'] in (('scaled',) if d['score']==4 else ('production','scaled')) for c in d['claim_refs']), 'announcement is not production')
    activities=index(data['value_chain']); ucs=index(data['use_cases'])
    if data['version'] == '0.2.0':
        drivers = index(data['drivers'])
        for arena in data['market_context']['arenas']:
            refs(arena['claim_refs'], claims)
            check(all(claims[c]['scope'] in ('sector','company') for c in arena['claim_refs']), 'market arena needs external/company claim')
        for peer in data['market_context']['peers']: refs(peer['claim_refs'], claims)
        for driver in drivers.values():
            refs(driver['external_signal_claim_refs'] + driver['exposure_claim_refs'] + driver['counter_evidence_refs'], claims)
            check(all(claims[c]['scope'] in ('sector','company') for c in driver['external_signal_claim_refs']), 'driver lacks external signal')
            check(bool(driver['exposure_claim_refs'] or driver['exposure_hypothesis']), 'driver lacks exposure')
            check(all(claims[c]['scope']=='company' for c in driver['exposure_claim_refs']), 'driver exposure needs company claim')
        cost_bases = {}
    for a in activities.values():
        refs(a['claim_refs'],claims); refs(a['ai_opportunity_refs'],ucs)
    for u in ucs.values():
        if data['version'] == '0.2.0':
            refs(u['driver_refs'], drivers)
            check(bool(u['driver_refs']) or u['is_prerequisite'], 'non-prerequisite use case lacks driver')
            if u['value_strategy'] == 'BLUE_OCEAN':
                check(bool(u['new_demand_hypothesis'] and u['customer_test']), 'BLUE_OCEAN needs demand hypothesis and customer test')
            if u['value_strategy'] in ('COST_REDUCTION','COST_AVOIDANCE') and u['cost_base_id']:
                previous = cost_bases.get(u['cost_base_id'])
                check(not previous or bool(u['double_count_justification'] and previous['double_count_justification']), 'double counting cost base')
                cost_bases[u['cost_base_id']] = u
        refs(u['company_claim_refs']+u['sector_claim_refs'],claims)
        for cid in u['company_claim_refs']:
            check(claims[cid]['scope']=='company', 'sector evidence in company list')
        for cid in u['sector_claim_refs']:
            check(claims[cid]['scope']=='sector', 'company evidence in sector list')
        if u['status']=='fact':
            check(any(claims[c]['status']=='fact' and fresh(c) and company_origin(c) and claims[c]['deployment_stage'] in ('experiment','production','scaled') for c in u['company_claim_refs']), 'observed UC lacks deployed company fact')
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
                check(all(fresh(c) and company_origin(c) for c in g['claim_refs']), 'gate pass requires current non-job company evidence')
        check({'quick_win':'0-6','structural':'6-18','transformation':'18-36'}[u['family']]==u['horizon'], 'family/horizon mismatch')
    for p in data['strategic_positions']:
        refs([p['activity_id']],activities);refs(p['claim_refs'],claims)
    return True

def validate_content(content, package, *, bundle_hash=None):
    validate_package(package)
    schema(content,'three-pager.schema.json')
    run=content['run_context']; payload=content['payload']; hitl=run['hitl']
    if package['version']=='0.2.0':
        check(bundle_hash is not None and hitl is not None and hitl.get('bundle_sha256')==bundle_hash,'v0.2 requires validated bundle and matching human approval')
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
    if package['version']=='0.2.0':
        check(content['version']=='0.2.0' and run['version']=='0.2.0', 'content/package version mismatch')
        shortlist=[ucs[x] for x in payload['page3']['use_case_ids'] if not ucs[x]['is_prerequisite']]
        check(6 <= len(shortlist) <= 10, 'shortlist requires 6-10 AI opportunities excluding prerequisites')
        check(all(u['driver_refs'] for u in shortlist), 'shortlisted use case lacks driver')
    check(payload['use_cases']==[ucs[x] for x in payload['page3']['use_case_ids']], 'frozen UC projection differs from package')
    check(payload['sources']==[sources[x] for x in payload['source_ids']], 'frozen source projection differs from package')
    def walk(value):
        if isinstance(value,dict):
            if 'claim_refs' in value:
                refs(value['claim_refs'],claims)
                if value['status']!='unknown': check(bool(value['claim_refs']),'content lacks lineage')
                if value['status']=='fact':
                    check(all(claims[c]['status']=='fact' for c in value['claim_refs']),'hypothesis promoted by composition')
                    check(all(not claims[c]['valid_until'] or claims[c]['valid_until'] >= package['cutoff'] for c in value['claim_refs']), 'stale fact in payload')
            for x in value.values():walk(x)
        elif isinstance(value,list):
            for x in value:walk(x)
    walk(payload)
    return True

if __name__=='__main__':
    def output(status, code=None, message=None, path=None):
        print(json.dumps({'status':status,'errors':[] if code is None else [{'code':code,'path':path or '', 'message':message}]}, ensure_ascii=False))
    args = sys.argv[1:]
    if len(args)==1: args=['package', args[0]]  # legacy invocation
    if (len(args)==2 and args[0]=='package') or (len(args)==3 and args[0]=='content'):
        try:
            if args[0]=='package': validate_package(json.loads(Path(args[1]).read_text(encoding='utf-8')))
            else: validate_content(json.loads(Path(args[1]).read_text(encoding='utf-8')), json.loads(Path(args[2]).read_text(encoding='utf-8')))
            output('PASS')
        except (OSError, json.JSONDecodeError) as exc:
            output('FAIL','E_INPUT',str(exc));sys.exit(2)
        except ValidationError as exc:
            output('FAIL','E_SCHEMA',exc.message,'/'.join(map(str,exc.path)));sys.exit(1)
        except (ValueError, KeyError, IndexError, TypeError) as exc:
            output('FAIL','E_INVARIANT',str(exc));sys.exit(1)
    else:
        output('FAIL','E_USAGE','Usage: validate.py package <file> | content <content> <package>');sys.exit(2)

