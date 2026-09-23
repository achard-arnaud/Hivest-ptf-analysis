"""Gate de disponibilité des preuves avant revue humaine, sans création de données."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def check(entity):
    manifest = json.loads((ROOT / 'companies' / entity / 'manifest.json').read_text())
    missing = []
    ref = manifest.get('package_ref')
    if not ref or not str(ref).endswith('.json'):
        missing.append('package_ref: package JSON manquant')
    elif not (ROOT / ref).is_file():
        missing.append('package_ref: fichier introuvable')
    else:
        from validate import validate_package
        from jsonschema import ValidationError
        try:
            data = json.loads((ROOT / ref).read_text())
            validate_package(data)
            if data['version'] != '0.2.0': missing.append('package_ref: contexte marché v0.2 absent')
        except (ValueError, KeyError, ValidationError) as exc:
            missing.append('package_ref: contrat invalide: ' + str(exc))
    if manifest.get('stage') == 'HITL_PENDING' and missing:
        missing.append('stage: HITL_PENDING prématuré')
    return {'entity_id':entity, 'status':'PASS' if not missing else 'FAIL', 'missing':missing}

if __name__ == '__main__':
    try:
        result = check(sys.argv[1]);print(json.dumps(result, ensure_ascii=False));sys.exit(0 if result['status']=='PASS' else 1)
    except (IndexError, OSError, json.JSONDecodeError) as exc:
        print(json.dumps({'status':'FAIL','errors':[{'code':'E_INPUT','message':str(exc)}]}));sys.exit(2)
