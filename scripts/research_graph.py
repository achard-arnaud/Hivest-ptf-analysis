"""Bounded context selection and impact propagation. Never performs network work."""
import argparse,json
from pathlib import Path

def index_graph(g):
    nodes={n['id']:n for n in g['nodes']}
    if len(nodes)!=len(g['nodes']): raise ValueError('duplicate graph node')
    def visit(k,stack):
        if k not in nodes:raise ValueError('dangling graph dependency')
        if k in stack:raise ValueError('graph cycle')
        for dep in nodes[k]['depends_on']:visit(dep,stack|{k})
    for k in nodes:visit(k,set())
    return nodes

def context(g,target,budget=12):
    nodes=index_graph(g);order=[]
    def walk(k):
        if k not in nodes:raise ValueError('unknown target')
        for dep in nodes[k]['depends_on']:walk(dep)
        if k not in order:order.append(k)
    walk(target)
    if len(order)>budget:raise ValueError('context budget exceeded: narrow question; no silent truncation')
    return [nodes[k] for k in order]

def affected(g,changed):
    nodes=index_graph(g)
    if changed not in nodes:raise ValueError('unknown changed node')
    result={changed}
    while True:
        extra={k for k,n in nodes.items() if set(n['depends_on']) & result}
        if extra<=result:break
        result|=extra
    return sorted(result)

def tasks(g,stage):
    return [q for q in g['questions'] if q['status']=='open' and stage in q['affects']]

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('graph');p.add_argument('target');p.add_argument('--changed',action='store_true');p.add_argument('--budget',type=int,default=12);a=p.parse_args()
    g=json.loads(Path(a.graph).read_text())
    result={'affected_nodes':affected(g,a.target)} if a.changed else {'context':context(g,a.target,a.budget),'targeted_tasks':tasks(g,a.target),'execution':'next_authorized_run_only'}
    print(json.dumps(result,ensure_ascii=False,indent=2))
