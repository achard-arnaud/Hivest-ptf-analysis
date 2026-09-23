"""Actual v0.2 dossier gates. Schema + semantic links + local integrity; not truth/GO_DRAFT."""
import argparse,hashlib,json
from pathlib import Path
from validate import validate_package,validate_content,digest,schema,check,index,refs
from research_graph import index_graph

def load(path):return json.loads(Path(path).read_text())
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def safe(base,relative):
    target=(Path(base)/relative).resolve()
    check(target.is_relative_to(Path(base).resolve()),'path escapes company bundle')
    check(target.is_file(),'missing bundle artifact: '+relative)
    return target

def validate_bundle(directory,archive=None):
    base=Path(directory);p=load(base/'package.json');c=load(base/'strategic_context.json');g=load(base/'research_graph.json')
    check(p['version']=='0.2.0','legacy cannot pass new bundle gate');validate_package(p);schema(c,'strategic-context.schema.json')
    check(p['entity_id']==c['entity_id']==g['entity_id'],'bundle entity mismatch')
    check(p['cutoff']==c['cutoff'],'bundle cutoff mismatch')
    check(p['strategic_context_ref']=='strategic_context.json','unexpected context path')
    claims=index(p['claims']);sources=index(p['sources']);ucs=index(p['use_cases']);acts=index(p['value_chain'])
    check({x['role'] for x in c['leaders']}=={'COO','DSI'} and len(c['leaders'])==2,'two leadership roles required')
    for role in c['leaders']:
        check((role['person'] is None)==(role['status']=='unknown'),'leadership unknown mismatch')
        refs(role['source_refs'],sources)
        if role['status']=='verified_group':check(role['scope']=='group' and bool(role['source_refs']),'subsidiary promoted to group')
    check(c['ml_strategy']['observed_status'] in ('unknown','observed'),'ML strategy status required')
    refs(c['ml_strategy']['observed_claim_refs'],claims)
    if c['ml_strategy']['observed_status']=='observed':
        check(any(claims[x]['status']=='fact' and claims[x]['scope']=='company' for x in c['ml_strategy']['observed_claim_refs']),'ML proposed is not observed')
    safe(base,c['ml_strategy']['search_ref'])
    for segment in c['segments']:
        refs(segment['claim_refs'],claims)
        if segment['bcg'] is not None:check(segment['market_growth'] is not None and segment['relative_market_share'] is not None,'BCG missing market axes')
        check(segment['revenue_year']<=int(p['cutoff'][:4]),'future segment')
    check(sum(x['revenue_share'] for x in c['segments'])==100,'segment mix reconciliation')
    check(set(c['frameworks'])=={'porter','four_p','swot','vrio','seven_s'},'missing business framework')
    for path in c['frameworks'].values():safe(base,path)
    check(len(c['opportunity_links'])==len(ucs),'opportunity mapping incomplete')
    seen=set()
    for m in c['opportunity_links']:
        refs([m['use_case_id']],ucs);refs([m['activity_id']],acts)
        check(m['use_case_id'] not in seen,'duplicate opportunity link');seen.add(m['use_case_id'])
        check(m['driver_id'] in c['driver_ids'],'unknown driver')
        check(m['use_case_id'] in acts[m['activity_id']]['ai_opportunity_refs'],'activity mapping broken')
        check(bool(m['baseline']) and bool(m['kpi']) and m['page']==3,'ML/baseline/page link missing')
    refs(c['shortlist_ids'],ucs);check(6<=len(set(c['shortlist_ids']))<=10,'shortlist cardinality')
    check(all(x['former_id'] not in ucs for x in c['prerequisites']),'data prerequisite presented as AI case')
    check({r['kind'] for r in c['reviews']}=={'contracts','alternative','decision'},'three reviews required')
    for r in c['reviews']:
        check(r['verdict'] in ['SURVIVES_RED_TEAM','SURVIVES_WITH_NARROWING','REOPEN_TARGETED','PIVOT_REQUIRED'],'invalid review verdict');safe(base,r['path'])
    nodes=index_graph(g);questions={q['id']:q for q in g['questions']};check(len(questions)==len(g['questions']),'duplicate question');refs(c['critical_questions'],questions)
    for n in nodes.values():
        safe(base,n['path']); refs(n['source_claim_refs'],claims)
    for q in questions.values():
        refs(q['affects'],nodes);check(q['budget_queries']>0 and bool(q['trigger']) and bool(q['stop_condition']),'unbounded research')
    for path,expected in c['artifact_hashes'].items():check(sha(safe(base,path))==expected,'artifact hash mismatch: '+path)
    required_paths={n['path'] for n in nodes.values()} | set(c['frameworks'].values()) | {r['path'] for r in c['reviews']} | {'research_graph.json','evidence/sources.json','evidence/fragments.json','evidence/claims.json'}
    check(required_paths <= set(c['artifact_hashes']),'artifact hash coverage missing')
    # Integrity is explicit: an excerpt hash never masquerades as a full original hash.
    fragments=index(p['fragments'])
    for s in sources.values():check(s.get('capture_kind')=='selected_excerpt' and s.get('hash_scope')=='excerpt_utf8','capture hash scope unsupported')
    if archive:
        captures={x['id']:x for x in load(archive)['sources']}
        for s in sources.values():
            check(s['id'] in captures and 'excerpt' in captures[s['id']],'missing capture')
            check(hashlib.sha256(captures[s['id']]['excerpt'].encode()).hexdigest()==s['sha256'],'source capture hash mismatch')
            for f in fragments.values():
                if f['source_id']==s['id']:check(f['excerpt'] in captures[s['id']]['excerpt'],'fragment not in capture')
    # No automatic human decision; valid bundle may deliberately remain pre-HITL.
    check(c['render_status']=='not_authorized','use separate human freeze gate')
    return {'status':'PASS','company':p['entity_id'],'cases':len(ucs),'claims':len(claims),'snapshot_integrity':'verified' if archive else 'not_checked_external_archive_required','render_authorized':False}

def validate_freeze(content,directory,archive):
    validate_bundle(directory,archive)
    base=Path(directory);p=load(base/'package.json');c=load(base/'strategic_context.json');g=load(base/'research_graph.json')
    bundle_hash=digest({'package':p,'context':c,'graph':g})
    hitl=content['run_context'].get('hitl')
    check(hitl is not None and hitl['decision']=='GO_DRAFT','human GO_DRAFT required')
    open_ids={q['id'] for q in g['questions'] if q['status']=='open'}
    check(open_ids <= set(hitl.get('accepted_unknown_ids',[])),'critical unknowns not accepted')
    check(all(r['verdict'] in ('SURVIVES_RED_TEAM','SURVIVES_WITH_NARROWING') for r in c['reviews']),'unresolved review')
    return validate_content(content,p,bundle_hash=bundle_hash)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('directory');ap.add_argument('--archive');a=ap.parse_args();print(json.dumps(validate_bundle(a.directory,a.archive),ensure_ascii=False))
