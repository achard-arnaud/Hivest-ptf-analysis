# Hivest — Portfolio AI Diagnostic OS

Phase 00, version 0.1.0, 23 septembre 2026. Propriétaire : François-Pro.
Socle de diagnostic public ; aucun diagnostic d'entreprise ni résultat économique n'est encore validé.

Commencer par `AGENTS.md`, puis `program/state.json`. Le dossier `docs/PROGRAM_DESIGN.md` contient les dix sorties du gate PROGRAM_DESIGN_READY.

## Exécution
Python 3.11+ ; installer `requirements.txt`, puis lancer :
```
python -m unittest discover -s tests -v
python scripts/validate.py /chemin/vers/company-package.json
```
Le validateur contrôle la structure et plusieurs invariants de preuve. Il ne vérifie pas la vérité d'une source : les trois revues humaines/agent restent nécessaires.

## Organisation
- `program/` : état, roster, dépendances figées, ordre de passage.
- `contracts/` : contrats JSON Schema exécutables et règles de décision.
- `skills/hivest-portfolio-ai/` : export du router et procédures par étape.
- `templates/` : contrat trois pages et spécification de rendu candidate.
- `tests/` : fixtures adversariales et non-régression, jamais chargées lors de la recherche.
- `wiki/` : index cumulatif, sources des pages et règles de fraîcheur.
- `companies/` : manifests canoniques ; les diagnostics viendront après recherche.

Les sources brutes, runs, traces et rendus de travail restent hors du code. Les données canoniques promues sont versionnées ; les sources à droits restreints restent dans un stockage externe, référencées par URI et SHA-256.

Ce dépôt contient un export de la skill, pas un mécanisme d'installation automatique dans une interface.
