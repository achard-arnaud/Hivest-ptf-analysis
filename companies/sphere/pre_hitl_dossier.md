# SPHERE — dossier pré-HITL de diagnostic IA

**Cutoff :** 23 septembre 2026 · **Périmètre :** groupe consolidé, avec distinction groupe/filiale lorsque la preuve le permet · **Statut :** pré-HITL, aucun rendu exécutif gelé.

## Thèse business provisoire

SPHERE est un groupe industriel européen d’emballages qui combine fabrication, négoce, R&D matériaux et distribution multi-marchés. Sa création de valeur repose sur trois actifs liés : une capacité industrielle multi-sites, une expertise matériaux/écoconception, et une largeur d’offre permettant de servir grand public, professionnels, collectivités et industriels.

La phase actuelle ajoute deux tensions de création de valeur : l’intégration de plusieurs acquisitions et systèmes locaux, et le passage à une offre professionnelle européenne unifiée avec SPHERE PRO. La priorité IA plausible se situe donc dans la **coordination des opérations, de la donnée produit et de la qualité/marge**, avant les assistants génériques. Cette formulation est une inférence, fondée sur la structure industrielle, le déploiement ERP, les acquisitions et la nouvelle organisation commerciale ; elle ne constitue pas une preuve d’un projet IA existant.

## Faits établis

| ID | Fait | Portée / source |
|---|---|---|
| F01 | SPHERE est un groupe industriel français fondé en 1976, passé sous contrôle majoritaire Hivest en 2024 [S06], leader européen des emballages ménagers, actif sur les marchés grand public, professionnel et collectivités. | Groupe ; site SPHERE. [S01] |
| F02 | Le groupe publie 18 sites de production européens, 235 000 tonnes de capacité annuelle, près de 814 M€ de CA en 2025 et plus de 1 800 salariés. | Groupe ; communiqué acquisition Polyex. [S02] |
| F03 | Le rapport annuel 2024 indique 782,054 M€ de CA consolidé, 77,945 M€ d’EBITDA, 46,054 M€ d’EBIT et 122,676 M€ d’endettement financier net. | Groupe consolidé ; exercice 2024. [S03] |
| F04 | La marge brute consolidée passe de 37,6 % à 40,1 % entre 2023 et 2024 ; les achats consommés s’élèvent à 472,7 M€ en 2024. | Groupe consolidé ; rapport annuel 2024. [S03] |
| F05 | Le BFR passe de 103,8 M€ à 125,7 M€ et les stocks de 147,4 M€ à 167,6 M€ entre 2023 et 2024. | Groupe consolidé ; rapport annuel 2024. [S03] |
| F06 | Les achats représentent 58 % de l’empreinte GES publiée en 2025 ; la fin de vie représente 33 %, le transport 5,3 % et l’électricité 1,3 %. | Groupe ; bilan carbone 2025. [S04] |
| F07 | SPHERE PRO rassemble l’offre professionnelle dans une organisation commerciale unifiée, avec plus de 4 000 références, un point d’entrée unique, un contrat et une logistique rationalisée. | Organisation commerciale ; publication SPHERE, avril 2026. [S05] |
| F08 | Le groupe a acquis Polyex en septembre 2026 pour renforcer le film industriel ; Polyex apporte 8 lignes d’extrusion, 8 lignes de coupe/soudure, 7 unités d’impression, 45 salariés et 10 000 tonnes de capacité. | Acquisition / nouvelle capacité ; communiqué SPHERE. [S02] |
| F09 | Le rapport annuel 2024 documente le déploiement de l’ERP groupe JD Edwards chez Flexopack et Comset en Italie. | Filiales italiennes ; rapport annuel 2024. [S03] |
| F10 | Le rapport annuel 2024 ne contient pas de mention trouvée d’intelligence artificielle ; il documente toutefois une assurance cyber couvrant le groupe. | Groupe ; recherche textuelle du rapport annuel. [S03] |

## Ce que les sources permettent d’inférer

