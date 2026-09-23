# Hivest Capital Partners — AI Portfolio Maturity Diagnostic
## Handoff / Operating Brief pour ChatGPT Work

**Version :** 0.1 — 23 septembre 2026  
**Owner :** François-Pro  
**Statut :** cadrage de reprise / bootstrap Work  
**Objet :** construire un diagnostic homogène, sourcé et comparable de maturité IA pour l’ensemble des participations actives de Hivest Capital Partners, puis pour Hivest elle-même.

---

# 1. Executive brief

L’objectif n’est pas de produire dix monographies indépendantes. Il faut construire **un système de diagnostic cumulatif**, capable de :

1. comprendre le business et la création de valeur de chaque participation ;
2. reconstruire sa chaîne de valeur et ses capacités internes ;
3. qualifier sa maturité IA dans toute sa largeur ;
4. identifier les opportunités IA réellement prioritaires ;
5. distinguer **quick wins**, **use cases structurants** et **transformations long terme** ;
6. rendre les résultats comparables au niveau portefeuille ;
7. capitaliser les recherches sectorielles d’une société à l’autre au lieu de les refaire ;
8. produire pour chaque entité un **3-pager exécutif commun**, adossé à un corpus de preuves plus profond ;
9. consolider ensuite les résultats au niveau Hivest afin de faire émerger des thèses de création de valeur transverses au portefeuille.

Le programme couvre les **10 participations actives actuellement publiées par Hivest** ainsi que **Hivest Capital Partners elle-même**, soit **11 entités** à diagnostiquer.

La logique cible doit réutiliser les principes de :

- `achard-arnaud/ai-maturity-diagnostic` pour l’acquisition, la preuve, les claims, le diagnostic et les use cases ;
- `achard-arnaud/skills-notes-and-storytelling` pour la composition, le claims graph light, le scaffold, le red-team, le loopback/dreaming et la production de notes exécutives ;
- le paradigme **Karpathy LLM Wiki** pour transformer les sources brutes en connaissance persistante et cumulative plutôt que relire tout le corpus à chaque run ;
- les patterns `nice-output-engine` / `two-pager` / futures variantes `three-pager` pour séparer strictement **analyse métier** et **mise en forme finale**.

**Principe d’architecture :**

```text
RAW SOURCES (immutables)
        ↓
EVIDENCE LEDGER
        ↓
ATOMIC FRAGMENTS / CLAIMS
        ↓
WIKI / KNOWLEDGE PAGES
        ↓
BUSINESS + VALUE CHAIN + AI MATURITY ANALYSIS
        ↓
USE CASE INVENTORY + PRIORITISATION
        ↓
RED TEAM / GAP SEARCH
        ↓
HITL
        ↓
FROZEN CONTENT CONTRACT
        ↓
3-PAGER RENDERING
        ↓
PORTFOLIO ROLLUP + LOOPBACK
```

---

# 2. Récapitulatif de la conversation Hivest

## 2.1 Hivest Capital Partners

Hivest Capital Partners est un fonds français de private equity orienté PME/ETI et amélioration opérationnelle / croissance. Dans ce programme, Hivest est considéré à la fois :

- comme **sponsor potentiel d’une démarche portefeuille** ;
- comme **11e entité à diagnostiquer** : processus d’investissement, due diligence, portfolio monitoring, value creation, sourcing, reporting, knowledge management, deal teams, operating partners, etc.

## 2.2 Portefeuille actif de départ

À la date du 23 septembre 2026, le portefeuille public Hivest indique les lignes actives suivantes :

| Entité | Entrée Hivest | Cluster de travail initial | Nature dominante |
|---|---:|---|---|
| VMI-Jokon | juil. 2026 | Industrie / mobilité | composants et systèmes techniques |
| Novasol Chemicals | déc. 2025 | Chimie / distribution spécialisée | distribution, expertise technique, international |
| NV Labs | déc. 2024 | Life sciences / manufacturing | nutraceutiques / contract manufacturing |
| Sphere | déc. 2024 | Industrie / packaging | manufacturing multi-sites |
| Reunimer | juil. 2024 | Agro / supply chain | produits de la mer, chaîne intégrée |
| Marie-Laure PLV | déc. 2023 | Industrie / retail / luxe | PLV, agencement, production multi-matériaux |
| CCE Group | mai 2023 | Aéronautique | équipements cabine et fret |
| Agora Makers | mai 2022 | Industrie / infrastructure urbaine | éclairage, mobilier urbain |
| STG | nov. 2018 | Logistique / agro | logistique température dirigée |
| Aurightec | juil. 2017 | Electronique / ingénierie | électronique et solutions connectées |
| **Hivest Capital Partners** | n/a | Private Equity | investissement et value creation |

**Important :** le « poids dans le portefeuille » ne doit pas être inventé.  
La collecte recherchera, lorsqu’ils sont publics :

- ticket d’investissement ;
- valorisation / enterprise value ;
- part détenue ;
- chiffre d’affaires / EBITDA ;
- taille du groupe ;
- importance dans la stratégie du fonds.

À défaut, le champ reste `unknown`. On peut calculer séparément un **score de priorité de recherche**, mais il ne doit jamais être présenté comme un poids économique du portefeuille.

## 2.3 Personnes déjà identifiées

Deux interlocuteurs Hivest ont été identifiés dans le fil :

- **Alexandre Levavasseur — Director**, ancien FCDE et Accuracy ;
- **Germain Le Gallic — Associate**, ancien PwC Transaction Services et Alandia Industries.

Le rôle courant doit être revalidé au moment d’utiliser un profil LinkedIn ou une information de personne.

---

# 3. Objectif final du programme

Produire une vision homogène de la création de valeur IA potentielle sur l’ensemble du portefeuille Hivest.

Le résultat doit répondre, pour chaque société, à cinq questions :

1. **Où l’entreprise gagne-t-elle ou perd-elle de la valeur aujourd’hui ?**
2. **Quelles capacités sont réellement différenciantes, critiques, standardisables ou externalisables ?**
3. **Quel est le niveau observable de maturité IA, data, automation et digital ?**
4. **Où l’IA peut-elle créer de la valeur à court, moyen et long terme ?**
5. **Quelles opportunités méritent une expérimentation, un investissement structurel, un partenariat ou aucune action ?**

