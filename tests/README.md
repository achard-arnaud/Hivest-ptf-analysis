# Validation scope

Run `python -m unittest discover -s tests -v` from the repository root.

Fixtures are synthetic, defined next to the assertions. They never establish facts about Hivest or its portfolio.
These tests validate schema and epistemic failure modes. They cannot prove source truth, causal ROI, quality of a 7S interpretation or visual readability.

Pilot acceptance still requires: source review, three review lenses, actual human HITL, three-page PDF render and inspection, then cross-pilot loopback.

## Dossier réel v0.2
`test_sphere_bundle.py` valide Sphere et des mutations critiques ;64tests au total après fusion des contrôles amont. `validate_bundle.py --archive` ajoute le contrôle des captures externes, non disponible automatiquement dans CI publique. Les tests ne certifient ni vérité des sources ni GO_DRAFT.