- **I01 — pression BFR / stock :** l’augmentation des stocks et du BFR rend la prévision de demande, la segmentation des stocks et la coordination achat-production-distribution matériellement intéressantes. Cela reste une hypothèse de valeur ; aucun coût de stock obsolète ni service level par famille n’est public.
- **I02 — intégration data :** JD Edwards fournit un point d’appui pour la standardisation, mais son déploiement chez certaines filiales ne prouve ni une architecture groupe homogène ni une donnée industrielle exploitable en temps réel.
- **I03 — qualité/marge :** le groupe documente une hausse de marge brute et un incident qualité Biotec en 2023 ; un use case qualité peut être pertinent, mais les données de défauts, rebuts, causes et coûts ne sont pas publiées.
- **I04 — complexité commerciale :** SPHERE PRO et ses 4 000 références créent une opportunité de recherche produit, configuration, devis et cross-selling ; le bénéfice réel dépend de la qualité des données produit, des règles de substitution et de l’adoption commerciale.
- **I05 — matières et carbone :** les achats dominent l’empreinte GES ; la valeur IA pourrait porter sur scénarios matière, coût-carbone, prévision et optimisation des approvisionnements. Il faut éviter de confondre calcul d’empreinte et optimisation opérationnelle.

## Chaîne de valeur opératoire

| Bloc | Création de valeur | Frictions / contrôles | Opportunités IA à tester |
|---|---|---|---|
| Matières / achats | Accès PE, recyclés, biosourcés, aluminium, résines ; différenciation par mix matière et disponibilité | volatilité prix, qualité matière, traçabilité, carbone, délais | prévision prix/volumes, scénarios matière-coût-carbone, détection anomalies fournisseurs |
| R&D matériaux / formulation | Biopolymères, compostabilité, performance, brevets, cahiers des charges | compromis coût/performance/fin de vie ; validation réglementaire et technique | recherche documentaire augmentée, aide à la formulation, retrieval de certificats et essais ; validation humaine obligatoire |
| Extrusion / production | Transformation en films, sacs, gaines, housses, papier, aluminium et produits finis | réglages ligne, changement de série, rebuts, qualité, énergie, disponibilité | monitoring paramétrique, vision défauts, réduction scrap, maintenance ciblée, optimisation énergie |
| Conversion / finition / conditionnement | Coupe, soudure, impression, emballage et personnalisation | synchronisation lignes, tolérances, délais, traçabilité | prévision qualité, ordonnancement, inspection vision, assistance opérateur |
| Qualité / conformité | Sécurité alimentaire, normes, certifications, recyclé/compostable | dossiers de preuve, libération, non-conformités, audits | dossier qualité assisté, classification défauts, recherche de précédents, contrôle documentaire |
| Distribution / logistique | Disponibilité, couverture européenne, service et proximité | stocks, BFR, transport, multi-sites, allocation | prévision demande, allocation de stock, transport, promesse de délai |
| Vente / SPHERE PRO | 4 000+ références, contrat unique, cross-selling, offre professionnelle | catalogue complexe, règles de substitution, connaissance commerciale | assistant de configuration, recherche catalogue, recommandation explicable, devis assisté |
| Support data / ERP / gouvernance | Coordination groupe et intégration des acquisitions | hétérogénéité systèmes, droits, qualité et ownership des données | catalogue produit, lineage, data quality monitoring, knowledge graph fournisseur-produit-process |

## Maturité IA evidence-bounded

Une cotation globale n’est pas défendable à ce stade. La preuve publique établit une transformation industrielle, RSE, ERP et commerciale ; elle ne démontre pas un portefeuille IA en production.

| Dimension | Verdict provisoire | Niveau maximal prouvé | Inconnue critique |
|---|---|---:|---|
| Strategy & value | Des priorités business et environnementales sont explicites ; stratégie IA non établie. | null — non établi | sponsor, business cases, budget IA, KPI |
| Operating model & governance | Gouvernance groupe, acquisitions et SPHERE PRO visibles ; gouvernance IA non établie. | null — non établi | decision rights data/IA, modèle central/fédéré |
| Data & knowledge | ERP groupe partiellement déployé ; données multi-sites et produit riches mais hétérogènes probables. | null — non établi | MES, historian, qualité, MDM produit, lineage |
| Technology & platform | JD Edwards documenté chez certaines filiales ; stack OT/IT/analytics non établie. | null — non établi | cloud, APIs, MES, edge, vision, observability |
| Delivery & industrialisation | Aucune preuve publique de cas IA en production. | null — non établi | pilotes, monitoring, réutilisation, run ownership |
| People & adoption | Échelle industrielle et nouvelle organisation commerciale ; compétences IA non établies. | null — non établi | data/AI roles, formation, adoption, supervision |
| Security, risk & compliance | Assurance cyber documentée ; contrôles IA/OT et risques modèles non établis. | null — non établi | segmentation OT, tiers, privacy, model risk |
| AI breadth | Applicabilité potentielle forte sur opérations, engineering, revenue et corporate ; pénétration réelle non établie. | null — non établi | cas actifs par domaine |

