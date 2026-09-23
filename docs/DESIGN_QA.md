# Design QA — 23 septembre 2026

Statut : PROGRAM_DESIGN_READY pour pilotes, périmètre limité au socle documentaire et contrôles de preuve. Aucun diagnostic ni rendu approuvé.

## Revue contradictoire indépendante
Une revue, une réparation, une vérification. Cinq constats :
1. Score entreprise alimenté par une inférence sectorielle : base transitive contrôlée.
2. Gates arbitraires et fondés sur hypothèses : ensemble canonique de cinq gates, pass sur fait entreprise.
3. Références orphelines dans RunContext : contrôle ajouté.
4. Renderer sans données complètes : projections use_cases et sources gelées, comparées au paquet.
5. Confusion validation contenu / DONE : validate_content accepte uniquement FROZEN ; les gates de fin restent une revue séparée.

La vérification indépendante a confirmé les corrections 2–5 et identifié un résiduel ciblé de 1 : recrutement entreprise + étude sectorielle passaient via deux contrôles indépendants. Réouverture ciblée, correction par contrôle conjoint sur chaque claim de score, ajout d'une fixture dédiée. Cette dernière correction a été vérifiée par test déterministe, sans prétendre à une nouvelle approbation indépendante.

## Résultat déterministe
33 tests unitaires/schema/NRT exécutés localement et réussis. Validation formelle du skill réussie. Les fixtures sont synthétiques ; leur contenu n'est jamais une donnée Hivest.

## Limites du verdict
Les contrôles testent des invariants et références, pas la vérité sémantique d'une citation. Une source réelle peut être mal interprétée ; l'indépendance d'origin_id et l'authenticité de GO_DRAFT exigent revue. Les snapshots distants ne sont pas téléchargés par le validateur. Le template reste candidat et les transitions RENDERED/DONE restent manuelles jusqu'à l'épreuve des pilotes.

## Gates ouverts
- Recherche et diagnostics Sphere/STG.
- Validation humaine des conclusions de chacun.
- Trois pages PDF, QA visuelle et reader/decision réelle.
- Loopback inter-pilotes et promotion explicite du template.
- Seulement ensuite production par clusters et consolidation portefeuille.