Le portefeuille devra ensuite permettre de répondre à :

- quels use cases sont transverses à plusieurs participations ?
- quelles capacités peuvent être mutualisées ?
- quelles sociétés justifient une transformation dédiée ?
- où Hivest peut-il créer une **playbook factory** de value creation IA ?
- quels assets communs seraient économiquement pertinents : expertise, gouvernance, vendor framework, AI factory, data/vision capabilities, procurement, benchmark, knowledge base, operating model, talent ?

---

# 4. Périmètre IA — définition large et industrielle

Le diagnostic ne doit pas être réduit à la GenAI de bureau.

## 4.1 Quatre couches à observer

### A. Operations / Manufacturing

- computer vision ;
- inspection qualité ;
- maintenance prédictive ;
- optimisation de rendement / scrap / OEE ;
- ordonnancement ;
- supply chain ;
- prévision de demande ;
- contrôle process ;
- energy optimisation ;
- robotics / cobotics ;
- anomaly detection ;
- simulation / digital twins ;
- optimisation de flux ;
- industrial copilots.

### B. Tech / Engineering / Product

- software engineering ;
- AI coding ;
- test generation ;
- embedded AI ;
- product engineering ;
- simulation ;
- R&D ;
- knowledge engineering ;
- technical documentation ;
- requirements engineering ;
- PLM / CAD augmentation ;
- agentic engineering workflows.

### C. Client / Distribution / Revenue

- sales enablement ;
- pricing ;
- demand intelligence ;
- forecasting ;
- configuration / CPQ ;
- customer service ;
- marketing ;
- tendering ;
- personalization ;
- account intelligence ;
- product recommendation ;
- distribution optimisation.

### D. Workspace / Corporate — couche transverse

- finance ;
- controlling ;
- procurement ;
- legal ;
- HR ;
- learning ;
- compliance ;
- knowledge management ;
- enterprise search ;
- document intelligence ;
- reporting ;
- agents / copilots ;
- workflow automation.

La restitution stratégique pourra conserver les **trois grandes verticales de valeur** demandées :

1. Operations / Manufacturing ;
2. Tech / Engineering ;
3. Client / Distribution ;

avec **Workspace / Corporate, Data, Platform, Governance et Cyber** comme couches horizontales.

---

# 5. Architecture analytique : ne pas mélanger les frameworks

Le brief initial contient plusieurs frameworks utiles, mais ils n’ont pas le même objet. Le Work doit les employer au bon étage.

---

## 5.1 Niveau 1 — comprendre le business et ses capacités

### Porter — chaîne de valeur

Objectif : localiser :

- activités créatrices de marge ;
- coûts structurants ;
- handoffs ;
- goulots ;
- dépendances ;
- contrôles ;
- points de friction ;
- actifs et savoir-faire critiques.

Ne pas forcer les catégories textbook si la chaîne réelle de l’entreprise est mieux décrite par une chaîne opérationnelle adaptée.

### VRIO

Objectif : qualifier les ressources/capacités qui peuvent soutenir un avantage durable :

- Valuable ;
- Rare ;
- Inimitable ;
- Organised.

VRIO doit être appliqué à des **capacités concrètes** et non à des slogans : réseau industriel, IP, données, distribution, savoir-faire process, expertise réglementaire, engineering, accès client, certification, etc.

### McKinsey 7S

Objectif : mesurer la **cohérence organisationnelle / readiness de transformation**, et non une « intensité IA » brute.

Axes :

- Strategy ;
- Structure ;
- Systems ;
- Shared Values ;
- Skills ;
- Staff ;
- Style.

Le radar de page 1 sera donc nommé :

> **Organizational readiness / 7S coherence radar**

et non « radar d’intensité IA ».

### SWOT

SWOT est une **synthèse dérivée**, produite après la recherche.

Elle ne doit pas piloter la collecte initiale.

---

# 6. Niveau 2 — contexte stratégique / portefeuille

## 6.1 GE–McKinsey 9-box

GE–McKinsey croise traditionnellement attractivité et compétitivité.

Dans ce programme, elle peut être utilisée lorsque l’entreprise possède plusieurs BU, marchés ou familles d’activité suffisamment documentées.

Elle ne doit pas être utilisée comme mesure de maturité IA.

## 6.2 BCG

La matrice BCG est une **2×2**, et non une 9-box.

Elle peut servir uniquement si :

- croissance de marché ;
- part de marché relative ;

sont raisonnablement établies.

Sinon : ne pas produire une BCG artificielle.

## 6.3 ADL

ADL peut être utile pour :

- maturité du secteur ;
- position concurrentielle ;
- trajectoire / cycle de vie.

Même règle : ne l’utiliser que si les données justifient le niveau de précision.

### Règle

**GE / BCG / ADL sont des lenses contextuelles facultatives.**

Le 3-pager ne doit pas devenir un catalogue de frameworks.  
Le Work choisit le framework qui explique le mieux le problème observé.

---

# 7. Niveau 3 — diagnostic de maturité IA

Construire un **AI Maturity Model propre au programme Hivest** en réutilisant la philosophie d’`ai-maturity-diagnostic`.

Le modèle doit mesurer des capacités observables et conserver `fact | inference | hypothesis | unknown`.

## Dimensions proposées

1. **AI strategy & value**
   - cas d’usage reliés aux priorités business ;
   - sponsorship ;
   - business cases ;
   - allocation de capital ;
   - mesure de valeur.

2. **Operating model & governance**
   - ownership ;
   - decision rights ;
   - central/federated model ;
   - governance ;
   - risk / controls ;
   - portfolio management.

3. **Data & knowledge**
   - disponibilité ;
   - qualité ;
   - accès ;
   - architecture ;
   - données industrielles ;
   - connaissance documentaire ;
   - lineage / governance.

4. **Technology & platform**
   - cloud / infra ;
   - APIs ;
   - integration ;
   - MLOps / LLMOps ;
   - edge ;
   - vision ;
   - IoT / OT integration ;
   - agentic stack.