## Strategic Centrality × Differentiation

| Capacité | Centralité | Différenciation | Posture provisoire | Pourquoi |
|---|---|---|---|---|
| Expertise matériaux / R&D biopolymères | Core | Differentiating | BUILD / PARTNER sélectif | actifs de connaissance et IP ; contrôle des données et validation |
| Qualité process / réglage extrusion | Core | Differentiating | BUILD / PARTNER | impact marge et réputation ; dépendance aux données ligne |
| ERP / MDM produit / intégration groupe | Enabler | Parity | BUILD/BUY contrôlé | socle d’exécution ; éviter de multiplier les systèmes de référence |
| Prévision demande / allocation stock | Enabler | Parity | PARTNER / configure | valeur récurrente, transférable, à tester sur une famille |
| Catalogue SPHERE PRO / configuration commerciale | Core | Differentiating | BUILD / PARTNER | devient une capacité commerciale distinctive si les données sont propres |
| Back-office documentaire générique | Support | Commodity | BUY / automate | faible différenciation ; hard gates confidentialité et adoption |

## Use-case inventory prioritaire

Les scores restent qualitatifs jusqu’à l’accès aux baselines. Les cas ci-dessous sont des hypothèses de travail, pas des demandes observées de SPHERE.

| ID | Use case | Famille / horizon | Valeur attendue | Garde-fous / question de validation |
|---|---|---|---|---|
| UC-S01 | Data quality + MDM du catalogue SPHERE PRO | Prérequis data / horizon à confirmer | réduire erreurs de références, doublons, attributs et substitutions | mesurer taux de complétude/erreur sur une famille ; owner commercial/data |
| UC-S02 | Assistant de recherche et configuration produit | Structural / 6–18 mois | réduire temps de réponse et améliorer cross-selling explicable | règles de compatibilité, sources certifiées, validation commerciale |
| UC-S03 | Prévision demande et segmentation des stocks | Structural / 6–18 mois | réduire BFR/stock et protéger service | baseline SKU-site, saisonnalité, substitutions, coût de rupture |
| UC-S04 | Optimisation allocation matière et scénario coût-carbone | Structural / 6–18 mois | arbitrer PE/recyclé/biosourcé/aluminium sous contraintes | prix, disponibilité, qualité, ACV ; décision humaine |
| UC-S05 | Détection défauts sur film/sac par vision | Structural / 6–18 mois | réduire rebuts, libérations tardives et réclamations | images labellisées, faux négatifs, intégration ligne, OT safety |
| UC-S06 | Monitoring paramètres extrusion et détection dérives | Structural / 6–18 mois | détecter dérives avant non-conformité et scrap | historian/MES et synchronisation lot-qualité à confirmer |
| UC-S07 | Ordonnancement multi-sites / réduction changements de série | Transformation / 18–36 mois | augmenter capacité utile et réduire pertes de démarrage | contraintes clients, nettoyage, qualification et ownership usine |
| UC-S08 | Knowledge assistant R&D / qualité / audits | Quick win / 0–6 mois | retrouver certificats, essais, normes, non-conformités et précédents | corpus autorisé, citations obligatoires, confidentialité/IP |

### Positionnement de priorité révisé

La priorité économique et le séquençage sont remplacés par la matrice D01–D06 ci-dessous. UC-S01 est un prérequis data, non un cas IA autonome.

## Red-team ciblé

