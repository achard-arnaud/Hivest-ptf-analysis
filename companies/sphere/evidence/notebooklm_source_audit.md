# Sources évoquées par les rapports NotebookLM — audit d'éligibilité

Date : 24 septembre 2026. Corpus : dix DOCX, classeur XLSX et mind map remis par l'utilisateur. Les rapports ne contiennent **pas** d'export de la bibliothèque des sources du notebook. Un seul DOCX contient un URL explicite (communiqué Hivest 2024). Le classeur contient une liste de titres, mais pas des URL ni des fragments exacts. Les nombres entre crochets et les identifiants `S-NLM` sont des références internes **non résolubles** ici. « Cité » ne veut pas dire « consulté par NotebookLM » ; l'inventaire exhaustif des sources chargées n'est pas reconstructible.

## Sources candidates retrouvées et politique d'usage

| Source mentionnée / retrouvée | Type et accès | Éligibilité Sphere | Limite |
|---|---|---|---|
| Hivest, reconfiguration du capital, 24/10/2024 — https://hivestcapital.com/en/hivest-capital-partners-leads-the-capital-reconfiguration-of-groupe-sphere-the-european-leader-in-sustainable-household-packaging/ | Communiqué primaire, URL explicite C7 | Oui : accord majoritaire, co-investisseurs, chiffres et stratégie **datés 2023/2024** | Accord annoncé ≠ close légal ; ~70 % des **ventes**, pas des achats |
| Hivest / Sphere, Polyex, 07–11/09/2026 — https://www.sphere.eu/fr/le-groupe-sphere-developpe-ses-activites-sur-le-marche-du-film-industriel-en-rachetant-la-societe-polyex/ ; https://hivestcapital.com/le-groupe-sphere-soutenu-par-hivest-capital-partners-se-developpe-sur-le-marche-du-film-industriel-avec-lacquisition-de-polyex/ | Communiqués primaires, même opération/origine | Oui : acquisition annoncée réalisée, ≈814 M€ **CA 2025 publié par communiqué**, 18 sites, >1 800 salariés | Ne pas qualifier 814 M€ de « pro forma » sans source ; Polyex n'est pas intégré dans ce CA 2025 par simple lecture |
| Sphere, SPHERE PRO, 14/04/2026 — https://www.sphere.eu/fr/le-groupe-sphere-presente-au-salon-interclean-2026-sa-nouvelle-division-europeenne-sphere-pro/ | Communiqué primaire | Oui : division et >4 000 références | Ne prouve ni revenu, ni marge, ni MDM opérationnel |
| Valtus, transformation italienne, 10/07/2026 — https://www.valtus.fr/blog/2026/07/10/groupe-sphere-structurer-et-transformer-la-filiale-italienne-du-leader-europeen-des-emballages-menagers/ | Cas client du prestataire ; témoignage direct mais promotionnel | Oui : S&OP et routines de stocks **Italie** | Pas de déploiement groupe, gain quantifié, IA ou causalité ML ; 220 M€ / ≈22 % à réconcilier |
| Sphere, rapport annuel 2024 — copie https://uploads1.craft.co/uploads/unified_record/source/document/2165394/f71eb45b0ee203cf.pdf | Document émis par le groupe, hébergement tiers | Conditionnel : chiffres et catégories de l'exercice 2024, après contrôle de page et de définition | Conserver 2024 séparé de 2025 ; aucune extrapolation organique ; original intégral non archivé dans le dossier |
| Sphere, site « Nous sommes » — https://www.sphere.eu/fr/nous-sommes/ | Déclaration primaire évolutive | Oui pour offre et présentation datée à la consultation | Pas une ventilation actuelle et auditée par segment ; contrôler chaque chiffre à sa date |
| Sphere, innovations et RSE 2024 / bilan carbone 2025 — https://www.sphere.eu/fr/ | Sources corporate à retrouver par page exacte | Conditionnel par affirmation technique/environnementale | Brevets, composition, émissions et produits exigent périmètre et page ; pas de premium prix inféré |
| Annuaire des entreprises / Pappers, GROUPE SPHERE 931299564 et SPHERE 306591249 | Registres juridiques à retrouver par SIREN | Oui pour mandataires et identités juridiques datés | Holding ≠ périmètre consolidé industriel ; capitaux propres de holding ≠ capital du groupe |
| August Debouzy, opération Polyex | Conseil de transaction, source secondaire proche | Corroboration du périmètre de l'opération seulement | Une date de publication n'est pas forcément la date de closing ; ne pas déduire les synergies |
| Wikipédia, Craft (résumé), Busyplace, ContactOut, LinkedIn indexé | Encyclopédie, agrégateurs, profils | Orientation de recherche uniquement ; titre LinkedIn à revérifier | Ne prouvent pas comptes groupe, rôle COO/DSI groupe, vacance, capacité ML ou mise en production |
| Sarantis / Trading Economics / JD Edwards Wikipédia | Autres entreprises ou éditeur | **Non éligibles aux faits Sphere** | Sarantis 295,28 M€ du classeur n'est pas un chiffre Sphere ; fonctionnalités JDE ≠ installation Sphere |
| « Rapport de cadrage », « Audit stratégique SPHERE », « HANDOFF_CODEX », autres sorties NotebookLM | Synthèses dérivées, origine non disponible | Hypothèses et questions seulement | Éviter la citation circulaire ; ne pas promouvoir MAPE, OTIF, DIO, pass-through ou BFR cible |