5. **Delivery & industrialisation**
   - experiments ;
   - production ;
   - reuse ;
   - monitoring ;
   - deployment ;
   - lifecycle ;
   - standardisation.

6. **People, skills & adoption**
   - AI literacy ;
   - engineering capabilities ;
   - business ownership ;
   - change ;
   - usage ;
   - training ;
   - supervision.

7. **Security, risk & compliance**
   - cyber ;
   - privacy ;
   - IP ;
   - model risk ;
   - regulated environment ;
   - third-party risk ;
   - OT constraints.

8. **AI breadth / domain penetration**
   - workspace ;
   - engineering ;
   - manufacturing ;
   - client/revenue ;
   - multimodal/vision ;
   - automation.

### Scoring

Ne pas produire de chiffre précis à partir de signaux faibles.

Préférer pour chaque dimension :

- `0 — non établi`
- `1 — isolated / exploratory`
- `2 — repeatable`
- `3 — managed / production`
- `4 — scaled / strategic`

Chaque score doit porter :

```yaml
score:
confidence:
evidence_refs:
counter_evidence:
unknowns:
```

Le score global ne doit pas être une moyenne mécanique.  
La synthèse doit décrire :

- le **niveau le plus élevé réellement prouvé** ;
- les dimensions qui limitent le passage à l’échelle ;
- les contradictions.

---

# 8. Niveau 4 — matrice stratégique 3×3 des activités / capacités

Le brief initial mélange BCG, Core/Critical et sourcing. La version opératoire doit devenir une **Strategic Centrality × Differentiation 9-box**.

## Axe X — Centralité stratégique

1. **Support**
2. **Enabler / Adjacent**
3. **Core business**

## Axe Y — Potentiel de différenciation

1. **Commodity**
2. **Competitive parity**
3. **Differentiating**

Résultat :

| | Support | Enabler | Core |
|---|---|---|---|
| **Differentiating** | rationaliser / valoriser | co-développer / investir | **build & own / strategic investment** |
| **Parity** | buy / standardise | partner / configure | invest selectively / acquire capability |
| **Commodity** | **outsource / SaaS / automate** | standardise / partner | protect control points, simplify execution |

Cette matrice est une **adaptation interne du programme**, pas une BCG.

Pour chaque activité ou capability, ajouter :

- position dans la 9-box ;
- justification ;
- rôle de l’IA ;
- posture `BUILD | BUY | PARTNER | OUTSOURCE | NO-ACTION` ;
- dépendances ;
- degré de réversibilité.

---

# 9. Niveau 5 — diagnostic des use cases IA

Chaque use case doit être décrit indépendamment de toute offre fournisseur.

## 9.1 Trois familles

### Quick wins

Caractéristiques :

- valeur compréhensible ;
- dépendances limitées ;
- faible niveau d’intégration ;
- réversible ;
- délai court ;
- adoption maîtrisable.

### Structural use cases

Caractéristiques :

- changement de workflow ;
- intégration système/data ;
- propriétaire métier clair ;
- valeur récurrente ;
- industrialisation nécessaire.

### Transformation bets

Caractéristiques :

- impact sur operating model, produit, réseau ou modèle économique ;
- changements de rôles ou decision rights ;
- nouveaux actifs ;
- réarchitecture possible ;
- horizon plus long.

## 9.2 Score de priorité use case

Ne pas classer uniquement par « potentiel IA ».

Évaluer :

| Dimension | Question |
|---|---|
| Economic value | impact coût, marge, revenu, capital, cash |
| Strategic value | renforce-t-il un avantage ou une capability critique ? |
| Feasibility | données, intégrations, process, talent |
| Time-to-value | vitesse d’obtention d’une preuve |
| Repeatability | répétition / volume du workflow |
| Adoption | friction humaine / changement |
| Risk | sécurité, réglementaire, OT, réputation |
| Reusability | pattern réutilisable dans le portefeuille |

Les dimensions peuvent être notées, mais :

- blockers et hard gates restent hors score ;
- un risque critique n’est jamais compensé par un bon total ;
- le classement doit exposer l’incertitude.

---

# 10. Blue Ocean / ERIC

La grille :

- Eliminate ;
- Reduce ;
- Raise ;
- Create ;

est conservée pour les **transformation bets** et les opportunités de redesign stratégique.

Ne pas appliquer ERIC mécaniquement à tous les quick wins.

L’usage prioritaire est :

- remodeler une proposition de valeur ;
- supprimer des étapes historiques ;
- créer un nouveau niveau de service ;
- transformer un business model ;
- redessiner une chaîne de valeur.

---

# 11. Contrat du 3-pager

Le 3-pager est la **surface exécutive**, pas la totalité du diagnostic.

Chaque 3-pager doit être généré à partir d’un package fonctionnel plus riche.

---

## PAGE 1 — Company context + AI maturity

### Bandeau signalétique

- activité ;
- siège / géographies ;
- ownership ;
- date d’entrée Hivest ;
- employés ;
- CA ;
- EBITDA si public ;
- sites / usines ;
- principaux marchés ;
- acquisitions récentes.

### Investment / business thesis

- moteur de croissance ;
- problème business principal ;
- transformation en cours ;
- risques ;
- enjeux de marge / capex / internationalisation / consolidation.

### Santé financière

Privilégier :

- CA et croissance ;
- EBITDA / marge lorsque disponible ;
- capex ;
- dette si publiquement documentée ;
- M&A ;
- signaux de santé / tension.

Si non public : `not publicly established`.

### Diagnostic organisationnel

- mini radar 7S ;
- 2–3 forces ;
- 2–3 fragilités.

### SWOT compact

4 quadrants, maximum 2–3 points chacun.

### AI maturity snapshot

- maturité globale descriptive ;
- dimensions les plus avancées ;
- bottlenecks ;
- preuves observées.

---

## PAGE 2 — Value chain & AI opportunity map

Construire une chaîne de valeur **adaptée à l’entreprise**.

### Structure

