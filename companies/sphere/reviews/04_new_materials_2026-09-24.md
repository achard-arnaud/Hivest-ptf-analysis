# Sphere — reprise des nouveaux matériaux (24 septembre 2026)

**Statut : RESEARCH ; intake secondaire, non preuve primaire.** Ce paquet regroupe dix DOCX, un classeur et une mind map NotebookLM fournis par l'utilisateur. Il est archivé dans le dépôt comme matériaux de travail, sans promouvoir ses assertions dans `claims.json`. Les deux Corporate Profile, les deux versions de la chaîne de valeur et deux profils stratégiques comportent des passages doublons ; leur multiplicité ne constitue pas une corroboration indépendante. `C8` est une autocritique de ce même corpus, pas une validation extérieure. Les citations numériques internes aux fichiers renvoient parfois à Wikipédia, Craft, à un autre rapport généré ou à une page sans passage contrôlable. Les annexes de sources ne contiennent pas les originaux.

## Ce qui améliore réellement le diagnostic

| Apport | Décision d'intégration | Vérification attendue |
|---|---|---|
| Chaîne de valeur décomposée : achats matières → extrusion/qualité → distribution, appuyée par R&D, SI et planification | Reprendre comme **carte d'hypothèses** et matrice de questions, sans reprendre les qualificatifs `Differentiating` ou les gains chiffrés | Marges par famille, variance matière, rebuts, service, coûts logistiques et substituts concurrents |
| Ishikawa 6M : méthodes, machines, main-d'œuvre, matière/données, milieu, mesure | Employer comme guide d'entretiens et de collecte par site ; il ne mesure pas à lui seul la maturité IA | Inventaire ERP/MES, traçabilité lots et nomenclatures, mesures de qualité, owners et baselines |
| S&OP Italie et possibilité d'une couche ML incrémentale | Confirme **la question** du gain supplémentaire de prévision/optimisation après S&OP ; le cas Valtus déjà présent demeure la preuve à lire | Résultats avant/après, périmètre Virosac, causalité, coûts et comparateur sans ML |
| Registre d'entretiens C7 | Ajouter les questions COO/DSI, gouvernance MDM, indexation matière, historique SKU/site et processus de mesure | Réponse nominative et mandat daté ; contrat, série et propriétaire de chaque baseline |
| Trois mécanismes économiques | Comparer marge matière/prix, rendement qualité et stocks/service/BFR dans une même unité d'analyse | Baselines sur périodes et périmètres compatibles ; absence de double compte |

## Bloquants avant toute promotion factuelle ou chiffrée

1. Le classeur juxtapose **Sarantis** (295,28 M€ en 2026), la holding juridique GROUPE SPHERE (effectif 0 / capitaux propres ~10,1 M€) et des indicateurs consolidés industriels. Ce n'est pas une série groupe ; ne calculer ni croissance, ni bilan consolidé, ni ratio d'endettement à partir de ces lignes.
2. Le document « Priorités IA » pose sans original vérifiable : décalage contractuel 90–180 jours, sensibilité EBITDA de 350–450 points de base pour +10 % de résine, MAPE 35 %, OTIF 91,5 %, stock « 68 jours », objectif 45 jours et libération de 35–50 M€. **Ces valeurs restent hypothèses à tester**, jamais baseline ni cible approuvée. Le rapport 2024 antérieur indique 167,6 M€ de stock de clôture ; ce montant ne prouve aucun DIO moyen. Une baisse de stock et une économie de coût de portage sont deux effets distincts.
3. Les parts de GMS, public et professionnel données dans les nouveaux documents mélangent **canaux, familles de produits et négoce**. Les 58/26/16 et 40/26/18/16 ne remplacent pas les catégories de produits 38/20/20 du rapport 2024 ; la classification BCG exige croissance du marché et part relative, toujours absentes.
4. La mention « 58 % Scope 3 » ne mesure pas la part des résines dans les achats ni le coût de revient. Les 70 % de ventes recyclées ou biosourcées ne décrivent pas les volumes ni le mix d'achats. Les bénéfices « down-gauging −30 % », « 200 brevets », surcoûts Bioplast et premium prix demandent source, référence produit, période et périmètre.
5. `C4`, `C5` et `C7` convertissent une **recherche négative** en poste vacant, absence d'équipe data/ML, absence de MES/Historian et « Orchestrator sous-exploité ». Conserver `COO groupe = unknown`, `DSI groupe = unknown`, `équipe ML = unknown`, `usage Orchestrator = unknown`, `MES par site = unknown`. Ni l'absence publique ni la capacité de l'éditeur ne prouvent l'état installé.
6. `C7` dit que l'absence de DSI est un « dead end » tout en demandant ensuite sa confirmation. `C8` dit que 220 M€ Italie représentent ~22 % de 814 M€ : l'arithmétique donne **27,0 %**. La proportion, la date et la consolidation doivent être réconciliées. Les dates de Polyex doivent être vérifiées dans la source transactionnelle ; acquisition annoncée réalisée ne prouve ni intégration ni synergie.
7. Les intitulés « EBITDA 77,945 M€ » et « EBIT » sont confondus dans le classeur. La qualification « pro forma » accolée aux 814 M€ de 2025 dans les nouveaux rapports n'est pas garantie par le seul communiqué cité ; reprendre son libellé exact dans la source primaire.

## Hypothèses de décision révisées

- **A — marge matière/prix** : analyser clauses et indices par matière/client, puis séparer risque temporel de pertes permanentes. Commencer par calcul explicable et simulation contractuelle ; ML seulement si l'erreur prédictive change une décision.
- **B — rendement industriel** : auditer variabilité du recyclé, taux de rebut, surgrammage, qualité et consommation par ligne. Vision/process ML seulement avec données disponibles et baseline de contrôle statistique.
- **C — S&OP/cash** : en Italie, mesurer les gains déjà obtenus sans IA et tester l'amélioration incrémentale de la prévision puis de l'optimisation sous contraintes. Recalculer stock moyen, DIO, OTIF, ruptures et cash ; aucune promesse de 35–50 M€.
- **D — gouvernance** : demander qui possède la décision transverse, les données et les interfaces JDE par site. Ne pas prescrire une vacance ou une architecture groupe avant cartographie.

**Effet sur les trois pages :** page 1 expose uniquement les chiffres et périmètres vérifiés ainsi que la thèse concurrentielle conditionnelle ; page 2 utilise la chaîne de valeur comme structure et montre trois zones de mesure ; page 3 compare les pilotes A/B/C, prérequis et questions de décision. Aucune note de maturité « faible » ou « partielle » n'est calculable avec ces seuls fichiers. Les annexes détaillées demeurent dans cette revue, sans gonfler les trois pages.

**Prochaines sources ciblées :** rapport consolidé 2024 original (pages finance et segmentation), communiqué corporate Polyex, cas Valtus Italie, organigramme officiel, cartographie SI/OT par site, contrats d'indexation échantillonnés et tableaux mensuels d'exploitation. Promouvoir chaque claim décisif uniquement après contrôle du fragment source, date et périmètre. La mind map est une vue de navigation : ses feuilles sont des questions, pas des preuves.