**Règle de promotion :** seules les pages primaires ci-dessus ou le rapport annuel original peuvent entrer comme source d'un fait matériel, avec passage, date, unité et périmètre. Le cas Valtus rapporte une transformation Italie, pas une efficacité IA. Un concurrent peut servir au contexte concurrentiel seulement après vérification sur son site ou ses comptes ; ses chiffres ne deviennent jamais ceux de Sphere. Une recherche négative conserve `unknown`, jamais « vacant/absent ». Ne pas ajouter à `claims.json` de donnée NotebookLM non retracée.

## Questions de recherche déclenchées

1. Obtenir l'export des sources NotebookLM pour lever les renvois numérotés ; tant qu'il manque, ne pas présenter cet audit comme liste exhaustive.
2. Réconcilier 2024 consolidé, communiqué 2025 et acquisitions 2024–2026 ; séparer CA, EBITDA, EBIT, BFR d'exploitation et stocks de clôture.
3. Reconstituer la ventilation produit 2024 à partir du tableau original, sans la confondre avec canaux GMS/professionnels/public.
4. Demander baselines S&OP Italie et groupe, données ERP/MES/site, gouvernance data, COO/DSI et contrats d'indexation avant de chiffrer les pilotes.

## Addendum — registre `S-NLM-001` à `S-NLM-030` reçu

Le registre fourni après cette première revue identifie **30 entrées**, ce qui résout la liste des titres mais pas la disponibilité des 30 documents ni les passages cités. Il est conservé sans modification dans `intake/notebooklm_register_supplied_2026-09-24.md`. La nomenclature du registre est celle du notebook ; elle ne remplace pas les IDs `S02`, `S03`, etc. du dossier Sphere.

| Traitement | IDs du registre | Décision |
|---|---|---|
| Primaires entreprise/sponsor ou registre public | 002, 004, 006, 007, 008, 009, 011, 018, 023, 025, 029, 030 | **Éligibles à vérification ciblée** sur page/PDF original, avec date et périmètre. 002 est un co-investisseur, 004 un conseil de transaction, 006 un catalogue commercial ancien. 005 (Busyplace) ne devient pas source légale A par libellé seul. |
| Témoignage opérationnel | 010 | Éligible pour l'Italie et l'action S&OP rapportée, sans extrapolation groupe ou attribution de ROI causal. |
| Études et docs génériques | 012, 014, 015, 017, 019, 021 | Contextualisation technique/sectorielle seulement ; préférer documentation Oracle et texte UE officiels pour JDE et PPWR. Ne prouvent aucun déploiement Sphere. |
| Pistes secondaires | 005, 013, 016, 020, 026, 028 | Recherche de source primaire avant toute promotion. L'inscription à un club Oracle ne démontre pas la version, les modules ni l'usage d'Orchestrator. |
| Hors périmètre | 024, 027 | Sarantis est un pair éventuel, jamais une donnée financière Sphere ; Sphere Informatique est un homonyme exclu. |
| Instructions et analyses internes | 001, 003, 022 | **Non éligibles comme preuves indépendantes**, même si le registre les note A. À utiliser pour questions, méthodes et hypothèses. |

**Erreurs internes au registre :** `S-NLM-023` est décrit comme bilan carbone/SBTi mais rapproché ensuite de l'opération Polyex ; il ne peut pas servir aux deux. `S-NLM-030` appelle les 814 M€ « pro forma », tandis que le communiqué Hivest indique simplement un CA **réalisé en 2025** ; enlever l'étiquette pro forma. `S-NLM-011` avance ≈76 % de participation alors que le communiqué Hivest vérifié indique une **participation majoritaire** sans pourcentage. Le 220 M€ Italie et « 22 % » ne se réconcilient pas avec 814 M€ (≈27 %) ; périodes/périmètres à clarifier. Les codes A–E du registre mêlent autorité de source et utilité méthodologique : la qualification du dossier prime.