| Attaque | Résultat actuel | Action |
|---|---|---|
| « SPHERE est déjà mature en IA parce que son ERP est déployé » | Rejeté : ERP ≠ IA en production. | conserver delivery IA à non établi |
| « L’IA vision est prioritaire car elle existe dans le secteur » | Réduit à hypothèse de faisabilité. | demander données défauts/ligne et baseline scrap |
| « La hausse de marge prouve le ROI d’un use case » | Rejeté : effet prix/mix, matières, périmètre et coûts se combinent. | isoler baseline par ligne/famille |
| « SPHERE PRO prouve un moteur de recommandation » | Rejeté : organisation commerciale annoncée, moteur IA non documenté. | tester catalogue et règles d’éligibilité |
| « Les 18/19 sites sont homogènes » | Rejeté : preuves d’intégration partielle seulement. | cartographier systèmes et ownership par site |
| « La décarbonation est un problème de modèle prédictif » | Trop étroit : achats et fin de vie dominent l’empreinte. | commencer par données d’achat, matière, ACV et gouvernance |

## Trois inconnues qui peuvent inverser le diagnostic

1. **Systèmes et données industrielles par site :** ERP, MES, historian, qualité, vision, maintenance et identifiants lot/SKU sont-ils reliés ?
2. **Économie opérationnelle :** quelles familles concentrent scrap, réclamations, changements de série, stocks, ruptures et énergie ?
3. **Operating model :** qui possède les données, le catalogue SPHERE PRO, les standards process et le droit de déployer un pilote sur une usine ?

## Lecture externe : trois arènes, pas un marché unique

**Analyse au 23 septembre 2026.** Les faits de marché sont distingués des hypothèses d’exposition de SPHERE. Aucun TAM ni taux de croissance global n’est retenu : les périmètres disponibles ne recouvrent pas précisément les activités du groupe.

| Arène | Ce que le client achète / hypothèse économique | Position Sphere et test nécessaire |
|---|---|---|
| Emballages ménagers et usages courants | Prix à l’usage, résistance, disponibilité ; pouvoir de négociation des grands comptes à mesurer | Couverture produits et canaux [S01]. Tester concentration clients, clauses d’indexation et marge par famille plutôt que supposer une prime écologique. |
| Professionnels / collectivités | Fiabilité d’approvisionnement, simplicité du catalogue et conformité aux usages | SPHERE PRO unifie l’offre [S05]. Tester coût de service, panier, taux de conversion et substitutions ; 4 000 références peuvent créer valeur et complexité. |
| Films industriels / spécialités matériaux | Performance technique, constance qualité, qualification et coût total chez le client | Polyex renforce le film industriel [S02]. Tester marges, durée de qualification et coût des défaillances ; montée en gamme possible, pas acquise. |

### Signaux sectoriels et concurrence

- **Matières : volatilité, plutôt qu’une baisse linéaire.** FPE publie au T1 2026 une hausse trimestrielle du HDPE de 12 % et du LDPE de 16 % [S09]. Cet indice n’est ni le prix payé par SPHERE ni une prévision annuelle. Le rapport Sphere décrit un décalage possible entre achats et répercussion client [S03, p.30] : le mécanisme économique à examiner est la marge exposée pendant ce délai.
- **Circularité : contrainte d’économie industrielle autant que promesse commerciale.** La Commission décrit des marchés de recyclés fragmentés, des coûts énergétiques élevés et une concurrence extérieure qui fragilisent les recycleurs [S10]. Cela justifie de tester disponibilité, qualité et preuve d’origine des intrants chez Sphere ; cela ne prouve aucune rupture fournisseur actuelle.
- **Accès au marché : documenter produit par produit.** Le PPWR s’applique généralement depuis le 12 août 2026 [S11]. Les échéances et obligations diffèrent selon usages, matières et exemptions ; un sac-poubelle et un emballage de produit ne doivent pas recevoir automatiquement la même qualification. Le cas IA potentiel porte sur l’aide au dossier de preuve, avec validation réglementaire humaine.
- **Rendement industriel : établir la frontière sans IA.** W&H documente déjà des paramètres et alertes de production via RUBY [S07]. L’enjeu n’est donc pas de rebaptiser le monitoring « IA », mais de démontrer un gain additionnel au contrôle statistique, aux alarmes et aux standards opératoires.

