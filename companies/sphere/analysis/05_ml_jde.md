# Sphere — JDE, stratégie ML et BFR : vérification technique

Date de consultation : 23 septembre 2026. Statut : recherche externe ; aucune preuve nouvelle de déploiement IA chez Sphere. Les recommandations ci-dessous sont des hypothèses de travail, pas des capacités installées.

## Décision

JDE constitue une voie d'intégration possible, sous réserve de vérifier l'édition, les versions, le périmètre des filiales, AIS, les droits et les interfaces réellement exploitées. La stratégie ML doit partir des décisions industrielles et du cash, non du catalogue Oracle. L'existence d'un ERP JDE ne démontre ni Orchestrator installé, ni OCI souscrit, ni une équipe ML opérationnelle.

## Factcheck du texte fourni

| Proposition | Conclusion et correction | Source |
|---|---|---|
| Oracle aurait décidé de ne pas réécrire le cœur JDE pour y injecter l'IA | Non établi sous cette formulation absolue. Oracle décrit une stratégie d'augmentation par les capacités de sa pile technologique. Ne pas attribuer une intention définitive ni promettre une absence d'évolution du cœur. | JDE-01, JDE-04 |
| Orchestrator expose des services REST et appelle des API externes | Confirmé : intégration entrante et sortante, avec sécurité applicative, données et objets utilisateurs. Une API disponible ne garantit pas la compatibilité fonctionnelle de tout modèle. | JDE-02 |
| Release 26 serait indispensable à l'IA | Faux comme règle générale. La connexion/authentification OCI AI documentée commence à Release 24, Tools 9.2.8.2. Les versions certifiées restent à contrôler pour le scénario retenu. | JDE-01 |
| OCI impose de migrer l'ERP dans le cloud | Faux : un JDE sur site peut se connecter aux services OCI ; prévoir tests de latence et configuration réseau. L'abonnement IA est distinct de la licence JDE. | JDE-01 |
| OCR et réconciliation complète à trois voies seraient une IA native prête à activer | À décomposer : Oracle documente un parcours d'intégration Document Understanding ; le rapprochement à trois voies est également une fonction Procurement classique. Ni zéro exception ni automatisation totale ne sont établis. | JDE-04, JDE-06 |
| La vision sur composants serait une invention alternative non proposée par Oracle | Contredit : le catalogue officiel inclut explicitement un parcours d'inspection de composants avec OCI AI Vision. Un tutoriel n'est pas une preuve d'adoption client à grande échelle. | JDE-04 |
| Prévision et maintenance prédictive seraient installées avec JDE | Non établi. Considérer des solutions à concevoir, alimenter et évaluer, sans confondre plateforme accessible et modèle métier exploité. | JDE-04 |
| Release 26 livrerait nécessairement des copilotes ou agents métier natifs | Non établi par les notes consultées. La release comprend notamment automatisation, tableaux de bord et améliorations techniques. Un guide Oracle de chatbot CNC existait déjà en 2022, explicitement comme construction spécifique, hors fonctionnalité généralement disponible du produit. | JDE-05, JDE-07 |
| Tout LLM serait interchangeable et supporté par Oracle | Connectivité REST possible en principe ; authentification, formats, politiques et support restent à qualifier. Oracle précise que son support IA porte sur ses services ; le support tiers relève de ces fournisseurs. ChatGPT ne doit pas être qualifié d'open source. | JDE-01, JDE-02 |

## Les dix exemples « terrain » : statut à conserver

La liste fournie ne constitue pas dix références de production vérifiées. Les liens de domaines génériques ne prouvent ni client, ni date, ni architecture, ni gain. Aucun cas client nommé n'a été établi dans cette collecte bornée.

| Exemple | Classification retenue |
|---|---|
| Génération/débogage d'orchestrations par LLM | Hypothèse de développement assisté ; vérifier formats, tests et droits ; ne pas promettre élimination des hallucinations. |
| CNC prédictif et auto-réparation | Guide chatbot CNC avéré ; détection prédictive et redémarrage autonome restent des extensions non démontrées. |
| NRT générés par IA | Hypothèse ; comparaison avec tests déterministes et jeux de référence indispensable. |
| Vision sur quai et blocage réception | Capacité générale d'intégration vision documentée ; scénario quai/blocage non démontré chez un client identifié. |
| Pricing piloté par sentiment web | Hypothèse fragile pour du B2B industriel ; pertinence des signaux et causalité à démontrer. |
| Tournées par apprentissage par renforcement | Hypothèse ; optimisation mathématique sous contraintes comme référence initiale. |
| Contrats et mise à jour des modules | Hypothèse ; extraction, interprétation et écriture ERP doivent être séparées et approuvées. |
| ESG fournisseur et blocage automatique | Hypothèse ; classification documentaire ne démontre ni conformité ni matérialité du risque. |
| CSV vers graphique en langage naturel | Analyse assistée plausible ; ce n'est pas nécessairement du RAG ni un tableau de bord gouverné connecté. |
| Agent de recouvrement | Hypothèse ; distinguer priorisation, brouillon de relance, envoi, promesse de paiement et écriture comptable. |

## Stratégie ML proposée pour Sphere — hypothèses priorisées

