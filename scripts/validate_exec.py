"""Validate an executive payload against a locally checked evidence archive."""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'renderers' / 'three_pager_exec'))
from render_exec import R  # noqa: E402
from validate import check, digest  # noqa: E402
from validate_bundle import validate_bundle  # noqa: E402


def validate_exec_payload(payload, directory, archive):
    base = Path(directory)
    result = validate_bundle(base, archive)
    check(result['snapshot_integrity'] == 'verified', 'archive not verified')
    package = json.loads((base / 'package.json').read_text(encoding='utf-8'))
    context = json.loads((base / 'strategic_context.json').read_text(encoding='utf-8'))
    graph = json.loads((base / 'research_graph.json').read_text(encoding='utf-8'))
    check(payload['entity_id'] == package['entity_id'], 'exec entity mismatch')
    check(payload['cutoff'] == package['cutoff'], 'exec cutoff differs from evidence bundle')
    source_ids = {source['id'] for source in package['sources']}
    for name, figure in payload['figures'].items():
        check(figure['src'] in source_ids, f'figure {name} refers to unknown source')
    bundle_hash = digest({'package': package, 'context': context, 'graph': graph})
    check(payload['lineage'].get('bundle_sha256') == bundle_hash, 'exec lineage bundle hash mismatch')
    R(payload).build()
    check(base.resolve() == (ROOT / 'companies' / package['entity_id']).resolve(),
          'exec bundle must be the canonical company directory')
    from check_prehitl import check as check_capture
    capture = check_capture(package['entity_id'], archive)
    check(capture['status'] == 'PASS', 'pre-HITL capture gate: ' + '; '.join(capture['missing']))
    return {'status': 'BUNDLE_STRUCTURALLY_VALIDATED_UNFROZEN', 'bundle_sha256': bundle_hash,
            'render_authorized_for_demo': True, 'committee_authorized': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', type=Path)
    parser.add_argument('payload', type=Path)
    parser.add_argument('--archive', type=Path, required=True)
    args = parser.parse_args()
    payload = json.loads(args.payload.read_text(encoding='utf-8'))
    print(json.dumps(validate_exec_payload(payload, args.directory, args.archive), ensure_ascii=False))