| Pair / comparabilité | Signal observable | Implication analytique / limite |
|---|---|---|
| Barbier — extrusion de films PE | Expertise et équipement d’extrusion mis en avant [S12] | La maîtrise du film constitue une base concurrentielle ; il faut prouver ce qui distingue Sphere. Ne pas comparer les groupes comme des périmètres identiques. |
| RKW — films techniques et industriels | Offre multi-applications, notamment emballages industriels et films de performance [S13] | La technicité est un espace concurrentiel existant. Un film plus performant n’est pas à lui seul un marché sans concurrence. Parts de marché et écarts de coût non établis. |

### Hiérarchie des drivers — priorité business provisoire

Cette hiérarchie est une inférence d’analyste, pas un classement validé par le management. La matérialité observée détermine l’ordre d’investigation ; la disponibilité des données détermine ensuite le pilote réalisable.

| Rang / ID | Driver, exposition et enjeu | Stratégie de valeur → opportunités | KPI et condition qui inverse le rang |
|---|---|---|---|
| 1 — D01 | **Marge matière / repricing.** Volatilité externe [S09] ; 472,7 M€ d’achats consommés et décalages tarifaires documentés [S03]. Tous ces achats ne sont pas du PE. | COST_REDUCTION + COST_AVOIDANCE → UC-S04 ; ajouter UC-S09 surveillance marge/clauses/prix. Optimisation mix, détection exposition, aide à la décision ; pas trading autonome. | Marge contributive €/kg, délai de répercussion, pertes matière. Rang réduit si contrats couvrent déjà l’exposition et pertes marginales. |
| 2 — D02 | **Qualité constante / rendement matière.** Films techniques et recyclés nécessitent une qualité tenue ; coût des rebuts Sphere inconnu. Incident Biotec historique [S03] : signal, pas baseline actuelle. | COST_REDUCTION + RISK_RESILIENCE → UC-S05/S06 ; vision/prédiction seulement si mieux que SPC/règles. | Scrap kg/t, coût non-qualité, faux négatifs, réclamations. Rang réduit si coût évitable faible ; ne pas additionner les mêmes rebuts avec D01. |
| 3 — D03 | **Stock / service / cash.** 167,6 M€ de stocks et 125,7 M€ de BFR en 2024 [S03] ; hausse en partie liée au périmètre. | CAPITAL_PRODUCTIVITY → UC-S03 ; prévision et segmentation comparées à politiques simples. | Stock moyen, jours de stock, OTIF, ruptures. Réduire rang si stocks sont requis par service/qualification ; cash libéré distinct du profit. |
| 4 — D04 | **Taille utile / intégration / capacité.** Acquisitions et offre unifiée [S02/S05] ; gains d’échelle potentiels mais transferts de production non prouvés possibles. | COST_AVOIDANCE + CAPITAL_PRODUCTIVITY → UC-S07 ; différer capex seulement si goulot démontré. | Changements de série, capacité qualifiée, délais, capex réellement évitable. Devient prioritaire si saturation d’un goulot et demande ferme. |
| 5 — D05 | **Différenciation / montée en gamme.** Matériaux, films industriels, largeur d’offre [S02/S05] face à pairs techniques [S12/S13]. | DIFFERENTIATION_GROWTH → UC-S02 et UC-S10 formulation/essais assistés. | Marge incrémentale, taux de gain, délais de qualification, volonté de payer. Remonte si premium ou commandes démontrés ; cross-sell n’est pas Blue Ocean. |
| Transversal — D06 | **Conformité / traçabilité / accès marché.** Contexte réglementaire [S11] et approvisionnement circulaire [S10]. Exposition à qualifier par SKU. | RISK_RESILIENCE → UC-S08 ; socle UC-S01. | Complétude des preuves, délai dossier, erreurs. Devient bloquant avant tout rang économique si exigence applicable non satisfaite. |

### Choix de stratégie IA et tests de valeur

**Thèse révisée :** commencer l’investigation économique par marge matière, qualité et stock/service ; sélectionner ensuite un pilote borné sur la meilleure combinaison de valeur démontrable, données et owner. MDM et recherche documentaire peuvent préparer ce pilote, sans capter par défaut le budget prioritaire.

