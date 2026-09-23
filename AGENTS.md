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
| Market context, drivers | references/market-drivers.md | signaux externes → exposition → drivers → stratégies de valeur |
| Value chain, 7S, maturity | references/diagnostic.md | diagnostic + inconnues |
| Opportunities, 9-box | references/opportunities.md | inventaire + shortlist |
| Red-team, HITL | references/review.md | dossier pré-HITL |
| Storytelling, rendu | references/composition.md | contenu gelé puis trois pages |
| Loopback, rollup | references/learning.md | delta proposé + lineage |

Limiter le contexte courant : une entreprise, une étape, un résumé wiki et les claims décisifs avec leurs contre-preuves. Top-k initial 12, élargir si une contradiction ou un claim critique est omis. Sauvegarder un checkpoint avant changement d'étape.

## États
PROGRAM_DESIGN_READY → PILOTS → PILOT_LOOPBACK → CLUSTERS → HIVEST → PORTFOLIO_REVIEW → DONE.
Entreprise : INTAKE → RESEARCH → MARKET_CONTEXT → ANALYSIS → OPPORTUNITIES → RED_TEAM → HITL_PENDING → GO_DRAFT → FROZEN → RENDERED → DONE.
Les décisions HITL sont GO_DRAFT, RESEARCH_TARGETED, NARROW_SCOPE, PIVOT. Ne jamais auto-attribuer une approbation utilisateur. L'autorisation de préparer le programme ne vaut pas validation de ses conclusions.
Ne lancer les clusters qu'après les deux pilotes et leur loopback. Une entreprise DONE satisfait toutes les conditions de `contracts/decision-rules.md`.

L'étape MARKET_CONTEXT utilise `references/market-drivers.md` et produit `market_context` et `drivers` au contrat v0.2. OPPORTUNITIES et RED_TEAM relisent ces sorties. Le contexte externe et le classement des drivers industriels sont obligatoires ; la facilité de déploiement ne détermine pas la priorité business. Un dossier prose n'est pas un `package_ref` validé ; Sphere reste en RESEARCH tant que les originaux ne sont pas archivés.


## Reprise v0.2
Lire `companies/<id>/INDEX.md` et `research_graph.json`. Charger la procédure `research-graph.md` pour segmentation/Porter/4P, COO/DSI, équipes data/IA/ML et loopback. Valider `package.json` ET `strategic_context.json` via `scripts/validate_bundle.py`. Le Markdown est une projection ; les tests legacy seuls ne suffisent plus.
