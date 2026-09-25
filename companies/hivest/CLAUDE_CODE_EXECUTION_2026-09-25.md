# Claude Code — Hivest strategic note V2 execution contract

**Target agent :** Claude Code  
**Owner :** François-Pro  
**Date :** 25 septembre 2026  
**Mission :** reprendre la note stratégique Hivest et produire une V2 C-Level 5–7 pages, sourcée, rendue et QA, sans modifier les gates du programme de diagnostic.

<success_criteria>
1. La note commence par la thèse business : la transformation est déjà le métier du LBO actif ; l'IA en est une nouvelle capacité.
2. Le Centre d'Excellence est expliqué avant le Forward Deployment.
3. Les deux mandats sont explicitement distincts : transformation des participations / modernisation du processus d'investissement.
4. Le papier traite Data, ML, optimisation, vision, GenAI, agentique et robotique selon le cas ; jamais « IA = LLM ».
5. La V2 remplace les drivers descriptifs par un SWOT factuel puis une TOWS décisionnelle.
6. L'exit readiness est sourcé sans transformer « digital maturity haircut » en « AI haircut ».
7. La trajectoire datée 0–60 mois est remplacée par des règles / quadrants fondés sur time-to-exit, payback, magnitude et maturity.
8. L'Invest 2.0 introduit un Second Brain / Investment Digital Twin comme architecture cible, pas comme état actuel.
9. Le rendu reste visuellement proche du PDF V1 : drift maximal ~15–20 %, palette et typographies conservées autant que possible.
10. Le PDF final fait 5–7 pages, toutes lisibles à taille normale, sans réduction opportuniste des fontes.
</success_criteria>

<start_here>
Avant toute édition :
1. `git status --short`
2. lire `AGENTS.md`
3. lire `program/state.json`
4. lire `companies/hivest/manifest.json`
5. lire `companies/hivest/INDEX.md`
6. lire ensuite uniquement les fichiers listés dans cet INDEX pour ce workstream.
Ne change pas `program/state.json` ni `companies/hivest/manifest.json` : ce travail de note stratégique ne ferme aucun gate du diagnostic.
</start_here>

<inputs>
Substance :
- `companies/hivest/NOTE_STRATEGIQUE_2026-09.md` — mémoire stratégique/evidence-aware existante ;
- `companies/hivest/reference/NOTE_STRATEGIQUE_REFERENCE_V1.md` — source Markdown du PDF de référence ;
- `companies/hivest/STRATEGIC_NOTE_FEEDBACK_2026-09-25.md` — contrat éditorial validé ;
- `companies/hivest/STRATEGIC_NOTE_GAPS_2026-09-25.md` — gaps, stop conditions et interdits ;
- `companies/hivest/SOURCE_SUMMARIES_2026-09-25.md` — résumés canoniques et limites de preuve ;
- `Best of Greenfield - S1 2026.pdf` seulement s'il est disponible localement hors dépôt ; sinon utiliser les extraits/claims déjà promus et ne rien inventer.

Styles / rendu :
- `renderers/strategic_note/theme.css` — style de la note V1 ;
- `renderers/strategic_note/build.py` — renderer A4 / Mermaid / QA ;
- `renderers/strategic_note/README.md` ;
- `renderers/strategic_note/sample_note.md` ;
- `templates/strategic-market-note.md` — contrat narratif générique ;
- `renderers/three_pager_exec/exec_theme.css` et `templates/THREE_PAGER_EXEC_v0.3.md` — vocabulaire visuel / exec secondaire, à consulter pour cohérence sans forcer leur structure trois pages.
</inputs>

<evidence_rules>
- Source → fragment → claim → analyse → texte.
- Distingue fact / attributed / inference / hypothesis / recommendation / unknown dans tes notes de travail ; la page C-Level porte la nuance dans les verbes et les sources.
- Ne transforme pas une source fournisseur en preuve indépendante.
- Ne transforme pas une statistique de panel en fait Hivest.
- Ne transforme pas « digital maturity valuation haircut » en « AI maturity discount ».
- Ne transforme pas 52 % d'inventaire buyout-backed >4 ans en 52 % des fonds incapables de vendre.
- Accelex/Canoe = patterns LP/allocator/data operations, pas validation d'une solution de DD GP.
- Second Brain / Digital Twin = architecture candidate.
- Toute donnée portfolio non supportée reste `unknown`.
- Aucune recommandation fournisseur implicite.
</evidence_rules>

<working_method>
Travaille en passes courtes et persistantes. Utilise Git comme état, mais ne crée pas de gros commits intermédiaires inutiles.

PASS 1 — INVESTIGATE
- Ouvre tous les fichiers explicitement référencés avant d'en parler.
- Compare V1, note stratégique longue, feedback et gaps.
- Pour une source web critique manquante, privilégie la source primaire ; ajoute seulement le résumé canonique et sa limite au fichier de sources, jamais le raw scraping dans le dépôt.
- Ne relance pas une recherche large si le gap est déjà fermé.

PASS 2 — PORTFOLIO ROLLUP CIBLÉ
Seulement pour le quadrant portefeuille :
- parcours chaque `companies/<id>/INDEX.md` puis le strict minimum canonique permettant d'obtenir :
  - date d'entrée Hivest ;
  - bottom line / transformation MT-LT ;
  - diagnostic public Data / ML / IA ;
  - stratégie dominante ;
  - niveau de preuve / inconnues.
- Ne charge pas tout le corpus.
- Ne crée pas de score global de maturité.
- Si l'information est insuffisante : `unknown` et absence du quadrant ou symbole dédié.

