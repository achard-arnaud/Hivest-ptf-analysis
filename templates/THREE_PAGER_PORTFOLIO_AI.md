# THREE_PAGER_PORTFOLIO_AI — 0.1.0 candidate

Audience : investment team / operating partner. Dimension principale : business.
Entrée : payload validé contre `contracts/three-pager.schema.json` + RunContext GO_DRAFT, claims et sources accessibles. Rendu interdit avant freeze. Les titres doivent être conclusifs, les propositions porter claim_refs et statut épistémique.
Le payload embarque la projection complète `use_cases` des 6–10 IDs retenus et `sources` correspondant à source_ids. Le validateur compare ces projections au paquet validé avant de geler. Le renderer lit ce payload autonome ; le paquet recherche reste réservé à la QA de lineage.

## Page 1 — Où se joue la création de valeur ?
Signalétique : activité, siège, géographies, ownership/date Hivest, employés, CA, EBITDA, sites, marchés, acquisitions. Chaque chiffre : unité, période, périmètre, source ; sinon « non établi publiquement ».
Thèse business/croissance, contexte financier, risques/marge/capex ; 7S avec preuves ou grille de couverture ; SWOT dérivée (2 points max/case) ; huit dimensions de maturité et bottlenecks. Une phrase dominante, jamais huit scores sans interprétation.

## Page 2 — Sur quels processus intervenir ?
Chaîne réelle et supports ; chaque activité a création de valeur, coût/friction, contrôle/handoff, capacité VRIO éventuelle, digitalisation observable, opportunité IA et contrainte. Les cases « non établi » sont acceptables ; ne pas remplir pour symétrie.
Maximum cinq colonnes horizontales ; chaîner sur deux lignes si nécessaire. Les opportunités hypothétiques ont un marquage distinct des déploiements observés. Les flèches remplacent les répétitions textuelles.

## Page 3 — Quelles décisions prendre et valider ?
3×3 Strategic Centrality × Differentiation (jamais BCG) avec 5–9 capacités lisibles ; shortlist de 6–10 opportunités, identifiants reliés à l'inventaire complet. Inclure manufacturing/operations, engineering, revenue et corporate selon applicabilité documentée ; aucune obligation d'inventer un cas par verticale.
Colonnes : workflow/valeur, horizon/famille, sourcing, gate/inconnue décisive. Thèse equity story et prochaine validation explicites. Si moins de six opportunités défendables, garder le dossier en NARROW_SCOPE plutôt que fabriquer.

## Rendu et QA à exécuter aux pilotes
A4 paysage, 297×210 mm, marges 10 mm ; corps ≥9 pt, sources ≥8 pt, interligne ≥1.1. Fond blanc, texte ardoise, accent bleu profond, inconnues ambre ; palette candidate sans prétention à une charte déjà approuvée.
Exactement trois pages. Vérifier nombre de pages, absence de clipping/overflow, césures, lisibilité des sources, contraste, légendes, toutes les rubriques et les liens. Export PDF + HTML + PNG de contrôle hors code. Inspection visuelle des trois PNG obligatoire.
Pas de radar si données 7S incomplètes ; jamais interpoler, zéroter ni fermer les trous. Pas de métrique créée par le renderer. Si overflow : condenser le contenu avec son auteur et renouveler hash/HITL si matériel, jamais diminuer la police sous le minimum.
Statut promotion : après deux pilotes contrastés, QA visuelle et décision humaine. La présente livraison ne prétend pas avoir validé un PDF.

## Contrat de contexte externe (v0.2)
P1 : signaux marché sourcés, concurrents comparables, trois drivers hiérarchisés. P2 : driver_id et KPI reliés aux processus. P3 : chaque cas relie driver, stratégie de valeur, alternative sans IA, sourcing et condition de validation ; distinguer priorité business et ordre de déploiement. BLUE_OCEAN exige nouvelle demande à tester. Ne pas ajouter une quatrième page.

## Contrat v0.2 — business, leadership et ML
P1 inclut COO/DSI (ou inconnu,périmètre,date),équipe data/IA/ML et stratégie ML observée séparée de la proposition ; segmentation CA datée et pricing power,Porter/4P condensés. P2 comprend pricing/indexation et order-to-cash. P3 relie driver,méthode ML/vision/optimisation/GenAI,baseline,stratégie de valeur,sourcing et gate. BCG non calculable sans croissance marché/part relative.
Le futur freeze v0.2 exigera hash global et inconnues acceptées dans le GO_DRAFT humain. Le contrat contenu reste0.1 : le gel v0.2 est actuellement refusé, même si le bundle de recherche est valide.