```text
SUPPLIERS / INPUTS
      →
INBOUND / SOURCING
      →
ENGINEERING / PRODUCT
      →
OPERATIONS / MANUFACTURING
      →
QUALITY / LOGISTICS
      →
SALES / DISTRIBUTION
      →
SERVICE / CUSTOMER
```

Support :

```text
DATA · IT/OT · PROCUREMENT · FINANCE · HR · LEGAL/COMPLIANCE · GOVERNANCE
```

### Pour chaque bloc

Afficher :

- création de valeur ;
- coûts / frictions ;
- capacités VRIO éventuelles ;
- niveau de digitalisation visible ;
- opportunités IA ;
- contraintes.

Les flèches / cartes visuelles doivent remplacer du texte, pas l’ajouter.

---

## PAGE 3 — AI Strategic Snapshot

### 1. Strategic Centrality × Differentiation 9-box

Positionner les activités / capabilities clés.

### 2. Priority use cases

Présenter 6–10 opportunités maximum :

- Operations / Manufacturing ;
- Tech / Engineering ;
- Client / Distribution ;
- quelques transverses Workspace si réellement matérielles.

### 3. Horizon

- **0–6 mois — Quick wins**
- **6–18 mois — Structural**
- **18–36 mois — Transformation bets**

### 4. Build / Buy / Partner / Outsource

Indiquer la posture probable, pas un fournisseur.

### 5. Executive thesis

Terminer par une phrase de synthèse :

> Where AI can materially change the equity story.

et :

> What should be validated next.

---

# 12. Le package de recherche sous-jacent

Pour ne pas compresser l’incertitude dans trois pages, chaque entreprise doit conserver un dossier structuré.

```text
companies/<company>/
├── manifest.yaml
├── raw/
│   ├── corporate/
│   ├── financial/
│   ├── people/
│   ├── jobs/
│   ├── tech/
│   ├── operations/
│   ├── sector/
│   └── social/
├── evidence/
│   ├── source_ledger.yaml
│   ├── fragments.yaml
│   ├── claims.yaml
│   ├── contradictions.yaml
│   └── unknowns.yaml
├── analysis/
│   ├── company_profile.md
│   ├── financial_context.md
│   ├── porter_value_chain.md
│   ├── vrio.md
│   ├── seven_s.md
│   ├── ai_maturity.yaml
│   ├── activity_9box.yaml
│   ├── use_cases.yaml
│   ├── blue_ocean.md
│   └── red_team.md
├── content/
│   └── three_pager_content.yaml
└── output/
    ├── three_pager.md
    ├── three_pager.html
    └── three_pager.pdf
```

**Règle déjà établie à conserver : les runs temporaires ne sont jamais stockés dans le code.**  
Les dossiers de run / debug / scratch restent en dehors des sources canoniques.

---

# 13. Architecture LLM-Wiki / mémoire cumulative

Le principal risque du programme est de refaire les mêmes recherches sur :

- computer vision industrielle ;
- maintenance ;
- supply chain ;
- manufacturing ;
- aéronautique ;
- packaging ;
- nutraceutique ;
- chimie ;
- logistics AI ;
- industrial copilots.

Il faut donc séparer **source**, **connaissance sectorielle** et **vérité entreprise**.

## 13.1 Raw

`raw/` contient les sources immuables :

- rapports ;
- pages web ;
- communiqués ;
- études ;
- transcripts ;
- notes ;
- LinkedIn / public profiles ;
- jobs ;
- vendor case studies ;
- research papers.

Ne jamais réécrire une source brute.

## 13.2 Wiki

`wiki/` contient des synthèses persistantes maintenues par l’agent.

Exemple :

```text
wiki/
├── portfolio/
│   ├── hivest.md
│   └── cross_portfolio_patterns.md
├── sectors/
│   ├── industrial-ai.md
│   ├── packaging.md
│   ├── aerospace-equipment.md
│   ├── cold-chain-logistics.md
│   ├── nutraceutical-manufacturing.md
│   ├── chemicals-distribution.md
│   └── seafood-value-chain.md
├── capabilities/
│   ├── computer-vision.md
│   ├── predictive-maintenance.md
│   ├── engineering-copilots.md
│   ├── industrial-agents.md
│   ├── supply-chain-ai.md
│   └── enterprise-workspace-ai.md
└── frameworks/
    ├── ai-maturity.md
    ├── strategic-centrality-differentiation.md
    └── use-case-prioritisation.md
```

Une nouvelle source doit :

1. enrichir les pages existantes ;
2. signaler contradictions et staleness ;
3. créer une nouvelle page uniquement si nécessaire ;
4. préserver le lien à la source.

## 13.3 Vérité entreprise

Une étude sectorielle peut proposer une **hypothèse** pour une entreprise.

Elle ne constitue jamais une preuve que le use case existe dans cette entreprise.

Règle canonique :

```text
SECTOR PATTERN
    ≠
COMPANY FACT
```

Le sector benchmark informe la recherche ; seule une preuve entreprise alimente la vérité entreprise.

---

# 14. Evidence OS

Réutiliser la doctrine des deux repos.

## États épistémiques

Chaque claim est :

- `fact`
- `inference`
- `hypothesis`
- `recommendation`
- `unknown`

## Chaîne minimale

```text
source
→ atomic fragment
→ claim
→ implication
→ decision relevance
```

Pour les gaps / use cases :

```text
source
→ fact
→ implication
→ capability gap
→ use-case hypothesis
→ validation question
```

## Source grading indicatif

### Grade A
- audited accounts ;
- official filings ;
- regulator ;
- annual report ;
- investor materials ;
- official technical documents.

### Grade B
- company press release ;
- official website ;
- Hivest transaction release ;
- official customer / supplier case study.

### Grade C
- reputable industry research ;
- Bain / BCG / McKinsey ;
- Big Four ;
- credible specialist consulting ;
- recognized trade publications.

### Grade D
- LinkedIn ;
- jobs ;
- conference ;
- public social signals ;
- indexed profiles.

### Grade E
- inference ;
- weak discovery source.

Une source D peut être utile pour générer une question, rarement pour établir seule une capacité stratégique.

---

# 15. Sources de recherche prioritaires

