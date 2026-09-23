# Marché → drivers industriels → stratégie IA

Étape obligatoire avant la shortlist, y compris lors d'une reprise. Ne pas commencer par les technologies disponibles.

## Collecte externe et scraping ciblé
1. Définir segments produits/usages, acheteurs, géographies et période. Séparer marché adressable, marché adjacent et fournisseurs amont. Ne jamais assimiler le marché mondial des plastiques au marché de l'entreprise.
2. Consulter sites entreprise/filiales, comptes, associations professionnelles et études sectorielles, sources réglementaires officielles, au moins deux pairs pertinents et preuves techniques. Une étude payante inaccessible reste un manque ; son résumé marketing ne devient pas une étude lue.
3. Collecter les pages et PDF publics nécessaires avec outils web ou extraction autorisée. Respecter restrictions d'accès, robots et conditions ; aucun contournement. Conserver URL canonique, titre, éditeur, date de publication (null si inconnue), date de collecte, périmètre, statut d'accès, page/section. Distinguer scrape intégral, extrait et synthèse. Ne pas prétendre archiver un original à partir d'un snippet.
4. Stocker captures acquises immuables hors code avec hash et URI durable ; extraire fragments identifiés, puis claims. Dédupliquer URL/hash et réutiliser la wiki par secteur/process ; créer une nouvelle version plutôt qu'écraser une preuve. Les synthèses seules sont des artefacts dérivés, pas du raw.
5. Vérifier les dates avant cutoff, séparer faits, discours commercial, prévisions et hypothèses. Toute source critique a une limite de transférabilité. Rafraîchir prix/demande à chaque diagnostic, réglementation avant freeze ; pages techniques stables réutilisables avec contrôle de validité.

## Artefacts à produire
- Registre des sources/extractions et couverture : demande/prix, concurrence/substitution, matières/énergie, productivité/qualité/capacité, réglementation, clients/montée en gamme. Chaque manque a impact décisionnel et recherche suivante.
- Note sectorielle wiki versionnée : segmentation, économie, concurrents comparables, contraintes, patterns techniques et contre-preuves ; séparer couche sectorielle et exposition entreprise.
- Matrice drivers : ID, signal externe sourcé, exposition entreprise sourcée ou hypothèse, mécanisme économique, priorité business argumentée, KPI/baseline, contre-preuve, owner à confirmer et condition qui inverse le rang.
- Mapping driver → stratégie de valeur → use case → page. Chaque opportunité retenue a un driver ; les travaux data sont des prérequis sauf mécanisme IA démontré.

## Prioriser et choisir la stratégie
Classer coût/marge, qualité, disponibilité/capacité, taille/intégration, BFR/service, différenciation/montée en gamme et conformité selon exposition, matérialité et urgence. Évaluer faisabilité séparément ; un assistant facile n'est pas une priorité économique. Pas de score chiffré sans baseline. Hard gates avant scoring.
- COST_REDUCTION (cost killing) : dépense existante effectivement supprimable ; identifier ligne P&L, coût de réalisation et risque qualité.
- COST_AVOIDANCE : dépense future évitée contre scénario explicite ; ne pas additionner avec réduction du même coût.
- CAPITAL_PRODUCTIVITY : cash/BFR ou capex différé ; cash libéré ≠ EBITDA récurrent.
- DIFFERENTIATION_GROWTH : performance, service, mix ou marge incrémentale avec volonté de payer à tester.
- RISK_RESILIENCE : pertes probabilisées évitées, accès marché, continuité ; pas de revenu inventé.
- BLUE_OCEAN : hypothèse de nouvelle demande/non-client et proposition de valeur nouvelle, avec test client et contre-preuve concurrentielle. Une offre durable, un chatbot ou un cross-sell ne suffisent pas.
Comparer à règle métier/SPC/optimisation classique/process sans IA et NO-ACTION. Séparer stratégie de valeur et sourcing BUILD/BUY/PARTNER/OUTSOURCE/NO-ACTION. Aucun fournisseur recommandé.

## Gates et projection trois pages
Avant HITL, red-team doit vérifier la chaîne complète et les transferts secteur→entreprise, ainsi que les doubles comptes. Sans contexte exploitable : RESEARCH_TARGETED ou manque explicitement accepté, jamais maturité zéro.
P1 : 2–3 signaux externes, position concurrentielle et drivers dominants. P2 : drivers attachés aux étapes/process et KPI. P3 : priorité business distincte du séquençage, stratégie de valeur, sourcing, baseline et test d'arrêt. Conserver exactement trois pages ; condenser ailleurs, pas de quatrième page ni police réduite. Aucun rendu final avant GO_DRAFT.

Un gain annoncé par un fournisseur ou un pair ne devient ni baseline ni ROI de l’entreprise : benchmark non transféré jusqu’à validation locale.
