# VMI-Jokon — audit du complément Deep Research/NotebookLM, 24/09/2026

**Entrée :** rapport fourni « Diagnostic Stratégique et Plan de Transformation IA/Data : VMI-Jokon » (`Texte collé(20260924-093159).txt`, SHA-256 `463ba715760149c528bbd7375d37d5301c854e7dcf02eba879f789b14edf3abd`). Synthèse dérivée, **pas source primaire ni capture originale**. Les deux autres briefs VMI-Jokon et Aurightec de la même remise normalisent aux briefs déjà intégrés, sans nouveaux claims. Le brief Agora est routé dans son dossier.

## Claims promus après retour aux sources

| ID | Claim vérifié, statut et périmètre | Source, fragment/localisation, limite |
|---|---|---|
| VC11 | **Fait — VM INDUSTRIES, société française VMI uniquement :** CA 2025 33 616 133 € contre 28 785 291 € en 2024 ; résultat d'exploitation 3 068 096 € contre 1 255 460 €. | [Comptes sociaux 2025 audités, PwC](https://www.pappers.fr/entreprise/vm-industries-517864757/comptes/VM%20INDUSTRIES%20-%20Comptes%20sociaux%202025%2017-06-2026.pdf), p. 24 (imprimée 7/28), lignes « montant net du chiffre d'affaires » et « résultat d'exploitation » ; opinion sans réserve p. 18–19. Dépôt 17/06/2026, consultation 24/09/2026. **Pas comptes consolidés du groupe**. |
| VC12 | **Fait — VM INDUSTRIES :** achats de matières et approvisionnements 19 075 628 € en 2025 ; export 27 672 941 € de CA. | Même comptes, p. 24 et p. 38 (ventilation France/étranger). L'achat de matières ne mesure pas le cuivre ; aucun pass-through établi. |
| VC13 | **Fait — VM INDUSTRIES :** stocks bruts 3 153 239 € au 31/12/2025, dont matières 1 803 479 € et finis 1 319 140 € ; dépréciation 67 849 €. | Même comptes, p. 34, détail de l'annexe ; instantané comptable, sans ancienneté SKU ni potentiel de réduction. |
| VC14 | **Fait — VM INDUSTRIES :** encours clients 7 376 922 € et dettes fournisseurs 4 143 985 € au bilan 2025 ; emprunts bancaires 1 448 571 €. | Même comptes, p. 22–23. Les agrégats Pappers « BFR 4,4 M€ / 47,8 j » sont calculés avec conventions à expliciter ; ne les transférer ni à Jokon ni au groupe. |
| VC15 | **Fait — aval allemand, pas Jokon :** camping-cars neufs août 2026 4 287, -22,3 % sur août 2025 ; janvier–août 54 405, -5,1 % ; juin–août -16,5 %. | [CIVD, statistiques courantes](https://www.civd.de/artikel/aktuelle-neuzulassungszahlen/), tableau « Reisemobile », consulté 24/09/2026. Un mois n'est ni l'été ni l'année ; la page évolue, revalider avant gel. |
| VC16 | **Fait — pair Aspöck, non Jokon :** gamme LED Ecoround pour plusieurs types de véhicules ; site affiche 265 M€ de CA FY 2025/26 et 1 550 salariés. | [Aspöck, page Ecoround](https://www.aspoeck.com/en/news/aspoeck_ecoround_30749), fiche datée 09/07/2024, encart « Facts » dynamique consulté 24/09/2026. Périmètre et période fiscale non comparables au CA groupe VMI-Jokon. Une page produit n'établit aucune part de marché. |
| VC17 | **Fait — Jokon :** Ludovic Weiss est « directeur usine Bonn / GM Jokon FR » et Sven Konrad « direction informatique ». | [Jokon, contacts](https://www.jokon.de/fr/contacter/), sections départements spécialisés, page sans date, consultée 24/09/2026. Hivest qualifie aussi Weiss de COO Jokon (V03). Konrad est IT **Jokon**, pas DSI groupe ; aucun effectif data/ML déduit. |
| VC18 | **Fait réglementaire limité :** R148 concerne les dispositifs de signalisation lumineuse ; R149 les dispositifs d'éclairage de la route. | [UNECE R148](https://unece.org/transport/documents/2021/05/standards/un-regulation-no-148-light-signalling-devices-lsd) et [R149](https://unece.org/transport/documents/2021/05/standards/un-regulation-no-149-road-illumination-devices-rid), textes de 2021. L'application exacte aux références Jokon et une obligation de renouvellement 2026 ne sont **pas** établies. |

**Calcul transparent :** la croissance du CA social VM INDUSTRIES 2025/2024 est `(33 616 133 / 28 785 291) - 1 = 16,78 %`. Le taux EBE 12,5 % affiché par Pappers est un agrégat de sa plateforme, pas une ligne certifiée « EBITDA » du compte de résultat ; le résultat d'exploitation 3,068 M€ est certifié. Les achats matière ~56,7 % du CA ne signifient pas « cuivre 40–60 % du coût matériel ». Stocks en hausse en valeur brute vs 2024 selon l'annexe, mais ratio stocks/CA dépend du mode de calcul.

## Claims non promus / corrections obligatoires

| Énoncé du complément | Verdict et test |
|---|---|
| « cuivre 40–60 % » à partir d'une étude du faisceau malaisien | **Rejeté pour VMI** : autre produit/pays ; extraire nomenclatures et clauses réelles d'indexation avant pricing/hedging. Le PDF 2025 mentionne une hausse générale des matières/transport dans les événements post-clôture, sans isoler cuivre ni indexation. |
| « -22,3 % l'été 2026 » et « contraction pleine » | **Corrigé** par VC15 : août -22,3 %, juin–août -16,5 %, YTD -5,1 %. L'exposition de Jokon par client reste inconnue. |
| « réglementation R148/149 impose un renouvellement du catalogue Jokon » | **Non établi** : identifier dispositifs homologués, anciennes approbations, dispositions transitoires et calendrier produit avant d'en faire un driver urgent. |
| « SI en silos, absence critique de DSI/data/IA, maturité FAIBLE » | **Unknown** : une page publique ne prouve ni absence ni niveau. VC17 montre même un responsable IT Jokon ; groupe/ERP/ML restent à enquêter. |
| « vision CNN/YOLO >95 %, zéro PPM, goulot éliminé » | **Non transférable** : benchmark vendeur ou autre expérience ; vérifier images, taux de défaut par classe, faux rejets, cadence et comparaison vision classique/SPC/inspection existante. |
| « Aspöck 265 M€ donc Jokon niche » ; Hella éclairage automobile proxy marge | **Inférence faible** : gamme et scopes différents ; définir un panel de pairs loisirs/signalisations et la taille de chaque sous-marché. |
| « BFR 4,4 M€ groupe, covenants menacés, VMI finance Jokon » | **Rejeté** : BFR Pappers est VMI société seule ; pas de comptes consolidés, flux intra-groupe ni covenants disponibles. |
| « red_team: SURVIVES_RED_TEAM » du YAML fourni | **Rejeté** : la couverture y est vide et plusieurs claims sont contredits ci-dessus ; aucune revue du dépôt ni bundle v0.2. |

## Ce que la nouvelle preuve change dans le business case

VC11–VC14 matérialisent **les ordres de grandeur de VMI**, pas un rendement IA : ~33,6 M€ de CA, ~19,1 M€ d'achats matières, ~3,15 M€ de stocks bruts et ~3,07 M€ de résultat d'exploitation. L'angle court terme à tester est la discipline matière/stock et qualité ; la seule taille de la ligne P&L ne démontre aucun gaspillage récupérable. VC15 rend plausible un stress de demande dans le loisir allemand, sans quantifier l'effet Jokon. VC17 identifie un owner IT de filiale à interviewer. Le comparatif Aspöck (VC16) donne un concurrent direct **pour l'offre éclairage**, sans calcul de part relative. Face au test de cohérence, la thèse « marge VMI finance les acquisitions » ne survit pas sans comptes consolidés et dette d'acquisition.

**Gates restants :** PDF original audité lu en ligne mais non archivé immuablement hors code ; captures et hashes manquants ; chiffres Jokon et consolidation absents ; baselines qualité/SKU/contrats absentes ; pas de bundle v0.2 `package.json` + `strategic_context.json`, ni trois revues/human GO_DRAFT. Décision proposée : **RESEARCH_TARGETED**, avec possibilité de brouillon Claude explicitement provisoire.