- **Cost killing :** supprimer des pertes mesurées, nettes du coût d’exploitation et de contrôle. Pour D02, gain annuel = volume concerné × baisse de scrap × coût évitable net de valorisation du rebut. Variables inconnues : aucun ROI chiffré.
- **Cost avoidance :** comparer à une dépense future crédible (incident, charge, investissement) et préciser probabilité/horizon. Des heures gagnées ne sont pas automatiquement des économies de salaires.
- **Capital productivity :** pour D03, cash libérable = baisse soutenable de stock moyen ; seul le coût de portage évité peut alimenter un gain récurrent. Aucun double compte avec EBITDA.
- **Montée en gamme :** pour D05, tester marge incrémentale après service, cannibalisation et essais. Une différenciation matériaux peut reposer d’abord sur R&D et process, avec IA auxiliaire.
- **Blue Ocean — option non validée :** hypothèse d’une offre de conception et preuve de performance/circularité pour des clients aujourd’hui mal servis. Vérifier non-clients, alternatives, willingness-to-pay et coût de service par entretiens ; arrêter si simple substitution à une offre existante. Aucun revenu ni avantage acquis n’est retenu.

### Enrichissement de l’inventaire et ordre de travail

UC-S01 est reclassé **prérequis data/MDM**, pas cas IA autonome. UC-S02 à S08 restent des hypothèses. Ajouter **UC-S09 : surveillance marge matière et délais de repricing** (D01 ; baseline BI/règles avant modèles) et **UC-S10 : aide à la formulation et au plan d’essais** (D05 ; expertise matériaux, IP, essais physiques et validation humaine obligatoires). Aucun de ces cas n’est présenté comme déployé.

1. Réconcilier achats, volumes, prix de vente et clauses sur une famille ; comparer D01/D02/D03 en valeur évitable.
2. Vérifier en parallèle données et owner : lot/ligne/qualité pour D02 ; SKU/site/service pour D03. Le socle MDM est financé pour un usage défini.
3. Choisir un pilote et une alternative sans IA ; mesurer avant/après sur périmètre comparable, saisonnalité et mix contrôlés. Aucune généralisation groupe sur seul résultat d’une ligne.
4. Traiter D04/D05 comme extensions conditionnelles ; tester l’option Blue Ocean séparément des gains d’efficacité.

### Projection vers le trois-pages

| Page | Message à intégrer | Éléments à conserver |
|---|---|---|
| 1 | La marge matière et la qualité structurent la priorité, dans un contexte de volatilité et de circularité sous contrainte économique. | Trois arènes, deux pairs, top drivers D01–D03, signaux S09–S13 ; maturité IA inconnue explicitée. |
| 2 | Les opportunités suivent les mécanismes industriels, des achats au service client. | D01 achats/pricing ; D02 extrusion/qualité ; D03 stocks ; D04 planification ; D05 R&D/vente ; D06 contrôles. |
| 3 | Investir selon valeur prouvable ; distinguer efficacité, cash et différenciation. | Stratégie de valeur + sourcing + alternative sans IA + gate pour chaque cas ; MDM présenté comme prérequis. |

### Couverture, red-team et recherche restante

**Couvert :** prix sectoriels, enjeux recyclage, cadrage réglementaire général, deux pairs, possibilité technique, exposition financière historique Sphere. **Partiel :** demande et concentration clients par segment, pression concurrentielle par pays, marges par application, comparaison de productivité. **Non disponible :** données internes industrielles et preuves de déploiement IA. Les publications professionnelles accessibles ne remplacent pas une étude exhaustive de marché ; aucune étude payante n’est déclarée lue.

Questions décisives : quelle part des achats est exposée sans répercussion rapide ? quel coût de non-qualité est réellement évitable ? quelle part du stock est liée à acquisitions, sécurité ou obsolescence ? quel segment paie une prime démontrable ? qui possède le pilote ? Owners proposés à confirmer : achats/finance D01, industriel/qualité D02, supply chain D03, opérations D04, commercial/R&D D05, qualité/réglementaire D06.

Contre-preuves : hausse de stock ≠ mauvaise planification ; inflation sectorielle ≠ prix d’achat Sphere ; GES ≠ coûts ; assurance cyber ≠ contrôle IA ; comparables ≠ mêmes marchés ; PPWR ≠ obligation identique pour tout produit ; technologie disponible ≠ besoin prouvé. La priorité reste provisoire jusqu’à ces tests.

## Verdict pré-HITL révisé

