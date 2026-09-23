# Hivest — Portfolio AI Diagnostic OS

Programme en pilotes, contrat de bundle v0.2, profil exec v0.3. Propriétaire : François-Pro.
Sphere possède un bundle structuré, mais la capture des originaux et la revue humaine restent ouvertes.

## Profil exec de démonstration

Le profil `exec` v0.3 a son contrat et son renderer dans `renderers/three_pager_exec/`. Le contrat trois pages v0.1 reste le profil `audit`. La fixture Sphere vient d'un autre environnement et cite trois sources supplémentaires absentes du bundle actuel ; son cutoff (24/09/2026) diffère de celui du bundle (23/09/2026). Elle reste dans `tests/fixtures/exec/` pour les tests de présentation.

```bash
python renderers/three_pager_exec/render_exec.py tests/fixtures/exec/sphere_unverified_v0.3.json /tmp/sphere_exec
# Après installation de playwright et de Chromium :
python renderers/three_pager_exec/render_exec.py tests/fixtures/exec/sphere_unverified_v0.3.json /tmp/sphere_exec --pdf
```

Le rendu sans `--pdf` vérifie schéma et cohérence et écrit HTML et manifeste. Avec `--pdf`, il crée PDF, trois PNG et `qa.json`, à relire visuellement. Le manifeste reste `UNVERIFIED_DEMO` : un contrôle de mise en page ne remplace pas un bundle validé ni GO_DRAFT. Le navigateur peut être fourni via `NICE_CHROMIUM_PATH` ; sinon Playwright utilise le sien. Les fichiers générés vont hors du dépôt.

Pour un **nouveau payload aligné** sur un bundle : fournir `--bundle companies/<id> --archive /chemin/vers/archive.json`. Le contrôle exige les captures vérifiées, le cutoff identique, les sources de chaque figure et `lineage.bundle_sha256` égal au hash canonique du bundle. Le manifeste indique alors `BUNDLE_STRUCTURALLY_VALIDATED_UNFROZEN` ; cela ne vaut ni revue humaine ni diffusion en comité. `python scripts/check_prehitl.py sphere /chemin/vers/archive.json` contrôle séparément la politique de capture.

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
- `companies/` : manifests et diagnostics canoniques en cours de recherche.

Les sources brutes, runs, traces et rendus de travail restent hors du code. Les données canoniques promues sont versionnées ; les sources à droits restreints restent dans un stockage externe, référencées par URI et SHA-256.

Ce dépôt contient un export de la skill, pas un mécanisme d'installation automatique dans une interface.