PASS 3 — GHOST PAPER
Crée hors dépôt, par exemple `/tmp/hivest-note-v2/ghost.md`, un squelette qui contient uniquement :
- action title de chaque section ;
- claim principal ;
- 2–4 preuves maximum ;
- figure/table nécessaire ;
- objection / contre-test ;
- transition vers la section suivante.
Vérifie que chaque bloc sert la thèse. Supprime les redondances.

Architecture préférée :
1. WHY — transformation historique du LBO actif ;
2. leçons Digital → SaaS/Cloud → Data → ML → IA/agentique → robotique ;
3. TOWS : ce que le contexte signifie pour Hivest ;
4. HOW — CoE : enablement/L&D + forward deployment + transformation ;
5. WHAT #1 — portefeuille : land, prove, scale, transfer, reuse ;
6. **rupture narrative** ;
7. WHAT #2 — Investissement augmenté : dealflow → DD → IC → hold → exit ;
8. Second Brain / Investment Digital Twin + souveraineté ;
9. priorisation par quadrants / time-to-exit ;
10. un rôle, deux mandats, puis trois questions de discussion.

Ne force pas dix sections si 6–8 titres d'action racontent mieux l'histoire.

PASS 4 — WRITE
Produit `companies/hivest/NOTE_STRATEGIQUE_2026-09_v2.md`.
- 5–7 pages après rendu, pas 5–7 pages avant compression.
- Ton : C-Level, concret, direct, respectueux, sans posture professorale.
- Réduis les phrases de balancement et les abstractions.
- Utilise des tableaux seulement lorsqu'ils accélèrent la décision.
- L'« En bref » et les KPI sont écrits **en dernier**, après reranking des messages.
- Toute mention de François est un RETEX personnel précis et transférable, pas une auto-évaluation vague.

PASS 5 — FIGURES
Conserve Mermaid comme source canonique. Figures prioritaires :
A. vagues technologiques + couche Target Operating Model / valeur ;
B. operating contract CoE ↔ FDE ↔ participations ↔ DSI, en swimlanes ou flux rôle/action ;
C. Investment Digital Twin / Second Brain en couches ;
D. quadrant de priorisation time-to-exit × maturity/execution capacity, avec payback/magnitude en annotation.

Si Mermaid produit un résultat trop dense, préfère un tableau / quadrant HTML-CSS simple. Pas d'infographie décorative.

PASS 6 — STYLE
Le PDF V1 est la référence visuelle.
- Réutilise `renderers/strategic_note/theme.css`.
- Drift graphique max 15–20 %.
- Palette : navy / blue / teal / gold.
- Titres : Source Serif 4 ; corps : Inter / fallbacks existants.
- Réutilise `tldr`, `kpis`, `callout`, `callout-gold`, `story`, `cols`.
- Ajoute du CSS uniquement pour : quadrant, swimlanes, stack digital twin ou bandeau de rupture si le renderer actuel ne suffit pas.
- Toute nouvelle classe réutilise les variables CSS existantes.
- Ne réduis jamais la taille des polices pour résoudre un débordement : coupe ou réécris.

PASS 7 — RENDER & QA
- installe seulement les dépendances nécessaires déjà documentées ;
- rends avec `renderers/strategic_note/build.py` ;
- vise `--pages 5-7`;
- conserve le output de travail hors dépôt, par exemple `/tmp/hivest-note-v2/`;
- lis `qa_report.json` ;
- inspecte visuellement chaque page du PDF (rasterise temporairement si nécessaire) ;
- vérifie : hiérarchie, blancs, tableaux, coupures, sources, figures, densité, taille réelle de lecture ;
- corrige le contenu avant le CSS quand le problème est la densité.
</working_method>

<content_decisions_already_made>
- Split strict : portefeuille / fonds. Ne pas écrire « deux chantiers se renforcent » comme idée centrale.
- Le CoE précède le Forward Deployment dans la narration.
- Le CoE : 3 casquettes = Enablement/L&D, Forward Deployment, Transformation.
- Le make/buy/partner appartient aux participations ; le CoE informe et facilite.
- Le modèle est de plus en plus une commodité ; mémoire, process, doctrine, règles et preuves sont les actifs à capitaliser.
- Pas de rétroplanning fake 3–5 ans : quadrants et stop conditions.
- Le rôle est une fonction transversale avec deux mandats, pas « Head of Forward Deployment ».
- Les 8 dimensions restent analytiques ; la note peut les compresser en 4 systèmes C-Level.
</content_decisions_already_made>

<deliverables>
Obligatoires :
1. `companies/hivest/NOTE_STRATEGIQUE_2026-09_v2.md`
2. modifications minimales de `renderers/strategic_note/theme.css` et/ou `build.py` si réellement nécessaires
3. `/tmp/hivest-note-v2/Hivest_note_strategique_IA_forward_v2.pdf`
4. `/tmp/hivest-note-v2/qa_report.json`
5. un bref compte rendu final :
   - fichiers modifiés ;
   - sources ajoutées / claims abandonnés ;
   - pages produites ;
   - QA passée / échecs résiduels ;
   - trois points restant à arbitrer humainement.

Ne modifie pas les gates, le manifest ou le programme state. Ne commit/push que si le diff final est cohérent et si l'utilisateur te l'a demandé dans la session Claude Code ; sinon laisse le diff prêt à relire.
</deliverables>

<final_check>
Avant de t'arrêter, relis le ghost paper puis la V2 et vérifie :
- chaque titre peut être compris sans son paragraphe ;
- chaque chiffre matériel possède une source adéquate ;
- aucune phrase ne confond attribution et fait ;
- aucun vendor n'est présenté comme recommandation implicite ;
- les deux mandats restent distincts ;
- l'output ressemble encore clairement au PDF V1 ;
- la conclusion ouvre une discussion d'associés, elle ne dicte pas une décision.
</final_check>