## Entreprise

- site corporate ;
- Hivest ;
- comptes / filings ;
- presse économique ;
- bases société accessibles ;
- communiqués ;
- acquisitions ;
- sites de production ;
- certifications ;
- patents / IP lorsque pertinent ;
- product documentation ;
- customer / supplier references.

## Organisation / people

- site entreprise ;
- LinkedIn ;
- conférences ;
- interviews ;
- job descriptions.

Ne jamais conclure :

> titre = pouvoir de décision.

## Technology signals

Rechercher notamment :

- ERP ;
- MES ;
- WMS ;
- TMS ;
- PLM ;
- CAD ;
- data platform ;
- cloud ;
- CRM ;
- industrial vision ;
- robotics ;
- IoT ;
- edge ;
- AI/ML stack ;
- software engineering environment.

## Sector state of the art

Multi-language lorsque pertinent :

- anglais ;
- français ;
- allemand ;
- italien ;
- autres selon géographie.

Priorité :

- Bain ;
- BCG ;
- McKinsey ;
- Deloitte ;
- PwC ;
- EY ;
- KPMG ;
- Accenture ;
- Capgemini ;
- industriels / hyperscalers quand les case studies sont utiles ;
- littérature technique ciblée.

Les case studies fournisseurs doivent être utilisées comme **preuve de possibilité**, jamais comme preuve de ROI transférable telle quelle.

---

# 16. Organisation des agents / skills

Ne pas construire un agent monolithique.

Réutiliser d’abord les skills existantes et ne créer que les gaps.

## 16.1 Portfolio Orchestrator

Responsabilité :

- roster ;
- sequencing ;
- manifests ;
- states ;
- handoffs ;
- portfolio consolidation ;
- HITL gates.

Ne fait pas la recherche lui-même.

## 16.2 Company Deep Research

Peut réutiliser :

- `ai-strategy-control-tower`
- `enterprise-demand-intelligence`
- research backends existants.

Responsabilité :

- company profile ;
- financial/business context ;
- AI / digital signals ;
- organization ;
- evidence ledger.

## 16.3 Value Chain Mapper

Réutiliser / étendre :

- `enterprise-value-chain-causal-analysis`.

Différence : partir ici de la **chaîne business globale** et non uniquement d’un use case déjà canonique.

## 16.4 AI Maturity Diagnostic

Nouvelle skill portefeuille :

- 8 dimensions ;
- evidence-bounded scoring ;
- readiness ;
- blockers ;
- contradictions.

## 16.5 Sector State-of-the-Art

Responsabilité :

- patterns sectoriels ;
- case studies ;
- use cases connus ;
- typical KPIs ;
- benchmark maturity ;
- failure patterns.

Les résultats vont dans le wiki sectoriel.

## 16.6 Use Case Intelligence

Réutiliser :

- `enterprise-use-case-intelligence`.

Ajouter :

- quick-win / structural / transformation ;
- 3 verticales ;
- strategic sourcing posture ;
- portfolio reusability.

## 16.7 Strategic 9-box

Responsabilité :

- centrality ;
- differentiation ;
- AI role ;
- build/buy/partner/outsource.

## 16.8 Red Team

Réutiliser le workflow canonical de `skills-notes-and-storytelling`.

Verdicts :

- `SURVIVES_RED_TEAM`
- `SURVIVES_WITH_NARROWING`
- `PIVOT_REQUIRED`
- `REOPEN_TARGETED`

Maximum :

- une passe de réparation ;
- une passe de vérification.

Si un défaut majeur subsiste : `REOPEN_TARGETED`.

## 16.9 Three-Pager Storytelling

Réutiliser :

- scaffold ;
- fragments ;
- claims graph ;
- rerank ;
- side stories ;
- reader/decision QA.

Ne doit pas mener de nouvelle recherche sauf `REOPEN_TARGETED`.

## 16.10 Output Engine

Étendre `nice-output-engine`.

Responsabilité :

- HTML ;
- PDF ;
- PNG ;
- QA visuelle ;
- charts ;
- radar ;
- 9-box ;
- Porter/value-chain canvas.

Ne modifie jamais le fond.

---

# 17. Pipeline par entreprise

## STEP 0 — Intake

Fixer :

- entité ;
- cutoff date ;
- périmètre ;
- secteurs ;
- géographies ;
- sources existantes ;
- trois inconnues capables d’inverser le diagnostic.

Sortie :

```text
00_intake.md
manifest.yaml
```

---

## STEP 1 — Company deep search

Objectifs :

- signalétique ;
- financials ;
- ownership ;
- acquisitions ;
- strategy ;
- growth thesis ;
- operations ;
- products ;
- markets ;
- tech stack signals ;
- organization ;
- AI signals.

Sortie :

```text
company_profile.md
financial_context.md
source_ledger.yaml
```

---

## STEP 2 — Value-chain reconstruction

Reconstruire la chaîne réelle :

- inputs ;
- sourcing ;
- engineering ;
- production ;
- logistics ;
- distribution ;
- service ;
- support.

Qualifier :

- margin pools ;
- cost pools ;
- bottlenecks ;
- controls ;
- VRIO resources.

Sortie :

```text
porter_value_chain.md
vrio.md
```

---

## STEP 3 — Sector deep search

Rechercher :

- état de l’art IA ;
- use cases réellement déployés ;
- benchmarks ;
- failures ;
- ROI ;
- architecture patterns ;
- operating model ;
- adoption.

Mettre à jour :

```text
wiki/sectors/*
wiki/capabilities/*
```

Puis revenir à l’entreprise avec des **hypothèses**, pas des faits.

---

## STEP 4 — AI maturity

Évaluer les 8 dimensions.

Sortie :

```text
ai_maturity.yaml
seven_s.md
```

---

## STEP 5 — Use-case harvest

Produire un inventaire large puis dédupliquer.

Pour chaque use case :

```yaml
id:
title:
vertical:
workflow:
problem:
value_mechanism:
company_evidence:
sector_evidence:
epistemic_status:
business_owner_hypothesis:
data_dependencies:
technology_dependencies:
risk:
time_to_value:
economic_value:
strategic_value:
repeatability:
portfolio_reuse:
horizon:
sourcing_posture:
unknowns:
validation_question:
```

