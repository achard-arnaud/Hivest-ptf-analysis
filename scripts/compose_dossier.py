"""Compile canonical modules into a user-facing pre-HITL view. No new analysis."""
from pathlib import Path
import argparse

def compose(company,output):
    c=Path(company)
    files=sorted((c/'analysis').glob('*.md'))+sorted((c/'reviews').glob('*.md'))+[c/'evidence/coverage.md',c/'source_register.md']
    out='# SPHERE — diagnostic business, IA et ML — dossier pré-HITL v0.3\n\nCutoff :23 septembre2026. Projection des artefacts canoniques. Workflow : RESEARCH ; gate archivage des originaux ouvert. Aucune approbation de rendu final attribuée.\n\n'
    for p in files:out+='\n---\n\n'+p.read_text()
    out+='\n---\n\n## Méthode et loopback\n\nLe dossier est une vue compilée. La mémoire canonique est découpée en preuves,claims,analyses et questions liées. Une mind map rend ces liens visibles ; les recherches suivantes sont déclenchées par les inconnues et changements, avec budgets et conditions d’arrêt. Voir le dépôt : docs/LOOPBACK_SPHERE_V03.md et companies/sphere/INDEX.md.\n'
    Path(output).write_text(out)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('company');p.add_argument('output');a=p.parse_args();compose(a.company,a.output)
