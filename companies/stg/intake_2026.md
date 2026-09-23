# STG — second pilote : transport frigorifique après la séparation logistique

**Date de lecture : 23 septembre 2026. État : RESEARCH / intake exploratoire.** Périmètre cible : activités de transport frigorifique et fonctions support qui restent dans STG. L'identité économique, le personnel, les systèmes et les coûts du nouveau périmètre sont à confirmer ; aucune estimation de ROI ni note de maturité IA.

## 1. Le fait qui change le pilote

STG déclare s'être séparé de l'activité logistique en 2026 pour se recentrer sur le transport. Boréal Logistics reprend l'entreposage/logistique ; une enquête sectorielle du 16 septembre évalue cette activité à 850 personnes, douze entrepôts et 90 M€ de CA 2025 **au sein de l'ancien ensemble**. Ces données ne se soustraient pas mécaniquement à un CA STG ancien pour calculer le transport 2026 : méthode de consolidation et dates de cession à obtenir. [STG gouvernance](https://www.stg.fr/qui-sommes-nous/) ; [Supply Chain Magazine, 16/09/2026](https://supplychainmagazine.fr/nl/2026/boreal-logistics-regroupe-les-ex-activites-logistiques-de-stg/).

Le site STG annonce actuellement 2 200 collaborateurs et plus de vingt plateformes pour des flux du colis au camion complet ; ces chiffres sont des **déclarations de site consulté**, à réconcilier avec les comptes du nouveau périmètre. Les formats affichés : messagerie, groupage, lots, complets, dédiés et affrètement, plus la distribution multitempérature de restauration hors foyer (RHF). [Ambition](https://www.stg.fr/notre-ambition/) ; [transport](https://www.stg.fr/le-transport-frigorifique/) ; [RHF](https://www.stg.fr/le-transport-rhf/).

| Ce qui sort du diagnostic STG | Ce qui reste à caractériser chez STG | Test de frontière |
|---|---|---|
| Stockage contractuel, inventaire et automatisation des entrepôts cédés | Plans de transport, agences, quai/transit, flotte, sous-traitants, froid, incidents, facturation | Vérifier contrat, patrimoine de données, SI et personnel transférés à Boréal |
| Scénarios de WMS et optimisation du stock client chez Boréal | Consolidation du fret, affectation de capacité, tournées, heure d'arrivée et preuves de livraison | Séparer quai de transit et entrepôt logistique avant de modéliser |

## 2. Lecture industrielle et commerciale provisoire

**Segmentation de travail** (pas ventilation de CA) : (a) messagerie et groupage réfrigérés multiclients ; (b) lots, complets et dédié pour l'agroalimentaire et la distribution ; (c) RHF à contraintes multi-sites et multitempératures. Ces segments découlent des offres affichées, pas d'une comptabilité analytique. Le top 3 des CA, leurs croissances et parts relatives restent inconnus. Une matrice BCG exige aussi la croissance externe de chaque marché et la part relative par segment.

| Driver à instruire | Exposition observée | Mécanisme de valeur et mesure | Risque de mauvais classement |
|---|---|---|---|
| D1 — densité et taux de remplissage du réseau | Offre colis→complet, >20 plateformes, promesse 24/48 h | Coût par livraison/tonne, km à vide, taux de chargement, km sous-traités et OTIF ; comparaison par lane, saison et température | Une baisse des km peut dégrader promesse, chaîne du froid ou service RHF |
| D2 — continuité du froid et conformité | Positif, négatif, multi-températures ; suivi télématique annoncé en 2021 | Incidents et réclamations par 1 000 voyages, temps hors consigne, résolution documentée | Le suivi et les alertes existent déjà ; ne jamais compter leur valeur une seconde fois |
| D3 — coût carburant/énergie et renouvellement | STG indique éco-conduite, renouvellement et objectif GES 2028 | L/100 km à mix de routes comparable, énergie par livraison conforme, coût complet du parc | Économies déclarées en éco-conduite et réduction de GES ne sont ni causalité IA ni économie future additionnelle |
| D4 — fiabilité sous volatilité | Flux tendus, RHF multi-points et objectifs de livraison | OTIF, taux de retard, capacité disponible, taux d'échec/retour et pénalités réellement supportées | Une prévision exacte sans flexibilité de dispatch ne crée pas de valeur |
| D5 — prix et marge par compte/flux | Mélange formats de transport ; aucun mix de revenu actuel établi | Marge contributive par lane/client/service, indexation énergie, coût froid et accès ; tests de renouvellement | Ne pas inférer un pouvoir de prix du seul maillage national |

L'ordre D1→D5 est une **hypothèse de recherche**, pas une allocation de capital. Tester d'abord le coût de service et les marges de flux pour savoir si D5 ou D2 doivent passer devant D1. STG indique des plans de transport existants, des remorques à étage et des actions d'éco-conduite : tout business case doit partir de cet existant. [RSE STG](https://www.stg.fr/engagements/) ; [offre transport](https://www.stg.fr/le-transport-frigorifique/).

**4P et cinq forces, première hypothèse.** Produit : fiabilité de température et créneaux sur plusieurs formats. Place : maillage et accès client par agences. Prix : comparer mix, surtaxes, conditions d'indexation et pénalités ; aucun barème comparable acquis. Promotion : promesse de sécurité alimentaire, proximité et responsabilité. Pouvoir des acheteurs potentiellement élevé chez grands donneurs d'ordre, à vérifier sur concentration CA ; pouvoir des fournisseurs à tester sur carburant, conducteurs, véhicules et capacité affrétée ; rivalité et substituts à analyser par lane et type de température. Le réseau STEF est un comparateur de capacité et de couverture, **pas** une preuve des trois leaders ni d'un prix STG. [STEF FAQ](https://www.stef.com/corporate/fr/faq) ; [France Logistique, décarbonation avril 2026](https://www.francelogistique.fr/wp-content/uploads/2026/04/2026-04_FranceLogistique_Note-Verdissement-TRM.pdf).

## 3. Base technique et thèse APS/TMS

STG a décrit en 2021 la sélection d'Ekolis pour les températures, alertes, géolocalisation et entretien des remorques, après un essai de deux mois sur dix véhicules ; le communiqué évoque une cible de près de 1 000 semi-remorques et l'interopérabilité avec le TMS et la gestion de parc. **La cible 2021 n'est pas un parc installé démontré en 2026.** C'est une preuve de système et de processus déjà envisagés, pas de déploiement d'IA/ML. [STG, annonce Ekolis](https://www.stg.fr/stg-optimise-le-suivi-des-temperatures-de-sa-flotte-avec-ekolis/).

Pour STG, la question analogue à l'APS/S&OP de Sphere est le **pilotage du réseau transport** : prévision des volumes par lane/jour/température, décision de capacité et d'affrètement, optimisation sous contraintes d'horaires/froid/conduite, puis arbitrage humain au dispatch. Un TMS et ses plans existants constituent la baseline. Le ML peut prévoir volume, ETA et risque d'incident ; l'optimisation mathématique choisit un plan sous contraintes ; règles/alertes gèrent des seuils ; la GenAI aide à qualifier litiges ou justificatifs. Cette architecture est **proposée**, non observée chez STG. France Logistique distingue justement prévision, optimisation et traitement documentaire dans son guide 2026 ; son taux sectoriel d'adoption n'est pas une note STG. [France Logistique](https://www.francelogistique.fr/ia/) ; [France Num, avril 2026](https://www.francenum.gouv.fr/guides-et-conseils/intelligence-artificielle/comprendre-et-adopter-lia/lintelligence-artificielle-5).

| Hypothèse d'essai | Baseline et technique minimale | Contrôle, KPI, arrêt |
|---|---|---|
| Prévision volume/capacité et plan de réseau | Plan actuel TMS, saisonnalité et règle simple → modèle temporel si gain incrémental ; solveur de tournées séparé | Simuler sur historique hors échantillon, puis mode conseil ; coût complet par livraison conforme + OTIF ; arrêter si économie absorbée par complexité ou baisse de service |
| ETA et gestion proactive des retards | Heure planifiée et alertes télématiques existantes → ML seulement si meilleur que la baseline | Calibration par lane et créneau, fausses alertes, retards anticipés utiles ; pas de réacheminement autonome |
| Risque de rupture de froid | Alertes température actuelles → diagnostic sur dérive capteurs, portes et groupe froid si événements observables | Incidents confirmés et délai de réaction ; pas d'arrêt automatique sans procédure qualité |
| Litiges/preuves de livraison et facturation | Documents transport et contrôles existants → extraction assistée, dossier préparé | Taux d'erreur et temps de résolution ; validation humaine de toute décision client/financière |
| Prix par service/route | Barème et indexation contractuelle, coût de service observé → recommandation ML seulement après segmentation et test commercial | Marge contributive et churn ; aucune écriture automatique en tarification |

**Stratégie ML observée : inconnue.** Les résultats publics trouvés attestent TMS/télématique, pas équipe data/ML ni modèles en production. Ne pas attribuer à STG français le site **STG Telematics**, société distincte qui commercialise « DaVinci AI » depuis un autre marché. Recherche d'offres et profils LinkedIn publics à compléter, en tenant compte de la séparation Boréal.

## 4. Direction et recherche à relancer

Le site actuel présente **Jean-Emmanuel Mongnot à la présidence**. Un communiqué STG de 2018 nommait **Franck Maso directeur général délégué aux opérations** ; aucun élément primaire récent examiné ne permet d'en faire le COO actuel au 23/09/2026. Un ancien CV place **Laurent Buc comme DSI de mai 2010 à avril 2017** ; il n'identifie pas le DSI actuel. COO, DSI groupe, responsable data/ML, rattachement TMS et transferts Boréal restent inconnus. [Gouvernance STG](https://www.stg.fr/qui-sommes-nous/) ; [communiqué 2018](https://www.stg.fr/une-nouvelle-gouvernance-pour-stg/) ; [CV daté Buc](https://www.doyoubuzz.com/buc-laurent/cv/jobs/stg-societe-des-transports-gautier).

| Question qui peut inverser le diagnostic | Recherche suivante / propriétaire présumé | Condition d'arrêt |
|---|---|---|
| Quel CA, marge, flotte et personnel transport seuls après Boréal ? | Comptes 2025/2026 pro forma et opération de cession ; direction financière | Périmètre réconcilié et date effective documentée |
| Quelles données TMS, télématique, parc et contrats sont détenues/licenciées par STG après la séparation ? | Cartographie DSI/opérations, droits de données, protocole Ekolis | Deux flux pilotes traçables avec baseline et accès autorisé |
| Quel est le premier goulot de marge : densité, qualité/froid, énergie ou prix ? | P&L par service/lane/client, OTIF et incidents 12–24 mois ; COO/exploitation | Sensibilité économique comparable et dépendances explicites |
| Qui pilote les opérations, le SI et la data/ML en septembre 2026 ? | Sources corporate puis LinkedIn public, intitulé et dates ; RH | Titre et périmètre vérifiés ou inconnu maintenu |
| Existe-t-il déjà un moteur de planification/optimisation, et quelles décisions restent manuelles ? | Démonstration TMS/dispatch et historique de plans | Baseline mesurée ; aucun double compte de l'existant |

### Contrôle de proportionnalité de la preuve

Conserver URL/date/périmètre et un extrait exact **pour les constats qui changent le périmètre, la priorité ou la recommandation** : séparation Boréal, capacités déjà installées, finances, rôle actuel et résultats de pilote. Les repères sectoriels et descriptions d'offre peuvent rester dans un registre léger ; les hypothèses restent explicitement conditionnelles. Le paquet formel viendra après collecte des originaux et choix des claims décisifs. Ce choix évite de produire des scores de preuve apparents sur des détails sans conséquence.