---

## STEP 6 — Scaffold + red-team gap search

Avant rédaction :

1. chercher ce qui pourrait invalider les conclusions ;
2. identifier les claims faibles ;
3. identifier les données manquantes ;
4. relancer uniquement des recherches ciblées.

Ne pas faire une deuxième recherche large.

---

## STEP 7 — HITL

Présenter au minimum :

- company thesis ;
- business/value-chain interpretation ;
- maturity verdict ;
- 6–10 use cases ;
- quick wins ;
- structural bets ;
- transformation bets ;
- unknowns ;
- red-team verdict.

HITL décide :

- `GO_DRAFT`
- `RESEARCH_TARGETED`
- `NARROW_SCOPE`
- `PIVOT`

---

## STEP 8 — Storytelling / frozen content

Après `GO_DRAFT` :

```text
research
→ fragments
→ claims graph light
→ rerank
→ scaffold
→ fill
→ sourcing
→ counter-perspective QA
→ reader/decision QA
```

Puis geler :

```text
three_pager_content.yaml
```

---

## STEP 9 — Rendering

Transformer le contenu gelé en :

- Markdown ;
- HTML ;
- PDF ;
- PNG par page si utile.

Charts privilégiés :

- radar 7S ;
- 9-box ;
- value chain ;
- maturity bars ;
- horizon map.

Éviter Mermaid dans le document final si un graphique natif est plus lisible.

---

## STEP 10 — Loopback

À la fin de chaque entreprise :

- nouveaux patterns sectoriels ;
- nouveaux heuristics ;
- templates à améliorer ;
- false positives ;
- test / fixture potentiel ;
- amélioration de taxonomy.

Utiliser un dreaming Tier 0–3.

Aucune amélioration n’est promue silencieusement.

---

# 18. Boucle portefeuille optimisée

Le brief initial prévoit une société après l’autre. Il faut conserver cette logique, mais éviter un simple séquençage linéaire.

## Phase 00 — Crystalisation du système

Avant les onze diagnostics :

1. figer le modèle de maturité ;
2. figer le schema use case ;
3. figer le 3-pager ;
4. figer le evidence contract ;
5. figer la 9-box ;
6. écrire les skills ;
7. créer les tests / NRT ;
8. définir la taxonomie des secteurs.

## Phase 01 — Classification portefeuille

Créer :

- cluster industrie ;
- modèle économique ;
- taille ;
- footprint ;
- intensité industrielle ;
- exposition client ;
- data / OT intensity ;
- source richness.

Ne pas confondre `priority_to_research` et poids économique.

## Phase 02 — Deux pilotes contrastés

Avant de lancer les 10 entreprises, sélectionner :

- un acteur industriel complexe ;
- un acteur service/logistique/distribution ou life sciences.

Objectif :

- casser le template ;
- tester la preuve ;
- tester le radar ;
- tester la 9-box ;
- tester les use cases ;
- tester le PDF.

Après ces deux pilotes : **loopback obligatoire**.

## Phase 03 — Production par clusters

Réutiliser le wiki sectoriel.

Exemple :

### Cluster industrial / engineering

- VMI-Jokon
- Sphere
- Marie-Laure PLV
- CCE Group
- Agora Makers
- Aurightec

### Cluster process / regulated / life sciences

- Novasol Chemicals
- NV Labs

### Cluster supply chain / food

- Reunimer
- STG

Les clusters seront révisés après recherche ; ils servent au partage de connaissance, pas à imposer des conclusions.

## Phase 04 — Hivest

Le diagnostic de Hivest doit bénéficier de tout ce qui a été appris :

- quels patterns sont répétés ?
- quels patterns sont spécifiques ?
- quelle operating capability portfolio serait utile ?
- quelles mutualisations sont crédibles ?
- quels investissements doivent rester locaux ?

## Phase 05 — Portfolio synthesis

Produire :

- heatmap de maturité ;
- use-case portfolio ;
- recurring capability gaps ;
- cluster-specific plays ;
- cross-portfolio quick wins ;
- strategic transformation themes ;
- shared-assets candidates ;
- governance implications.

---

# 19. Ordre de recherche intelligent

Ne pas traiter automatiquement le portefeuille du plus ancien au plus récent.

Calculer un **research sequencing score** distinct du business value :

- disponibilité des sources ;
- capacité à tester le template ;
- diversité sectorielle ;
- représentativité ;
- potentiel de réutilisation ;
- actualité / transaction récente ;
- dépendances avec d’autres analyses.

Le but du sequencing est de **maximiser l’apprentissage du système**, pas de classer les investissements.

---

# 20. Context engineering / coût token

Le Work doit éviter de charger :

- toutes les sources ;
- tous les skills ;
- tous les templates ;
- toutes les sociétés ;

dans la même fenêtre.

## Pattern

```text
ROUTER
  ↓
load manifest
  ↓
load relevant skill
  ↓
load company wiki summary
  ↓
retrieve top evidence / claims
  ↓
execute stage
  ↓
persist structured artifact
  ↓
release context
```

## Tests

Placer les tests au plus près de la ressource :

```text
skills/<skill>/
  SKILL.md
  schema/
  tests/
  fixtures/
```

Distinguer :

- unit tests ;
- schema tests ;
- deterministic lint ;
- NRT ;
- render regression ;
- reader/decision fixtures.

Ne pas charger le corpus complet d’un NRT pendant un run normal.

---

# 21. Design et direction artistique

Objectif : présentation PE / strategy / operating partner, pas rapport académique.

## Principes

- forte densité mais lecture immédiate ;
- 1 insight dominant par page ;
- titres conclusifs ;
- graphiques simples ;
- peu de prose ;
- sources compactes ;
- métriques visibles ;
- décisions / unknowns séparés.

## Références de forme à réutiliser

- styles Canva déjà sélectionnés ;
- CV François lorsque pertinent comme langage visuel ;
- `two-pagers-nice` ;
- `nice-output-engine`.

Créer une variante :