La lecture externe renforce une thèse de protection de marge, qualité et productivité du capital. Différenciation et Blue Ocean sont des options à tester séparément. Les huit niveaux de maturité IA restent inconnus faute de preuves spécifiques. Dossier enrichi pour revue HITL ; aucun GO_DRAFT ni rendu final n’est attribué.

### Précautions de périmètre
Les 18 sites publiés dans le communiqué daté sont retenus ; un profil social mentionne 19, à réconcilier. Le CA 2025 n’établit pas une croissance organique face à 2024. La dette financière nette 2024 est présentée séparément des passifs IFRS16 de 25,1 M€. La hausse des stocks/BFR comporte un effet acquisitions. Les achats dans le bilan carbone ne mesurent pas la structure des coûts.

# Registre de sources — SPHERE / contexte sectoriel

Collecte et cutoff : 23 septembre 2026. Sources publiques consultées ; sources historiques reprises du dossier précédent. Ce registre conserve URLs et limites, pas une archive intégrale des originaux. Les pages web sont extraites/synthétisées ; aucun hash de fichier raw n’est revendiqué.

| ID | Document | Publication | Portée / limite |
|---|---|---|---|
| S01 | [SPHERE, présentation](https://www.sphere.eu/fr/) | non daté | Identité et marchés ; chiffres anciens exclus |
| S02 | [SPHERE, acquisition Polyex](https://www.sphere.eu/en/the-sphere-group-expands-its-operations-in-the-industrial-film-market-through-the-acquisition-of-polyex/) | 2026-09-07 | Chiffres groupe publiés et périmètre Polyex ; pro forma à confirmer |
| S03 | [SPHERE, rapport annuel 2024](https://uploads1.craft.co/uploads/unified_record/source/document/2165394/f71eb45b0ee203cf.pdf) | 2025-03-27 | Rapport groupe hébergé par tiers ; pp.18–21 finances, p.25 ERP, p.30 matières |
| S04 | [SPHERE, bilan GES](https://www.sphere.eu/fr/plus-de-95-de-reduction-des-emissions-de-gaz-a-effet-de-serre-ges-entre-2022-et-2025/) | 2026-07-30 | Répartition carbone, pas répartition des coûts |
| S05 | [SPHERE PRO](https://www.sphere.eu/fr/le-groupe-sphere-presente-au-salon-interclean-2026-sa-nouvelle-division-europeenne-sphere-pro/) | 2026-04-14 | Organisation et 4000 références, pas preuve IA |
| S06 | [Hivest, prise de participation](https://hivestcapital.com/hivest-capital-partners-mene-la-reconfiguration-capitalistique-du-groupe-sphere-leader-europeen-des-emballages-menagers-durables/) | 2024-10-24 | Annonce majoritaire ; chiffres historiques |
| S07 | [W&H, RUBY](https://www.wh.group/cee/en/company/news_events/e_magazine/intelligent_data_use_with_ruby/) | non établi | Monitoring extrusion ; discours équipementier, pas ROI Sphere |
| S08 | [ISRA, inspection films](https://www.isravision.com/en-en/industries/plastic-film-foil-sheets) | non daté | Possibilité technique ; pas preuve déploiement Sphere |
| S09 | [FPE, prix T1 2026](https://www.flexpack-europe.org/press-release/rising-raw-material-costs-and-geopolitical-tensions-impact-the-markets-for-flexible-packaging-materials) | 2026-03-26 | Association, prix sectoriels trimestriels ; panier distinct des achats Sphere |
| S10 | [Commission européenne, circularité plastiques](https://cyprus.representation.ec.europa.eu/news/new-package-measures-boost-circular-economy-and-strengthen-europes-plastic-recycling-2025-12-19_en) | 2025-12-19 | Pressions sur recyclage ; mesures annoncées, pas présumées toutes adoptées |
| S11 | [Commission européenne, packaging waste](https://environment.ec.europa.eu/topics/waste-and-recycling/packaging-waste_en) | page évolutive | Application générale PPWR 12 août 2026 ; qualification par produit requise |
| S12 | [Barbier, production equipment](https://www.barbiergroup.com/en/barbier-group-2/production-equipment/) | non daté | Pair extrusion ; positionnement auto-déclaré, pas parts de marché |
| S13 | [RKW, corporate profile](https://rkw-group.com/company/corporate-profile/) | non daté | Pair films techniques ; domaines plus larges que Sphere |
