# Hivest — Note stratégique IA : gap register et décisions de preuve

**Cutoff :** 25 septembre 2026  
**Objet :** enregistrer les gaps qui doivent être fermés, bornés ou explicitement laissés ouverts avant la V2.  
**Important :** ce fichier ne modifie aucun gate du diagnostic Hivest dans `manifest.json`.

| ID | Priorité | Claim / besoin | État au 25/09 | Décision pour la V2 |
|---|---|---|---|---|
| GAP-01 | P0 | « La maturité IA crée déjà une décote à l'exit » | **Non démontré directement.** BCG 2026 documente une décote liée à une maturité **digitale** insuffisante : 40 % des investisseurs interrogés disent avoir vu une décote ≥5 %. | Écrire « maturité digitale / fondations data-tech » ; toute extension à l'IA reste une inférence explicitement qualifiée. |
| GAP-02 | P0 | « X % des fonds sont dans l'impossibilité de vendre » | Formulation incorrecte / population mal définie. McKinsey 2026 estime 16 000 sociétés buyout-backed détenues >4 ans, soit 52 % de l'inventaire 2025 ; holding global moyen 6,6 ans. | Parler de **backlog d'actifs et allongement des détentions**, pas de proportion de fonds incapables de vendre. |
| GAP-03 | P0 | Placement des 10 participations dans un quadrant time-to-exit × maturité / capacité | Les dossiers sont hétérogènes. Les dates d'entrée sont disponibles mais le niveau canonique de maturité n'est pas uniformément résumé dans Hivest. | Claude doit lire seulement les artefacts canoniques de chaque société et conserver `unknown` si le dossier ne supporte pas un placement. Aucun score moyen inventé. |
| GAP-04 | P0 | TOWS Hivest / portefeuille | Le document V1 juxtapose des drivers ; il ne construit pas un vrai SWOT→TOWS. | Construire SWOT factuel puis TOWS ; chaque option doit pointer vers une preuve ou être qualifiée comme hypothèse. |
| GAP-05 | P1 | « Forward deployment : modèle Palantir devenu mainstream » | L'origine Palantir n'est pas nécessaire à la thèse et doit être sourcée si conservée. En revanche, Hg, Vista/Google Cloud, OpenAI et Anthropic montrent une diffusion forte du modèle embedded/FDE en 2025–2026. | Retirer l'étymologie non essentielle ; démontrer la diffusion récente avec les pairs sourcés. |
| GAP-06 | P1 | Économie d'une activité de services / Academy | KKR publie des revenus et charges attribuables à Capstone ; AI Partners publie son modèle Academy/Organization/Factory. Aucun de ces cas n'est directement transposable à Hivest. | Garder en **dézoom / option**. Ne pas présenter la différence frais-charges Capstone comme une marge économique transposable. |
| GAP-07 | P1 | Market KPI « 5,5 Md$ levés par les sociétés de déploiement OpenAI + Anthropic » | Le V1 agrège des montants provenant de communications distinctes. La comparabilité des tours, investisseurs et structures doit être vérifiée. | Remplacer par un KPI plus robuste ou citer séparément chaque opération ; ne pas conserver l'agrégat sans recapture. |
| GAP-08 | P1 | France Invest : 76 % confidentialité comme frein principal | Claim présent dans le corpus existant, source officielle PDF. Le crawler web de cette passe rencontre un 403 direct sur le PDF. | Conserver seulement après recapture du PDF officiel ou réutilisation de l'archive déjà vérifiée ; sinon écrire qualitativement « confidentialité parmi les principaux freins ». |
| GAP-09 | P1 | Bpifrance/Siparex : 80 % des cas déployables <6 mois / 70 % 15–100 k€ | Le landing officiel confirme le livre blanc, 20 cas et une base de >600 entreprises accompagnées ; les pourcentages exigent lecture du livre blanc source. | Ne pas afficher les pourcentages si Claude ne retrouve pas le fragment primaire. |
| GAP-10 | P1 | Accelex / Canoe comme solutions directes de DD GP | Périmètre trompeur. Carta positionne Accelex sur LP Portfolio Analytics ; Canoe cible surtout allocataires, asset servicers et wealth managers. | Les utiliser comme **patterns de document/data operations** et non comme preuve d'un produit Hivest-ready pour la due diligence GP. |
| GAP-11 | P1 | Corporatings comme solution de due diligence private-company | Lens couvre surtout des données publiées / sociétés cotées et des états financiers normalisés. | Utiliser comme pattern de normalisation, screening et traçabilité ; ne pas le présenter comme couverture complète du non coté. |
| GAP-12 | P1 | DilBloom performances chiffrées | Le site publie x10, 95 %, 80 % etc. Ce sont des **claims vendeur**, sans validation indépendante trouvée. | Décrire capacités / architecture / traçabilité ; exclure les performances du business case sauf attribution explicite. |
| GAP-13 | P1 | Sinequa « élimine virtuellement les hallucinations » | Claim vendeur non démontré. | Exclure la promesse de performance ; conserver RAG, accès aux sources, connecteurs et traitement documentaire comme patterns. |
| GAP-14 | P1 | Second Brain / Investment Digital Twin comme état Hivest | Il s'agit d'une **hypothèse de design**, pas d'une capacité observée. | Écrire au conditionnel / comme architecture cible et séparer strictement de l'état courant. |
| GAP-15 | P1 | Souveraineté = on-prem / open source | Aucun besoin Hivest documenté n'impose une solution unique. | Produire une matrice de décision : data class, privilege, latency, cost, reversibility, model portability ; aucune recommandation blanket. |
| GAP-16 | P1 | Roadmap 3–5 ans | Trop d'inconnues internes pour une séquence datée fiable. | Remplacer par quadrant / règles de priorisation et stop conditions. |
| GAP-17 | P2 | Candidat : « je sais le faire à l'échelle » | L'expérience François est pertinente, mais ce n'est pas une preuve publique Hivest. | Encadré RETEX personnel : responsabilités exactes, résultats autorisés et transférabilité ; pas d'auto-affirmation non étayée. |
| GAP-18 | P2 | 8 piliers de maturité dans la note C-Level | Trop détaillés pour le fil principal. | Garder les 8 dimensions en backend ; synthèse executive en 4 systèmes de valeur si cela accélère la lecture. |

## Gates de sortie de la recherche pour la V2

La rédaction peut avancer si :
1. GAP-01 et GAP-02 sont corrigés dans la formulation ;
2. GAP-03 conserve explicitement les `unknown` et ne force aucun placement ;
3. toute statistique matérielle a un fragment primaire ou une attribution claire ;
4. les claims fournisseurs restent des claims fournisseurs ;
5. le ghost paper est validé logiquement avant la densification graphique.

Le présent gap register n'autorise ni changement du `manifest.json`, ni passage de Hivest à un gate de diagnostic ultérieur.