```text
THREE_PAGER_PORTFOLIO_AI
```

avec un contrat strict de trois pages.

---

# 22. Definition of Done — entreprise

Une entreprise n’est `DONE` que si :

- [ ] roster / identité validée ;
- [ ] signalétique sourcée ;
- [ ] financials publics capturés ou explicitement inconnus ;
- [ ] business thesis établie ;
- [ ] Porter/value chain construite ;
- [ ] VRIO traité ;
- [ ] 7S traité ;
- [ ] SWOT dérivé ;
- [ ] AI maturity 8 dimensions ;
- [ ] company-vs-sector evidence séparée ;
- [ ] use cases récoltés ;
- [ ] 9-box appliquée ;
- [ ] quick wins / structural / transformation séparés ;
- [ ] build/buy/partner/outsource traité ;
- [ ] contradictions conservées ;
- [ ] unknowns explicites ;
- [ ] red-team exécuté ;
- [ ] HITL obtenu ;
- [ ] content contract gelé ;
- [ ] 3-pager rendu ;
- [ ] QA reader/decision passée ;
- [ ] wiki / loopback mis à jour.

---

# 23. Definition of Done — portefeuille

Le programme n’est `DONE` que si :

- [ ] les 10 participations actives sont diagnostiquées ;
- [ ] Hivest est diagnostiquée ;
- [ ] la comparabilité des scores est contrôlée ;
- [ ] les analyses sectorielles sont mutualisées ;
- [ ] les use cases transverses sont identifiés ;
- [ ] les use cases spécifiques ne sont pas artificiellement généralisés ;
- [ ] les capability gaps communs sont documentés ;
- [ ] les options de mutualisation sont challengées ;
- [ ] une portfolio heatmap existe ;
- [ ] les recommandations distinguent local vs portfolio-wide ;
- [ ] chaque conclusion portfolio garde la lineage vers les entreprises sources.

---

# 24. Prompt de démarrage recommandé pour ChatGPT Work

Copier la section suivante comme instruction initiale du Work.

---

## WORK MISSION — HIVEST AI PORTFOLIO DIAGNOSTIC

Tu pilotes un programme de diagnostic de maturité IA et de création de valeur pour Hivest Capital Partners.

### Mission

Construire un diagnostic comparable, evidence-grounded et décisionnel pour :

1. VMI-Jokon  
2. Novasol Chemicals  
3. NV Labs  
4. Sphere  
5. Reunimer  
6. Marie-Laure PLV  
7. CCE Group  
8. Agora Makers  
9. STG  
10. Aurightec  
11. Hivest Capital Partners  

### Output par entreprise

Un **3-pager commun** :

**Page 1 — Company Context + AI Maturity**
- signalétique ;
- financials ;
- business/growth thesis ;
- 7S radar ;
- SWOT ;
- AI maturity.

**Page 2 — Value Chain**
- Porter-like business chain ;
- margin/cost/friction pools ;
- VRIO capabilities ;
- AI opportunity overlay.

**Page 3 — Strategic AI Snapshot**
- Strategic Centrality × Differentiation 9-box ;
- priority use cases ;
- quick wins / structural / transformation ;
- build/buy/partner/outsource ;
- executive thesis + next validation.

### Repos à inspecter avant de créer une nouvelle méthode

- `https://github.com/achard-arnaud/ai-maturity-diagnostic`
- `https://github.com/achard-arnaud/skills-notes-and-storytelling`

Réutilise d’abord les skills, contracts, evidence rules, workflow, RunContext, red-team et output engine existants.

**Exclusion explicite :** ne réutilise pas le principe de product matching comme finalité du diagnostic.

### Architecture de connaissance

Applique un pattern Karpathy LLM-Wiki :

```text
raw immutable sources
→ evidence
→ fragments / claims
→ persistent wiki
→ analysis
→ artifact
```

Les recherches sectorielles doivent être cumulatives.

Un pattern sectoriel n’est jamais automatiquement une vérité entreprise.

### Evidence doctrine

Tout élément matériel doit être :

- `fact`
- `inference`
- `hypothesis`
- `recommendation`
- `unknown`

Préserve :

- date ;
- source ;
- evidence grade ;
- confidence ;
- contradictions ;
- lineage.

Ne jamais transformer :

- annonce → déploiement ;
- job → capability établie ;
- partenariat → adoption ;
- titre → pouvoir de décision ;
- benchmark sectoriel → réalité entreprise.

### AI scope

Couvrir toute la largeur :

- GenAI / workspace ;
- software engineering ;
- engineering / R&D ;
- industrial AI ;
- computer vision ;
- multimodal ;
- predictive / optimisation ;
- automation ;
- agents ;
- client / distribution ;
- data / platform ;
- governance / cyber.

### Maturity model

Évaluer :

1. AI strategy & value  
2. Operating model & governance  
3. Data & knowledge  
4. Technology & platform  
5. Delivery & industrialisation  
6. People / skills / adoption  
7. Security / risk / compliance  
8. AI breadth / domain penetration  

Ne calcule pas un score global par moyenne mécanique.

### Framework routing

Utiliser :

- Porter → value chain ;
- VRIO → strategic capabilities ;
- 7S → organizational readiness ;
- SWOT → synthesis ;
- GE / BCG / ADL → uniquement lorsque les données business le justifient ;
- Strategic Centrality × Differentiation → 3×3 sourcing / investment posture ;
- ERIC / Blue Ocean → transformation bets.

BCG n’est pas une 9-box.  
GE/BCG/ADL ne sont pas des maturity models IA.

### Research

Pour chaque société :

1. deep research company ;
2. value chain ;
3. sector state-of-art multi-language ;
4. AI maturity ;
5. use-case harvest ;
6. red-team gaps ;
7. targeted research only ;
8. HITL ;
9. final storytelling ;
10. render ;
11. loopback.

### Sector research

Cherche notamment :

- Bain ;
- BCG ;
- McKinsey ;
- Deloitte ;
- PwC ;
- EY ;
- KPMG ;
- Accenture ;
- Capgemini ;
- strong industrial / cloud / AI case studies.

