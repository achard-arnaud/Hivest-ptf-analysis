# Hivest — Portfolio AI Diagnostic OS

Diagnostic de création de valeur et de maturité IA des participations Hivest, piloté par des preuves et une décision humaine. Profil François-Pro. Le dépôt est un **OS documentaire et de validation** : il ne déploie pas de produit ni ne recommande de fournisseur.

## État et points d'entrée

La source de vérité sur l'avancement est [`program/state.json`](program/state.json), puis `companies/<id>/manifest.json` pour chaque société. Au 25 septembre 2026, le programme est en **PILOTS**, avec Sphere et STG ; `production_allowed=false`. Sphere possède un bundle v0.2 structuré, mais son archivage des originaux et la revue humaine restent ouverts. STG est en recherche. Les autres dossiers ont des niveaux de couverture variables : ne pas déduire leur gate de l'existence d'un texte ou d'un PDF.

| Besoin | Lire d'abord | Puis |
|---|---|---|
| Reprendre un run | [`AGENTS.md`](AGENTS.md) | `program/state.json` → `companies/<id>/manifest.json` → `companies/<id>/INDEX.md` si présent → [workflow](skills/hivest-portfolio-ai/references/workflow.md) |
| Comprendre le code et ses limites | [Carte du code](docs/architecture/code-map.md) | [`contracts/decision-rules.md`](contracts/decision-rules.md) |
| Exécuter une étape métier | [Skill unique](skills/hivest-portfolio-ai/SKILL.md) | Une seule procédure d'étape ; entrée, sortie et suite dans le [workflow](skills/hivest-portfolio-ai/references/workflow.md) |
| Comprendre les gates | [Règles de l'agent](docs/agent/gates.md) | Schémas dans `contracts/` et validateurs dans `scripts/` |

## Parcours de travail

`intake et preuves → marché et drivers → diagnostic → opportunités → trois revues et HITL → composition et rendu → loopback`.

Le [workflow](skills/hivest-portfolio-ai/references/workflow.md) donne pour **chaque passage** les artefacts d'entrée et de sortie, le contrôle avant relais, et le chemin de la procédure suivante. `research-graph.md` est chargé seulement pour une reprise, une question de recherche ou une intégration ; `exec-writing.md` seulement pour la branche de rendu exec. Il n'y a qu'une skill programme, avec des références conditionnelles, et non une skill par rôle.

Preuve canonique : **source → fragment → claim → analyse → décision → contenu gelé**. Une inconnue est `null`, pas zéro ; les faits sectoriels et les hypothèses d'entreprise restent séparés. Les hard gates priment sur les classements. Les sources brutes et les runs restent hors du dépôt ; seules les références et connaissances revues sont promues. Voir [gates](docs/agent/gates.md) et [reprise/contextes](docs/agent/context-and-resume.md).

## Exécuter et contrôler

Python 3.11+ :

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python scripts/validate.py package companies/sphere/package.json
python scripts/validate_bundle.py companies/sphere
python scripts/check_prehitl.py sphere /chemin/externe/vers/archive.json
```

`validate_bundle.py` sans `--archive` contrôle schéma, liens et fichiers locaux, **pas** l'intégrité des captures externes ; avec `--archive`, il contrôle le hash selon la nature déclarée de chaque capture. `check_prehitl.py` impose de plus les originaux requis pour les sources matérielles. Un contrôle structurel ne certifie ni la vérité des sources ni GO_DRAFT. L'archive d'exemple n'est pas incluse dans ce dépôt.

Pour tester uniquement la **mise en page exec** avec la fixture non vérifiée :

```bash
python renderers/three_pager_exec/render_exec.py tests/fixtures/exec/sphere_unverified_v0.3.json /tmp/hivest-exec
# Après installation de Playwright et Chromium :
python renderers/three_pager_exec/render_exec.py tests/fixtures/exec/sphere_unverified_v0.3.json /tmp/hivest-exec --pdf
```

Le premier appel écrit HTML et manifeste `UNVERIFIED_DEMO`. Le second ajoute PDF, trois PNG et `qa.json` à inspecter. Pour un **nouveau payload aligné** sur un bundle et ses captures, fournir ensemble `--bundle companies/<id> --archive /chemin/externe/vers/archive.json` ; la validation renvoie `BUNDLE_STRUCTURALLY_VALIDATED_UNFROZEN` avec `committee_authorized=false`, tandis que le manifeste conserve le statut de preuve. La fixture Sphere a un cutoff et des sources différents du bundle courant : elle ne doit pas être présentée comme preuve. Le profil audit a un schéma et un validateur de contenu gelé ; le renderer présent dans le dépôt est celui du profil exec. Voir [carte du code](docs/architecture/code-map.md).

## Arborescence utile

- `program/` : état, roster et dépendances ; `companies/` : manifest, bundle et analyses propres à chaque entreprise ; `wiki/` : connaissance sectorielle sourcée.
- `contracts/` : schémas exécutables et règles de décision ; `scripts/` : validations et composition du dossier pré-HITL.
- `skills/hivest-portfolio-ai/` : export de la skill unique ; `templates/` : spécifications des deux profils trois pages ; `renderers/three_pager_exec/` : rendu et QA du profil exec.
- `tests/` : tests de contrat et fixtures techniques. L'export de skill dans ce dépôt n'est pas un mécanisme d'installation dans une interface.
