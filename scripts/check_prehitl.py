"""Gate de disponibilité des preuves avant revue humaine, sans création de données."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def check(entity, archive=None):
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
            material=set(manifest.get('material_source_ids', []))
            ids={s['id'] for s in data['sources']}
            if not material or not material <= ids:
                missing.append('material_source_ids: liste absente ou IDs inconnus')
            for s in data['sources']:
                policy=s.get('capture_policy', 'full_original_required')
                if s['id'] in material or s['source_type'] in ('filing','legal_register'):
                    policy='full_original_required'
                if policy == 'full_original_required':
                    if s.get('capture_kind')!='full_original' or s.get('hash_scope')!='original_bytes':
                        missing.append(f'{s["id"]}: original et hash des octets requis')
                elif policy == 'excerpt_by_rights':
                    if s.get('capture_kind')!='selected_excerpt' or s.get('hash_scope')!='excerpt_utf8' or not s.get('rights'):
                        missing.append(f'{s["id"]}: extrait traçable et droits requis')
                else:
                    missing.append(f'{s["id"]}: capture_policy invalide')
            if archive is None:
                missing.append('archive: contrôle des captures indisponible')
            else:
                from validate_bundle import validate_bundle
                try:
                    validate_bundle(ROOT / 'companies' / entity, archive)
                except (ValueError, KeyError, OSError) as exc:
                    missing.append('archive: '+str(exc))
            if data['version'] != '0.2.0': missing.append('package_ref: contexte marché v0.2 absent')
        except (ValueError, KeyError, ValidationError) as exc:
            missing.append('package_ref: contrat invalide: ' + str(exc))
    if manifest.get('stage') == 'HITL_PENDING' and missing:
        missing.append('stage: HITL_PENDING prématuré')
    return {'entity_id':entity, 'status':'PASS' if not missing else 'FAIL', 'missing':missing}

if __name__ == '__main__':
    try:
        result = check(sys.argv[1],sys.argv[2] if len(sys.argv)>2 else None);print(json.dumps(result, ensure_ascii=False));sys.exit(0 if result['status']=='PASS' else 1)
    except (IndexError, OSError, json.JSONDecodeError) as exc:
        print(json.dumps({'status':'FAIL','errors':[{'code':'E_INPUT','message':str(exc)}]}));sys.exit(2)