Les vendor cases prouvent une possibilité, pas automatiquement une performance transférable.

### LinkedIn

Utilise LinkedIn pour :

- organisation ;
- hiring ;
- capabilities ;
- people ;
- transformation signals.

Revalide les rôles courants.

Ne prends jamais un profil LinkedIn unique comme preuve suffisante d’une capability organisationnelle.

### Use cases

Pour chaque use case :

- workflow ;
- business pain ;
- value mechanism ;
- economic value ;
- strategic value ;
- feasibility ;
- data dependencies ;
- technology dependencies ;
- adoption ;
- risk ;
- time-to-value ;
- repeatability ;
- portfolio reuse ;
- horizon ;
- sourcing posture ;
- unknowns ;
- validation question.

Classer en :

- quick win ;
- structural ;
- transformation.

### Red-team

Chaque entreprise passe par :

- conformance review ;
- counter-perspective review ;
- reader/decision review.

Verdict :

- `SURVIVES_RED_TEAM`
- `SURVIVES_WITH_NARROWING`
- `PIVOT_REQUIRED`
- `REOPEN_TARGETED`

Une réparation maximum puis une vérification.

### HITL

Ne rédige pas le 3-pager final avant validation humaine du :

- business thesis ;
- maturity verdict ;
- value chain ;
- use cases ;
- prioritisation ;
- red-team result.

### Rendering

Sépare le fond de la forme.

Le renderer ne peut jamais :

- créer un claim ;
- modifier une conclusion ;
- changer un score ;
- inventer une métrique.

Préférer radar / matrix / value-chain diagrams aux Mermaid bruts.

### Context engineering

Ne charge jamais tous les skills et tout le corpus.

Charge uniquement :

- manifest ;
- skill nécessaire ;
- wiki summary ;
- claims / evidence top-k nécessaires au stage.

Persist les artefacts structurés puis libère le contexte.

Les runs temporaires ne sont jamais conservés dans le code.

### Première séquence de travail

Ne commence pas immédiatement les onze diagnostics.

Commence par :

1. inspecter les deux repos ;
2. produire un gap analysis `existing capability → needed capability` ;
3. proposer l’arborescence cible ;
4. écrire le contrat du 3-pager ;
5. écrire le maturity schema ;
6. écrire le use-case schema ;
7. écrire la Strategic 9-box ;
8. écrire l’AGENTS.md / router ;
9. proposer les skills réellement nouvelles ;
10. construire les fixtures / NRT ;
11. sélectionner deux sociétés pilotes contrastées ;
12. lancer les pilotes ;
13. effectuer le loopback ;
14. seulement ensuite industrialiser le portefeuille.

### Règle de décision

À chaque étape :

> maximise la valeur informationnelle, la traçabilité et la réutilisabilité ; minimise le contexte chargé, les recherches redondantes et les conclusions non prouvées.

---

# 25. Première réponse attendue du Work

La première réponse du Work ne doit pas être un diagnostic d’entreprise.

Elle doit produire :

1. **audit de réutilisation des deux repos** ;
2. **capability map** :
   - existing ;
   - extend ;
   - new ;
   - reject ;
3. **architecture dossier / wiki / skills** ;
4. **schemas canoniques** à créer ;
5. **contrat 3-pager** ;
6. **plan de tests** ;
7. **sélection argumentée des deux pilotes** ;
8. **ordre de passage des 11 entités** ;
9. **risques / angles morts du programme** ;
10. **plan d’exécution du premier pilote**.

Cette première étape est le gate `PROGRAM_DESIGN_READY`.

---

# 26. Principaux risques à red-team dès le départ

## Risque 1 — Framework theatre

Accumuler Porter, VRIO, 7S, SWOT, BCG, ADL, GE, Blue Ocean sans valeur décisionnelle.

**Mitigation :** framework routing + optional lenses.

## Risque 2 — False precision

Produire des scores précis sur des sociétés privées avec peu de données.

**Mitigation :** confidence + `unknown` + evidence-bounded maturity.

## Risque 3 — Sector laundering

Transformer un use case courant dans un secteur en besoin établi de la société.

**Mitigation :** séparation sector hypothesis / company fact.

## Risque 4 — Generative AI bias

Surpondérer copilots et agents au détriment de vision / optimisation / industrial AI.

**Mitigation :** AI breadth model.

## Risque 5 — Portfolio over-standardisation

Chercher une solution commune partout.

**Mitigation :** local truth first ; mutualisation seulement après plusieurs preuves indépendantes.

## Risque 6 — Output-driven analysis

Forcer la recherche à tenir dans trois pages.

**Mitigation :** research package profond + frozen content contract + renderer séparé.

## Risque 7 — Context collapse

Charger trop de skills / docs / sources et perdre la stabilité du run.

**Mitigation :** router, staged loading, wiki, top-k evidence, colocated tests.

## Risque 8 — Run contamination

Stocker des fichiers temporaires/debug dans le repo canonique.

**Mitigation :** runs externes aux sources canoniques.

---

# 27. Sources / références de cadrage

## Repos

- `https://github.com/achard-arnaud/ai-maturity-diagnostic`
- `https://github.com/achard-arnaud/skills-notes-and-storytelling`

## LLM Wiki

- Karpathy LLM Wiki pattern — source conceptuelle / gist.
- Architecture recommandée : sources brutes immuables + wiki Markdown maintenu et enrichi par l’agent.

## Framework 7S

- McKinsey 7S framework : utiliser comme lens de cohérence organisationnelle.

## Source portefeuille

- Hivest Capital Partners — page officielle « Participations », état vérifié le 23 septembre 2026.

---

# 28. Décision de cadrage

Le bon point de départ n’est **pas** « lancer VMI-Jokon ».

Le bon point de départ est :

> **cristalliser le système de diagnostic, ses contrats, son Evidence OS, sa mémoire cumulative et son template ; le casser sur deux pilotes contrastés ; puis seulement lancer la production portefeuille.**

C’est ce qui permettra d’obtenir, à la fin, non pas onze bons documents indépendants, mais **un véritable operating system de value creation IA pour portefeuille de private equity**.
