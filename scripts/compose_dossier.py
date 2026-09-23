"""Compile canonical modules into a user-facing pre-HITL view. No new analysis."""
from pathlib import Path
import argparse
import json

def compose(company,output):
    c=Path(company)
    manifest=json.loads((c/'manifest.json').read_text(encoding='utf-8'))
    package_ref=c/'package.json'
    version=json.loads(package_ref.read_text(encoding='utf-8'))['version'] if package_ref.is_file() else 'unversioned'
    files=sorted((c/'analysis').glob('*.md'))+sorted((c/'reviews').glob('*.md'))+[c/'evidence/coverage.md',c/'source_register.md']
    out=(f'# {manifest["entity_id"].upper()} — diagnostic business, IA et ML — dossier pré-HITL v{version}\n\n'
         f'Cutoff : {manifest["cutoff"]}. Projection des artefacts canoniques. Workflow : {manifest["stage"]} ; '
         f'capture : {manifest.get("capture_status", "à établir")}. Aucune approbation de rendu final attribuée.\n\n')
    for p in files:
        if not p.is_file():
            raise FileNotFoundError(p)
        out+='\n---\n\n'+p.read_text(encoding='utf-8')
    out+=(f'\n---\n\n## Méthode et loopback\n\nLe dossier est une projection compilée. '
          f'Les sources, claims, analyses et questions canoniques restent dans `companies/{manifest["entity_id"]}/`. '
          'Une modification de preuve réouvre les conclusions qu’elle soutient.\n')
    Path(output).write_text(out,encoding='utf-8')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('company');p.add_argument('output');a=p.parse_args();compose(a.company,a.output)
