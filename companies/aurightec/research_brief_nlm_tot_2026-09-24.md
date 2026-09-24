# Aurightec — Prompt de cadrage Tree-of-Thought · Gemini Deep Research + NotebookLM → Codex

| Champ | Valeur |

|---|---|

| Programme | Hivest – Portfolio AI Diagnostic |

| Entité / `entity_id` | **Aurightec** / `aurightec` |

| Rang dans la séquence du dépôt | 4 / 11 |

| État dans le dépôt | INTAKE |

| Mode de recherche | **FULL** (premier cadrage complet) |

| Cutoff des preuves | 2026-09-23 |

| Version du brief | nlm-tot-0.1 — préparé le 2026-09-24 |

> Fichier **autonome** : toutes les règles communes sont répétées ici. Aucun renvoi à un autre fichier n'est nécessaire.

## 0. Mode d'emploi (5 étapes)

1. **Gemini → Deep Research** : coller le **BLOC A** entier (de « BLOC A » jusqu'à « BLOC B » exclu). Valider le plan de recherche proposé seulement s'il couvre les 8 branches B1–B8. Exporter le rapport (Google Docs).

2. **NotebookLM → nouveau notebook** « HIVEST · Aurightec ». Ajouter comme sources : (a) **ce fichier .md entier**, en source texte nommée `00_BRIEF_aurightec` ; (b) le rapport Deep Research exporté ; (c) les URL de grade A et B citées par le rapport, importées une par une (le rapport seul n'est pas une preuve primaire) ; (d) si la fonction de découverte / recherche de sources de NotebookLM est disponible dans votre version, la lancer avec la Racine R0 (section A.5) et ne garder que les sources pertinentes.

3. **Configurer le chat** (réponse personnalisée) : coller le **BLOC B**.

4. **Lancer C1 → C8** (BLOC C), un message à la fois ; enregistrer chaque réponse comme note.

5. **Studio → Carte mentale**, puis remettre à Codex : YAML `HANDOFF_CODEX` (C7 corrigé par C8) + export de la carte mentale + rapport Deep Research, avec le message **D.2**.

Point d'attention : les limites de longueur des champs de NotebookLM évoluent ; le BLOC B et les requêtes C sont volontairement courts, la méthode détaillée étant portée par la source `00_BRIEF_aurightec`.

---

## BLOC A — Prompt Deep Research (autonome, à coller tel quel)

### A.1 Rôle

Tu es un analyste senior en stratégie industrielle et en private equity, spécialiste de la création de valeur par l'IA, la data et le ML (vision, prévision, optimisation, scoring, GenAI, automatisation). Tu mènes une **recherche de cadrage profonde, sourcée et multilingue** sur **Aurightec**, participation du fonds Hivest Capital Partners, en explorant un arbre Tree-of-Thought (section A.5) selon le protocole de la section A.6. Tu privilégies les faits qui qualifient l'entreprise ; tu exposes l'incertitude sans la combler.


### A.2 Contexte du programme (commun à toutes les entités)

Programme **« Hivest – Portfolio AI Diagnostic »**. Objectif : un diagnostic homogène, sourcé et comparable de la création de valeur IA / data / ML pour les 10 participations actives de Hivest Capital Partners (page « Portefeuille » consultée le 23/09/2026) et pour Hivest elle-même. Chaque entité recevra un **trois-pages exécutif** (lisible par un C-level) adossé à un paquet de preuves versionné dans le dépôt `achard-arnaud/Hivest-ptf-analysis`, que l'agent **Codex** intègre et valide.

**Ta mission dans ce programme : la recherche de cadrage de l'entité Aurightec uniquement.** Tu produis une carte de recherche (arbre Tree-of-Thought exploré, élagué et documenté) et un registre de preuves. Tu ne produis **ni** diagnostic final, **ni** score de maturité, **ni** ROI, **ni** recommandation fournisseur. Codex partira de ton livrable comme point de départ et comme mind map de recherche.

Roster de référence (ne rechercher QUE l'entité ciblée ; les autres lignes servent à éviter les confusions) :

| Entité | Entrée Hivest (page Portefeuille) | Activité déclarée |

|---|---|---|

| VMI-Jokon | juil. 2026 | composants et systèmes techniques pour la mobilité (FR/DE) |

| Novasol Chemicals | déc. 2025 | distribution de spécialités chimiques et ingrédients |

| NV Labs | déc. 2024 | fabrication à façon de compléments alimentaires (USA) |

| Sphere | déc. 2024 | emballages ménagers durables, films, matériaux |

| Reunimer | juil. 2024 | produits de la mer, chaîne intégrée océan Indien → Europe |

| Marie-Laure PLV | déc. 2023 | PLV et agencement pour le luxe / cosmétique |

| CCE Group | mai 2023 | équipements cabine (catering) et fret aérien (ULD) |

| Agora Makers | mai 2022 | éclairage public, mobilier urbain, smart city |

| STG | nov. 2018 | transport sous température dirigée |

| Aurightec | juil. 2017 | sous-traitance électronique (EMS) et solutions connectées |

| Hivest Capital Partners | n/a (sponsor) | private equity PME/ETI, 11e entité diagnostiquée |

**Ce que la recherche doit alimenter — contrat de page `exec` v0.3** (chaque carte se termine par une ligne « À retenir » ; la recherche doit donc rapporter d'abord des faits qui *qualifient*, les inconnues seulement si elles changent la décision) :

| Page | Cartes à alimenter | Pied de page |

|---|---|---|

| 1 — Où se crée la valeur | Signalétique · Thèse (2 phrases) · Drivers hiérarchisés (≤ 5, libellés métier) · Activity breakdown (concentration, canal dominant, pouvoir de négociation, mix) · **Board's empowerment & ownership** (promoteurs et owners naturels de la transformation ; owner manquant signalé) · SWOT → **TOWS** avec posture déduite (offensive S-O, défensive S-T, veille W-T, opportuniste W-O) | Magic Quadrant — lecture activité : chaque activité classée **Core / Enabler / Support** |

| 2 — Où agir dans la chaîne de valeur | **Chaîne de Porter** : 5 activités principales + 4 de soutien ; par activité : description (un fait chiffré si possible), bénéfice attendu, impact ★ à ★★★ · 3 ordres de grandeur | Impact bottom line par zone : **commodity / parity / differentiating** |

| 3 — Quelles priorités | Magic Quadrant (centralité × différenciation) · 3 à 5 **thèmes** regroupés par workflow, chacun activité → driver → changement → **B-A-C** (Bénéfice, Avantage compétitif, Caractéristique) · Transformation **MT** (pilotage unifié par la donnée) / **LT** (modèle prédictif) · Diagnostic public IA/data/ML (faible / partiel / établi + 2-3 faits) · Stratégie dominante (résilience, coût, cash, différenciation) | Conclusion orientée TOWS |

Règle de classement Core / Enabler / Support : **Core** = transforme ou vend le produit / service ; **Enabler** = coordonne les flux ; **Support** = administre. Chaîne de Porter de référence : principales = logistique amont, opérations, logistique aval, marketing & ventes, services ; soutien = infrastructure (direction, finance, juridique), GRH, développement technologique (R&D, ingénierie, SI/data), approvisionnements. Pour un EMS, les opérations = CMS/assemblage/test ; l'amont = sourcing composants (poste de coût dominant) ; les services = réparation, obsolescence, fin de vie.

### A.3 Fiche entité — Aurightec

**Désambiguïsation :** Aurightec = groupe EMS issu du reliquat d'Eolane (sites Tallinn, Suzhou, Kulim) ; les sites français et marocains d'Eolane sont passés chez Cicor en 2025 et sont HORS périmètre.

**Identité (faits d'amorce à revérifier).** Aurightec est le nouveau nom du reliquat du groupe **Eolane** après la vente des sites français et marocains au suisse **Cicor** début 2025 (VIPress). Hivest est actionnaire majoritaire d'Eolane depuis 2017 (entrée « juil. 2017 » sur la page Portefeuille).

- Site aurightec.com : EMS « mid-volume, high-complexity » ; production à **Tallinn (Estonie), Suzhou (Chine), Kulim (Malaisie)** ; services de la conception au phase-out, box-build, réparation/refurbishment.

- Marchés : transport, énergie, industrie, médical, communications critiques (site) ; VIPress cite aussi défense, aéronautique, test semi-conducteurs.

- Certifications affichées : ISO 9001, 14001, 14064-1, IATF 16949, 45001, 13485, ISO 22163 (ferroviaire), AS 9100D.

- Direction : **Olivier Clément**, CEO (ex-président d'Eolane) selon VIPress. Siège : Paris selon VIPress.

- VIPress mentionne « smart factory » et « intégration de l'IA » dans le positionnement : **déclaration, pas preuve de déploiement**.

**Pièges de périmètre :** tout chiffre, effectif ou projet Eolane antérieur à 2025 inclut des sites désormais chez Cicor ; homonymie « Eolane » (Cicor utilise encore des références historiques).

### A.4 Règles de preuve (non négociables, communes à toutes les entités)

1. **Cutoff : 23/09/2026.** Toute information postérieure est marquée `post_cutoff` et n'écrase rien.

2. **Chaque affirmation matérielle** porte : URL canonique, éditeur, date de publication (`null` si inconnue, jamais devinée), date de consultation, localisation (page/section), extrait **verbatim ≤ 40 mots**.

3. **Statut épistémique obligatoire** : `fact` (source directe) · `inference` (base explicite citée) · `hypothesis` (test falsifiable énoncé) · `recommendation` · `unknown`.

4. **Grades de source** (classes, pas probabilités) : **A** comptes audités, registres légaux, régulateur, rapport annuel, documents techniques officiels · **B** communiqué entreprise, site officiel, communiqué Hivest, cas client/fournisseur officiel · **C** études reconnues (cabinets, Big Four, fédérations, presse spécialisée) · **D** LinkedIn public indexé, offres d'emploi, conférences, signaux sociaux · **E** inférence, source de découverte faible. Une source D génère une question ; elle n'établit jamais seule une capacité stratégique.

5. **Conversions interdites** : annonce → déploiement ; offre d'emploi → capacité acquise ; partenariat → adoption ; titre → pouvoir de décision ; benchmark sectoriel → fait entreprise ; capacité éditeur → installation chez l'entreprise ; cas client fournisseur → ROI transférable ; CA interne → croissance du marché ; panel de concurrents → « top 3 ».

6. **Inconnu = `null`, jamais zéro.** Une recherche sans résultat n'est pas une preuve d'absence : consigner la requête négative (moteur, date, formulation).

7. **Périmètre explicite** sur chaque claim : `group` / `subsidiary` / `site` / `sector` / `portfolio`. Pas d'extrapolation filiale → groupe. Pas de substitution CEO → COO, CFO → DSI, CTO produit → DSI, expert IT → DSI.

8. **Origine unique** : un même communiqué repris par N sites = une seule origine (`origin_id`).

9. **Chiffres** : une valeur canonique datée par indicateur ; en cas de divergence, exposer les deux valeurs et leurs périmètres au lieu de choisir.

10. **Interdits d'analyse** : pas de recommandation fournisseur, pas de ROI chiffré, pas de matrice BCG sans croissance de marché externe ET part de marché relative, pas de moyenne de maturité, pas de score qui compense un risque bloquant.

11. **Accès** : aucun contournement de paywall, d'authentification ou de robots. Une étude payante non lue reste un manque ; son résumé marketing n'est pas l'étude. LinkedIn : uniquement pages publiques indexées.

12. **Personnes** : uniquement rôles professionnels publics (mandataires sociaux, dirigeants, responsables fonctionnels) ; aucune donnée personnelle privée. Revalider tout rôle au cutoff.

13. **Secteur ≠ entreprise** : un pattern sectoriel (étude, pair, éditeur) devient au mieux une `hypothesis` pour l'entreprise jusqu'à preuve entreprise.

### A.5 Arbre Tree-of-Thought de Aurightec

**Racine R0 —** Après la cession des sites France/Maroc à Cicor, où Aurightec (Estonie, Chine, Malaisie) crée-t-il sa marge d'EMS moyenne série/forte complexité, et quelles couches data/IA (sourcing, industrialisation, test, qualité) peuvent la différencier ?

Les pensées ci-dessous sont des **hypothèses concurrentes à tester**, pas des faits. Chaque branche doit aussi répondre à ses champs de sortie.

**B1 — Identité, périmètre et chronologie** · alimente : `page1.signaletique ; périmètre de tous les claims`

| Pensée | Hypothèse | Test de falsification | Requêtes d'amorce |

|---|---|---|---|

| H1.1 | La date et le périmètre exact de la cession à Cicor sont documentés | Communiqués Cicor (SIX), VIPress, Electroniques.biz | `Cicor acquisition Eolane France Morocco closing 2025` |

| H1.2 | Aurightec a une holding française et trois entités opérationnelles étrangères | Registres FR, EE, MY, CN | `Aurightec SAS Pappers ; Aurightec Estonia äriregister` |

**B2 — Économie et santé financière** · alimente : `page1.signaletique, page2.ordres_de_grandeur`

| Pensée | Hypothèse | Test de falsification | Requêtes d'amorce |

|---|---|---|---|

| H2.1 | Le CA du périmètre Aurightec est publiable (comptes Estonie publics) | Äriregister (EE), comptes FR holding | `Aurightec Tallinn majandusaasta aruanne ; Eolane Tallinn revenue` |

| H2.2 | Le prix de cession Cicor et la dette résiduelle éclairent la santé financière | Communiqué Cicor (société cotée) | `Cicor Eolane purchase price revenue acquired` |

**B3 — Marché, concurrence et pouvoir de prix** · alimente : `page1.activity_breakdown, page1.tows, page3.quadrant`

| Pensée | Hypothèse | Test de falsification | Requêtes d'amorce |

|---|---|---|---|

| H3.1 | L'EMS européen est consolidé ; Aurightec est un acteur de taille modeste face à Kitron, Scanfil, Cicor, Incap | Classements EMS Europe **(sector)** | `European EMS ranking 2025 revenue Kitron Scanfil Cicor Incap` |

| H3.2 | La combinaison Europe (Estonie) + Asie (Chine, Malaisie) répond au « China+1 » et aux droits de douane | Déclarations Aurightec, presse | `Aurightec Malaysia Kulim expansion ; EMS China plus one tariffs 2026` |

**B4 — Activity breakdown et chaîne de Porter** · alimente : `page1.quadrant_bridge, page2.porter_activities, page2.quadrant_bridge`

| Pensée | Hypothèse | Test de falsification | Requêtes d'amorce |

|---|---|---|---|

| H4.1 | Les achats de composants représentent la majorité du coût et du risque (pénurie, obsolescence) | Données **sector** + mentions sourcing Aurightec | `EMS material cost share revenue ; Aurightec sourcing obsolescence` |

| H4.2 | L'industrialisation (NPI) et le test sont les activités différenciantes pour la forte complexité | Offres de service, cas clients | `Aurightec NPI industrialisation test ICT flying probe` |

**B5 — Board's empowerment & ownership** · alimente : `page1.board_empowerment ; registre COO/DSI`

| Pensée | Hypothèse | Test de falsification | Requêtes d'amorce |

|---|---|---|---|

| H5.1 | Un COO/directeur des opérations groupe coordonne les trois usines | LinkedIn public, site | `Aurightec "COO" OR "Chief Operating Officer" OR "VP Operations"` |

| H5.2 | Une DSI groupe existe (ou l'IT est gérée par site) | Offres IT, profils | `Aurightec IT manager OR CIO Tallinn Suzhou Kulim` |

| H5.g | Un responsable data / BI / IA / ML (interne ou partenaire) est identifiable | Offres « data », profils publics, prestataires nommant l'entreprise | `"Aurightec" data OR BI OR "machine learning" OR IA` |

**B6 — Socle digital, data et IA (Ishikawa 6M)** · alimente : `page3.public_ai_diagnostic ; questions 6M`

| Pensée | Hypothèse | Test de falsification | Requêtes d'amorce |

|---|---|---|---|

| H6.1 | Machines : MES/traçabilité et AOI/AXI déployés (norme pour IATF/ISO 13485) | Pages capacités, offres, références éditeurs | `Aurightec MES traceability AOI X-ray ; Eolane Tallinn MES` |

| H6.2 | Méthodes : « smart factory » annoncée → quelles briques réelles ? | Détail de la communication, cas | `Aurightec smart factory AI` |

| H6.3 | Main-d'œuvre : offres data/automatisation dans les usines | Offres EE/MY/CN | `Aurightec job data engineer OR automation engineer` |

| H6.g | La stratégie ML **observée** est publiquement établie (modèles en production, MLOps, budget, owner) | Toute preuve de production ; sinon `unknown`, pas zéro | `"Aurightec" intelligence artificielle OR "machine learning" OR IA production` |

**B7 — Drivers de valeur et signaux externes** · alimente : `page1.drivers, page3.dominant_strategy`

| Pensée | Hypothèse | Test de falsification | Requêtes d'amorce |

|---|---|---|---|

| H7.1 | Les droits de douane US/Chine et la souveraineté européenne redistribuent la demande | Presse **sector**, déclarations clients | `EMS reshoring Europe 2026 tariffs electronics` |

| H7.2 | La volatilité prix/délais composants reste un driver de BFR | Indices composants, déclarations | `electronic components lead times 2026 prices` |

**B8 — Thèmes IA candidats (état de l'art → hypothèses)** · alimente : `page3.themes (B-A-C), page3.transformation MT/LT`

| Pensée | Hypothèse | Test de falsification | Requêtes d'amorce |

|---|---|---|---|

| H8.1 | Chiffrage RFQ/BOM assisté (IA) accélère les devis sur forte complexité | Cas **sector** | `EMS quoting BOM analysis AI case study` |

| H8.2 | Analytique de test et vision (AOI) réduit faux rejets et rebuts | Cas **sector** + certifications | `AOI false call reduction deep learning EMS case` |

### A.6 Protocole d'exploration Tree-of-Thought (commun)

**Structure.** Racine R0 (question décisionnelle) → 8 branches B1–B8 → pensées concurrentes H (hypothèses, section A.5) → sous-questions de niveau 3 si la pensée survit à l'évaluation.

**Boucle par pensée :**

1. **Générer** 2 à 3 requêtes par pensée, multilingues si pertinent ; chaque requête porte son hypothèse falsifiable.

2. **Évaluer** : `score = V × P ÷ C` (chaque facteur de 1 à 3). V = utilité pour formuler une ligne « À retenir » ; P = probabilité d'une source publique de grade A à C ; C = coût (accès, langue, homonymie).

3. **Faisceau (beam)** : ne développer que les **3 meilleures pensées par branche** ; niveau 3 seulement si `score ≥ 3`.

4. **Étendre** : lire la source → fragment verbatim → claim typé → statut de la pensée `confirmed` / `refuted` / `dead_end` / `open`.

5. **Élaguer** : **deux résultats négatifs** sur une pensée → `dead_end` → formuler une **question d'entretien** avec owner cible.

6. **Retour arrière** : toute découverte qui change le périmètre (cession, acquisition, homonyme, changement de dirigeant) renvoie à B1 et invalide les descendants concernés.

7. **Pensées émergentes** : au plus 2 nouvelles pensées par branche si une source les impose ; les justifier.

8. **Arrêt** : budget global de **40 requêtes** (≤ 6 par branche), OU toutes les lignes « À retenir » formulables sans inventer, OU toutes les pensées closes.

**Ishikawa 6M** (appliqué à B6, et à toute carte qui ne peut pas formuler son « À retenir ») : **Méthodes** (process, S&OP, qualité) · **Machines** (ERP, MES, WMS, TMS, PLM, CRM, data platform, cloud, OT/IoT, vision) · **Main-d'œuvre** (owners, équipes data/BI/ML/IA, recrutements) · **Matière** (données, référentiels, catalogues, labels) · **Milieu** (intégration post-acquisitions, réglementation, géographie) · **Mesure** (KPI suivis : OTIF, rendement, stocks, BFR, qualité).

### A.7 Sources à sonder (ordre de priorité)

**Communes :** site officiel et filiales (aurightec.com) · communiqués Hivest (hivestcapital.com) et conseils de l'opération (avocats, banques d'affaires) · registres légaux et comptes (Pappers, Infogreffe, societe.com, BODACC pour la France ; registres équivalents à l'étranger) · rapports annuels / RSE · presse économique et spécialisée (CFNEWS, Les Échos, L'Usine Nouvelle, presse sectorielle) · fédérations professionnelles et régulateurs · offres d'emploi (site carrières, APEC, Welcome to the Jungle, Indeed, LinkedIn Jobs public) · LinkedIn public indexé (page société, profils dirigeants) · références intégrateurs / éditeurs (preuve de système installé uniquement si l'entreprise est nommée) · études sectorielles (Bain, BCG, McKinsey, Deloitte, PwC, EY, KPMG, Accenture, Capgemini, fédérations) pour l'état de l'art IA — **au niveau `sector` uniquement**.

**Spécifiques à Aurightec :**

- aurightec.com ; VIPress et Electroniques.biz (changement de nom, 2025) ; communiqués Cicor (société cotée SIX) sur la reprise d'Eolane France/Maroc.

- Registres : Pappers (holding FR), e-Business Register (Estonie), SSM (Malaisie).

- Pairs candidats à vérifier : Cicor, Kitron, Scanfil, Incap, Hanza, Katek, Lacroix Electronics.

**Langues de recherche :** EN, FR, ET (Estonie), ZH (Chine), MS (Malaisie).

### A.8 Livrable attendu (rapport de cadrage, en français)

Structure imposée, citations inline `[S-NLM-xxx]` renvoyant au registre final :

0. **Synthèse de cadrage** (≤ 10 lignes) : ce qu'on sait qui *qualifie* l'entreprise ; les **3 inconnues qui inverseraient le diagnostic**.

1. **Journal ToT** : tableau `pensée | requêtes lancées | V/P/C | score | statut | claims | question d'entretien`.

2. **B1 Identité, périmètre et chronologie** — 3. **B2 Économie** — 4. **B3 Marché et concurrence** — 5. **B4 Activity breakdown et chaîne de Porter** — 6. **B5 Board's empowerment & ownership** — 7. **B6 Socle digital / data / IA (6M)** — 8. **B7 Drivers de valeur** — 9. **B8 Thèmes IA candidats** : pour chaque branche, tableau `claim_id | énoncé | statut | périmètre | source | extrait`.

10. **Amorce du trois-pages** (tout est `candidat`) : thèse, drivers hiérarchisés, TOWS + posture, 9 activités de Porter avec ★ candidates, pré-classement du quadrant, 3 à 5 thèmes B-A-C, MT/LT, niveau public IA/data/ML.

11. **Questions ouvertes** : `id | question | branche 6M | affecte | owner cible | déclencheur | budget | condition d'arrêt`.

12. **Couverture négative** : requêtes sans résultat, sources bloquées ou payantes.

13. **Registre des sources** : `S-NLM-xxx | URL | titre | éditeur | date publication | date consultation | grade | périmètre | nature (intégral / extrait / synthèse) | accès`.

Ne pas conclure au-delà des preuves. Ne pas remplir un champ pour « faire complet ».

---

## BLOC B — Instructions de chat NotebookLM (« Configurer le chat » → personnalisé)

> Coller tel quel. Autonome. Longueur volontairement courte pour tenir dans le champ d'instructions.

```text

Rôle : analyste de recherche du programme « Hivest – Portfolio AI Diagnostic », entité Aurightec (entity_id aurightec), cutoff 23/09/2026.

Tu réponds UNIQUEMENT à partir des sources du notebook. La source « 00_BRIEF_aurightec » fixe la méthode (arbre Tree-of-Thought B1–B8, Ishikawa 6M, contrat de page exec v0.3, format HANDOFF_CODEX) ; toutes les autres sources sont des preuves.

Règles : citer chaque affirmation ; statut fact / inference (base citée) / hypothesis (test falsifiable) / recommendation / unknown ; périmètre group / subsidiary / site / sector / portfolio ; inconnu = null, jamais 0 ; secteur ≠ entreprise ; annonce ≠ déploiement ; offre d'emploi ≠ capacité ; titre ≠ pouvoir ; capacité éditeur ≠ installation ; pas de ROI chiffré, pas de fournisseur recommandé, pas de BCG sans croissance de marché externe et part relative ; divergences de chiffres exposées, jamais arbitrées en silence.

Désambiguïsation : Aurightec = groupe EMS issu du reliquat d'Eolane (sites Tallinn, Suzhou, Kulim) ; les sites français et marocains d'Eolane sont passés chez Cicor en 2025 et sont HORS périmètre.

Style : français, dense, tableaux, IDs préfixés NLM (S-NLM, F-NLM, C-NLM, Q-NLM), zéro remplissage. Signale explicitement toute incertitude et toute source manquante.

```

---

## BLOC C — Séquence de requêtes NotebookLM (une par message, dans l'ordre)

> Chaque requête est autonome (nom d'entité et règles clés répétés). Enregistrer chaque réponse comme **note** du notebook avant de passer à la suivante.

**C1 — Périmètre et chronologie (B1)**

```text

Aurightec (aurightec) — Applique la branche B1 du brief 00_BRIEF_aurightec. Résous l'entité : raison sociale, holding, filiales, sites, pays, acquisitions et cessions avec date d'annonce ET date de closing distinctes. Liste les pièges de périmètre et homonymes rencontrés. Tableau claim_id | énoncé | statut | périmètre | source | extrait ≤ 40 mots. Termine par les pensées H1.x : confirmed / refuted / dead_end / open.

```

**C2 — Économie, marché et concurrence (B2, B3)**

```text

Aurightec (aurightec) — Applique B2 et B3 du brief 00_BRIEF_aurightec. Donne CA, EBITDA, effectifs, BFR, capex, dette par année et périmètre, divergences exposées. Puis segments (produit / canal / pays), 4P, cinq forces de Porter par segment, pairs nationaux et internationaux avec leur actionnariat. Aucune matrice BCG si croissance de marché externe et part relative absentes. Statut et source sur chaque ligne.

```

**C3 — Activity breakdown et chaîne de Porter (B4)**

```text

Aurightec (aurightec) — Applique B4 du brief 00_BRIEF_aurightec. Construis l'activity breakdown (concentration clients, canal dominant, mix, pouvoir de négociation) puis la chaîne de Porter : 5 activités principales + 4 de soutien. Pour chacune : description avec un fait chiffré sourcé si possible, bénéfice attendu (hypothèse), impact ★ à ★★★ candidat, classement Core / Enabler / Support et commodity / parity / differentiating avec justification. Marque tout ce qui n'est pas sourcé comme hypothesis.

```

**C4 — Board's empowerment & ownership (B5)**

```text

Aurightec (aurightec) — Applique B5 du brief 00_BRIEF_aurightec. Produis le registre dirigeants : lignes obligatoires COO et DSI (même inconnues), plus mandataires légaux, CEO/DG, CFO, responsable data/BI/IA, responsables supply chain / industriel. Colonnes : rôle demandé | personne ou null | titre exact | périmètre groupe/filiale/pays | début de mandat | source | date de vérification | statut de preuve | promoter_signal (strong/medium/weak/none/unknown) | ownership_scope | prochain test. Ne substitue jamais un rôle à un autre. Signale l'owner manquant de la transformation.

```

**C5 — Socle digital, data et IA en Ishikawa 6M (B6)**

```text

Aurightec (aurightec) — Applique B6 du brief 00_BRIEF_aurightec avec l'Ishikawa 6M (Méthodes, Machines, Main-d'œuvre, Matière, Milieu, Mesure). Pour chaque M : ce qui est établi, l'hypothèse testée, la source, le statut. Sépare la stratégie ML OBSERVÉE (preuves publiques) de la stratégie ML PROPOSÉE (hypothèses : prévision, optimisation, vision, scoring, GenAI, avec baseline sans ML). Conclus sur un niveau public IA/data/ML candidat : faible / partiel / établi, avec 2-3 faits.

```

**C6 — Drivers, thèmes et TOWS (B7, B8)**

```text

Aurightec (aurightec) — Applique B7 et B8 du brief 00_BRIEF_aurightec. Matrice drivers : signal externe sourcé → exposition entreprise (fact ou hypothesis) → mécanisme économique → stratégie de valeur (COST_REDUCTION, COST_AVOIDANCE, CAPITAL_PRODUCTIVITY, DIFFERENTIATION_GROWTH, RISK_RESILIENCE, BLUE_OCEAN) → KPI/baseline → contre-preuve. Puis 3 à 5 thèmes IA candidats regroupés par workflow au format B-A-C, une transformation MT et LT, un SWOT puis TOWS avec posture candidate. Tout état de l'art sectoriel reste au périmètre sector.

```

**C7 — Évaluation ToT finale et HANDOFF_CODEX**

```text

Aurightec (aurightec) — Applique la section BLOC D du brief 00_BRIEF_aurightec. Réévalue chaque pensée H (V×P÷C, statut final), élague, liste les questions d'entretien. Puis produis UN SEUL bloc YAML « HANDOFF_CODEX » strictement conforme au schéma du brief, suivi d'un bloc Mermaid « mindmap » de l'arbre exploré (racine R0, branches B1–B8, pensées avec statut). Aucune information absente des sources.

```

**C8 — Red-team du notebook (contrôle avant remise à Codex)**

```text

Aurightec (aurightec) — Red-team des notes C1–C7 selon le brief 00_BRIEF_aurightec : liste les claims sans fragment verbatim, les conversions interdites (annonce→déploiement, offre→capacité, titre→pouvoir, secteur→entreprise, éditeur→installation), les extrapolations filiale→groupe, les chiffres divergents non signalés, les homonymes suspects et les sources post-cutoff. Verdict : SURVIVES_RED_TEAM / SURVIVES_WITH_NARROWING / REOPEN_TARGETED, avec corrections à appliquer au YAML.

```

Puis : **Studio → Carte mentale** (mind map native NotebookLM) sur l'ensemble du notebook ; exporter l'image et la joindre à Codex avec le YAML.

---

## BLOC D — Contrat de handoff vers Codex

### D.1 Schéma `HANDOFF_CODEX` (YAML, à produire tel quel)

```yaml

handoff_version: nlm-tot-0.1

entity_id: aurightec

entity_name: "Aurightec"

cutoff: 2026-09-23

mode: FULL            # FULL = premier cadrage ; DELTA = compléter un dossier existant

generated_with: [gemini_deep_research, notebooklm]

generated_at: null          # date réelle de production

sources:                    # IDs réservés S-NLM-### (ne jamais réutiliser un ID du dépôt)

  - id: S-NLM-001

    url: ""

    title: ""

    publisher: ""

    published_at: null      # YYYY-MM-DD ou null

    accessed_at: ""

    grade: B                # A | B | C | D | E

    scope: group            # group | subsidiary | site | sector | portfolio

    capture_kind: excerpt   # full | excerpt | summary

    access: open            # open | paywall | blocked

    origin_id: null         # même communiqué repris = même origin_id

fragments:

  - id: F-NLM-001

    source_id: S-NLM-001

    locator: ""             # page, section, paragraphe

    excerpt: ""             # verbatim ≤ 40 mots

claims:

  - id: C-NLM-001

    text: ""

    status: fact            # fact | inference | hypothesis | recommendation | unknown

    scope: group

    fragment_refs: [F-NLM-001]

    basis: null             # obligatoire si inference

    falsification_test: null  # obligatoire si hypothesis

    contradicts: []

    post_cutoff: false

    decision_relevance: []  # ex. [page1.signaletique, page2.porter.operations, page3.themes]

leadership:                 # lignes COO et DSI obligatoires, même null

  - role_requested: COO     # COO | DSI | CEO | CFO | LEGAL_OFFICER | DATA_AI_LEAD | SUPPLY_CHAIN | INDUSTRIAL | OTHER

    person: null

    exact_title: null

    scope: group

    mandate_start: null

    source_id: null

    verified_at: null

    evidence_status: unknown_after_bounded_search

    promoter_signal: unknown  # strong | medium | weak | none | unknown

    ownership_scope: null

    next_test: ""

tot:

  root: "Après la cession des sites France/Maroc à Cicor, où Aurightec (Estonie, Chine, Malaisie) crée-t-il sa marge d'EMS moyenne série/forte complexité, et quelles couches data/IA (sourcing, industrialisation, test, qualité) peuvent la différencier ?"

  branches:

    - id: B1

      name: "Identité, périmètre et chronologie"

      thoughts:

        - id: H1.1

          hypothesis: ""

          falsification_test: ""

          queries_run: []

          score: {V: null, P: null, C: null, total: null}

          status: open      # confirmed | refuted | dead_end | open

          claim_refs: []

          interview_question: null

exec_seed:                  # tout est candidat, rien n'est gelé

  page1:

    signaletique: {}

    thesis_candidate: ""

    drivers_candidates: []  # ≤ 5, libellés métier, hiérarchisés

    activity_breakdown: ""

    board_empowerment: ""

    tows: {s: [], w: [], o: [], t: [], posture_candidate: null}  # offensive | defensive | veille | opportuniste

  page2:

    porter_activities:      # 5 primary + 4 support

      - name: ""

        porter_type: primary  # primary | support

        description: ""

        benefit_hypothesis: ""

        impact_stars_candidate: null  # 1 | 2 | 3

        claim_refs: []

  page3:

    quadrant_seed:

      - activity: ""

        centrality: null      # core | enabler | support

        differentiation: null # commodity | parity | differentiating

        rationale: ""

    themes_candidates:        # 3 à 5, regroupés par workflow

      - workflow: ""

        driver: ""

        change: ""

        benefit: ""

        competitive_advantage: ""

        characteristic: ""

        value_strategy: null  # COST_REDUCTION | COST_AVOIDANCE | CAPITAL_PRODUCTIVITY | DIFFERENTIATION_GROWTH | RISK_RESILIENCE | BLUE_OCEAN

        status: hypothesis

    transformation: {mt: "", lt: ""}

    public_ai_diagnostic: {level_candidate: null, facts: []}  # faible | partiel | établi

    dominant_strategy_candidate: null

questions:

  - id: Q-NLM-001

    question: ""

    branch_6m: null          # methodes | machines | main_oeuvre | matiere | milieu | mesure | null

    affects: []              # ex. [drivers, usecases, page3]

    owner_target: ""

    trigger: ""

    budget_queries: 3

    stop_condition: ""

    status: open

coverage:

  negative_searches: []      # {query, engine, date, result}

  blocked_sources: []

red_team:

  verdict: null              # SURVIVES_RED_TEAM | SURVIVES_WITH_NARROWING | REOPEN_TARGETED

  corrections: []

mindmap_mermaid: |

  mindmap

    root((R0))

```

### D.2 Message de remise à Codex (coller avec le YAML et l'export de mind map)

```text

Contexte : dépôt achard-arnaud/Hivest-ptf-analysis. Entité Aurightec (entity_id aurightec), cutoff 23/09/2026, mode FULL.

Pièces jointes : HANDOFF_CODEX.yaml (cadrage Gemini Deep Research + NotebookLM, IDs réservés S-NLM / F-NLM / C-NLM / Q-NLM), rapport Deep Research, mind map NotebookLM.

1. Lis AGENTS.md, program/state.json, companies/aurightec/manifest.json. Ne relis pas le handoff programme entier.

2. Traite le YAML comme un PAQUET DE TRAVAIL du rôle research, pas comme des preuves validées : aucune capture originale n'est archivée. Ne promeus aucun claim en fact dans le package sans capture de la source (URL, date, hash) hors dépôt, conformément à references/evidence.md et market-drivers.md.

3. Intègre la carte : crée ou complète companies/aurightec/research_graph.json (nœuds question avec branch_6m, owner, trigger, budget_queries, stop_condition) et companies/aurightec/INDEX.md ; reporte les lignes COO/DSI dans program/leadership_register.json avec promoter_signal et ownership_scope.

4. Déduplique origines et entités, résous les contradictions, conserve les divergences de chiffres. Tout ce qui vient du périmètre sector alimente wiki/ comme hypothèse, jamais la vérité entreprise.

5. Priorise les recherches de capture par valeur décisionnelle pour le contrat exec v0.3 (lignes « À retenir »), lance scripts/validate_bundle.py et les tests ; l'état reste RESEARCH tant que les gates de capture et HITL ne sont pas levés.

6. Rends : delta proposé (fichiers touchés), questions encore ouvertes, et décisions à soumettre à François. Aucun rendu trois-pages.

```

---

## Annexe — Traçabilité de ce brief

Brief préparé le 2026-09-24 à partir de : dépôt `achard-arnaud/Hivest-ptf-analysis` (commit `3ebd6a8` : AGENTS.md, skill `hivest-portfolio-ai`, `program/roster.json`, `program/leadership_register.*`, `companies/aurightec/manifest.json`), handoff programme v0.1 du 23/09/2026, loopback trois-pages SPHERE v1 → v2 (contrat exec v0.3, protocole Ishikawa × ToT), et une vérification web ciblée du 2026-09-24. Les « faits d'amorce » de la section A.3 sont des **pistes à revérifier**, pas des preuves validées.

Sources consultées pour l'amorce :

- https://hivestcapital.com/portefeuille/

- https://vipress.net/aurightec-un-nouveau-nom-de-la-sous-traitance-bati-sur-ce-quil-reste-du-groupe-eolane/

- https://www.aurightec.com/ 