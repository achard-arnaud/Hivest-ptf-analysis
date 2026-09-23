# Portfolio router — v0.1.0

Profil François-Pro. Finalité business et création de valeur ; aucune logique de product matching.
Lire `program/state.json` puis UN manifest entreprise. Charger uniquement la procédure de l'étape depuis `skills/hivest-portfolio-ai/references/`. Ne pas relire le handoff entier ni énumérer le corpus pendant un run.

## Invariants
- Source → fragment → claim → analyse → décision → contenu gelé. Conserver IDs, dates, contradictions et inconnues.
- Une absence de preuve vaut `null / unknown`, jamais zéro. Ne pas calculer une moyenne globale de maturité.
- Un pattern sectoriel n'est pas un fait entreprise ; un poste ouvert n'est pas une capacité acquise ; une annonce n'est pas un déploiement.
- Évaluer les hard gates avant toute priorité. Garder NO-ACTION et la solution sans IA.
- Les runs temporaires ne sont jamais stockés dans le code. Utiliser un répertoire externe au dépôt. Ne promouvoir que des connaissances contrôlées, fixtures et décisions canoniques.
- Ne pas écrire de recommandations fournisseur. Distinguer technical, product et business ; business est la dimension principale.
- Orchestrateur : distribuer les étapes, vérifier états/handoffs ; la recherche appartient au rôle research. Un rôle n'impose pas un nouvel agent.

## Routage
| Étape | Ressource | Sortie / gate |
|---|---|---|
| Intake, research, sector wiki | references/evidence.md | paquet evidence + couverture |
| Value chain, 7S, maturity | references/diagnostic.md | diagnostic + inconnues |
| Opportunities, 9-box | references/opportunities.md | inventaire + shortlist |
| Red-team, HITL | references/review.md | dossier pré-HITL |
| Storytelling, rendu | references/composition.md | contenu gelé puis trois pages |
| Loopback, rollup | references/learning.md | delta proposé + lineage |

Limiter le contexte courant : une entreprise, une étape, un résumé wiki et les claims décisifs avec leurs contre-preuves. Top-k initial 12, élargir si une contradiction ou un claim critique est omis. Sauvegarder un checkpoint avant changement d'étape.

## États
PROGRAM_DESIGN_READY → PILOTS → PILOT_LOOPBACK → CLUSTERS → HIVEST → PORTFOLIO_REVIEW → DONE.
Entreprise : INTAKE → RESEARCH → ANALYSIS → RED_TEAM → HITL_PENDING → GO_DRAFT → FROZEN → RENDERED → DONE.
Les décisions HITL sont GO_DRAFT, RESEARCH_TARGETED, NARROW_SCOPE, PIVOT. Ne jamais auto-attribuer une approbation utilisateur. L'autorisation de préparer le programme ne vaut pas validation de ses conclusions.
Ne lancer les clusters qu'après les deux pilotes et leur loopback. Une entreprise DONE satisfait toutes les conditions de `contracts/decision-rules.md`.