| Décision métier | Méthode candidate et baseline | Données / test requis | Valeur et indicateurs |
|---|---|---|---|
| Prévoir demande et recalibrer stock de sécurité | ML de prévision probabiliste contre saisonnier naïf, règles ABC/XYZ et planification actuelle | SKU/site/client, ruptures, promotions, délais ; backtest temporel sans fuite | BFR et service : DIO, stock excédentaire, biais, coût de rupture, OTIF ; ne pas optimiser seulement l'erreur moyenne |
| Contrôler stock physique, réception et conformité visuelle | Vision contre scan/code-barres, pesée et contrôle humain | Images réelles représentatives, labels défauts, éclairage et traçabilité lot | Fiabilité d'inventaire, faux rejets, défauts échappés ; effet BFR indirect, à mesurer séparément |
| Prioriser créances et litiges | Score de retard/récouvrabilité + règles comptables ; GenAI pour brouillons contrôlés | Balance âgée, échéances, litiges, encaissements, actions passées ; test par cohortes | DSO, créances échues, délai résolution, cash effectivement encaissé ; ne pas compter le montant total des créances comme gain |
| Proposer prix et indexations | Estimation d'élasticité si identifiable, détection de fuite de marge, simulation ; baseline coût-plus et clauses existantes | Prix nets, remises, volumes, coût résine, contrats, concurrence comparable | Marge contributive, délai de répercussion, taux de gain, rétention ; décision commerciale humaine |
| Choisir MOQ, lots et fréquence de livraison | Optimisation sous contraintes, éventuellement alimentée par prévisions ML ; pas de ML obligatoire | Capacités, temps de changement, transport, minimums contractuels, service, stockage | Coût total rendu, stock, rendement, charge et OTIF ; éviter les économies transport annulées par le surstock |
| Réduire rebuts et variabilité extrusion | SPC/règles comme baseline, puis détection d'anomalies et modèles supervisés | MES/capteurs, lots matière, recettes, défauts, temps ; validation entre lignes | Rendement matière, rebut, stabilité qualité ; recommandation avant boucle fermée |

Le BFR doit séparer stocks, clients et fournisseurs : une baisse de stock libère du cash une fois ; les coûts de possession évités sont récurrents. Une accélération d'encaissement n'est pas du chiffre d'affaires nouveau. Ne pas additionner cash libéré, baisse DSO et amélioration du BFR comme trois gains distincts. Le diagnostic financier doit valider les bases comptables et la saisonnalité.

## Prérequis et gates proposés (contrat de diagnostic)

1. **État installé** : édition/version Applications, Tools, AIS, Orchestrator, modules, filiales, interfaces, hébergement et contrats. Chaque champ absent = inconnu.
2. **Données** : owner, granularité, couverture historique, qualité, droits, latence, disponibilité des labels et définitions KPI.
3. **Évaluation** : baseline non-IA ; découpage temporel ; coûts des faux positifs/négatifs ; test sur site pilote puis transfert ; conditions d'arrêt.
4. **Exploitation** : responsabilités COO/DSI/data, surveillance dérive, réentraînement, disponibilité, support et coût complet.
5. **Action** : lecture seule puis recommandation ; validation humaine pour prix, crédit, réception et contrats ; journal, reprise et idempotence avant écriture ERP. Ne pas déduire d'un code de table le droit de modifier directement la base.
6. **Généralisation** : déploiement prouvé séparément des démonstrations ; aucune promesse de ROI transposée d'un tutoriel fournisseur.

## Registre primaire et locateurs

Toutes les sources sont Oracle. Dates de publication renseignées seulement lorsqu'explicites. Les IDs web permettent le contrôle dans la session ; les URL assurent la portabilité.

| ID | Publication / portée | URL et référence de consultation |
|---|---|---|
| JDE-01 | FAQ janvier 2025 v1 ; pp.4–6 : versions, licence, site, support tiers | https://www.oracle.com/webfolder/technetwork/tutorials/jdedwards/FAQ/FAQ-Oracle-AI-JDE.pdf — turn810110view0 |
| JDE-02 | Documentation Orchestrator actuelle, date non indiquée ; intégration et sécurité | https://docs.oracle.com/en/applications/jd-edwards/cross-product/9.2/eotos/jd-edwards-enterpriseone-orchestrator-overview.html — turn116892search2 ; https://docs.oracle.com/cd/E84502_01/learnjde/orchestrator-integration.html — turn116892search1 |
| JDE-03 | Technical Brief janvier 2025 v1 ; exemple notes de frais via extraction de reçus, pp.4–11 | https://www.oracle.com/webfolder/technetwork/tutorials/jdedwards/White%20Papers/TechBrief-OCI-Services-with-JDE.pdf — turn156026view0 |
| JDE-04 | Catalogue LearnJDE actuel, non daté ; parcours de formation, pas preuves clients | https://docs.oracle.com/cd/E84502_01/learnjde/jde-ai.html — turn156026view1 |
| JDE-05 | Release 26, octobre 2025 ; Applications Update 26 / Tools 9.2.26 | https://docs.oracle.com/cd/E84502_01/learnjde/release26.html — turn810110view1 |
| JDE-06 | Documentation Procurement 9.2, non datée ; fonction de rapprochement | https://docs.oracle.com/en/applications/jd-edwards/supply-management/9.2/eoapr/understanding-voucher-creation.html — turn156026search0 |
| JDE-07 | Technical Brief décembre 2022 v1, pp.4–6 ; chatbot CNC construit spécifiquement | https://www.oracle.com/webfolder/technetwork/tutorials/jdedwards/White%20Papers/ChatbotforCNCAdministrationUsingServerManager_TechBrief.pdf — turn101988view0 |

### Questions qui déclenchent la prochaine recherche

- Quelle édition JDE et quel parc de versions chez Sphere ? Source attendue : DSI/inventaire applicatif, pas un catalogue Oracle.
- Quel gisement cash par stock, créances et litiges ? Source attendue : finance interne avec périmètre et dates comparables.
- Quels modèles et owners existent réellement ? Source attendue : entretiens, jobs/profils professionnels recoupés, inventaire des modèles et projets.
- Quelle amélioration dépasse les baselines ? Source attendue : historique nettoyé puis backtest et pilote contrôlé.
