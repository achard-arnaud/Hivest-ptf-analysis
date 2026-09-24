# VMI-Jokon — recherche business case, 24 septembre 2026

**État : RESEARCH ; cutoff 23/09/2026.** Complément financier et red-team dans [audit du rapport fourni](audit_complement_2026-09-24.md) ; ses claims VC11–VC18 corrigent et précisent cette première passe. Le [brief ToT fourni](intake_brief_tot_2026-09-24.md) est une carte de questions, non un rapport de preuves. Les sources ci-dessous ont été lues en ligne ; aucune archive originale ni empreinte de capture complète n'est prétendue. Pas de ROI ni de maturité chiffrée.

## Registre de sources et assertions

| ID | Source primaire, date de publication / consultation, locator | Claim, scope et limite |
|---|---|---|
| V01 | [Hivest, annonce d'acquisition](https://hivestcapital.com/en/hivest-capital-partners-acquires-vmi-jokon-group-alongside-its-management-team/), 10/09/2026 / 24/09/2026, paragraphes 1–8 | Closing 30/07/2026, Hivest majoritaire et management/Marc Laisné proche de 40 %, CA consolidé 2025 proche de 60 M€, environ 270 salariés. Source transactionnelle, chiffres non audités ici. |
| V02 | V01, paragraphes VMI et Jokon | VMI : >350 M pièces/an, conception à coût cible, labo test, câbleurs/rang 1 ; Jokon : ~3 000 références, >600 clients, développement interne, production Bonn/Folschviller, éclairage véhicules de loisirs et professionnels. Chiffres d'activité non interchangeables, pas de marge par filiale. |
| V03 | V01, paragraphes stratégie et direction | Développement produits, montée en gamme et acquisitions Europe/Amérique du Nord envisagées ; Romain Bontemps DG VMI, Martin Zavelberg DG Jokon, Ludovic Weiss COO **Jokon** sous Marc Laisné. Annonce de thèse, aucune acquisition future acquise ; COO groupe non documenté. |
| V04 | [VMI, site d'entreprise](https://www.vmi-31.com/), n.d. / 24/09/2026, «Home» | Villemur, origine Molex et intégration Jokon en 2012. Site commercial, capacités et performances à vérifier sur données internes. |
| V05 | [Jokon, site d'entreprise](https://www.jokon.de/en/english/), n.d. / 24/09/2026, «About us», «Products» | Offre de feux pour véhicules spéciaux et commerciaux ; catalogue avec systèmes LED. Présence de logos clients n'établit ni volumes ni contrats actuels. |
| V06 | [CIVD, bilan Allemagne 2025](https://www.civd.de/en/news/01-2026-caravanning-market/), janvier 2026 / 24/09/2026 | 94 134 immatriculations de véhicules de loisirs en Allemagne en 2025, -2,3 % ; CA industrie ~14,1 Md€, -6,5 %. Marché aval allemand, **pas** CA adressable de Jokon. |
| V07 | [CIVD, marché européen 2025](https://www.civd.de/en/news/01-2026-new-registrations/), janvier 2026 / 24/09/2026 | Plus de 215 000 immatriculations de véhicules de loisirs en Europe. Même organisme et collecte que V06 ; ne pas compter comme confirmation indépendante. |
| V08 | [ACEA, immatriculations voitures 2025](https://www.acea.auto/pc-registrations/new-car-registrations-1-8-in-2025-battery-electric-17-4-market-share/), 27/01/2026 / 24/09/2026 | Voitures neuves UE +1,8 %, BEV 17,4 % du marché en 2025. Demande automobile agrégée, pas volumes de contacts VMI ; impacts architecture connecteurs à valider. |
| V09 | [ACEA, véhicules commerciaux 2025](https://www.acea.auto/cv-registrations/new-commercial-vehicle-registrations-vans-8-8-trucks-6-2-buses-7-5-in-2025/), 29/01/2026 / 24/09/2026 | Vans UE -8,8 %, camions -6,2 %, bus +7,5 %. Segments partiellement adjacents à Jokon ; périmètre client non établi. |
| V10 | [Jokon, profil officiel LinkedIn](https://www.linkedin.com/company/jokongmbh), page indexée / 24/09/2026 | La société attribue à Ludovic Weiss production, logistique, achats, qualité **et IT** depuis avril 2026. Signal de mandat filiale seulement ; DSI groupe et équipe data/ML inconnus. Source à revalider sans accès restreint. |

**Chronologie :** closing le 30 juillet, communiqué Hivest daté du 10 septembre ; ne pas confondre avec l'affichage 23 septembre de la page d'accueil. V06/V07 et V08/V09 proviennent chacun d'un même organisme : pas quatre validations indépendantes du marché.

## Segments et structure du marché

Deux chaînes à ne pas fondre dans un « marché mobilité » unique. **VMI** : pièces métalliques de précision/connectivité automobile, acheteurs câbleurs et Tier-1, volumes élevés, coûts matière/outillage, homologation et qualité série, prix contractuels et dépendance des programmes OEM. **Jokon** : systèmes d'éclairage et signalisation pour loisirs, bus, remorques et agriculture, mix catalogue/OEM, engineering et conformité, assortiment long et production franco-allemande. CIVD mesure l'aval véhicules de loisirs, ACEA l'aval automobile et utilitaire ; la part de VMI/Jokon, les concurrents directement comparables, parts relatives et prix ne sont pas documentés. Les barrières IP/homologations annoncées par Hivest (V01) protègent éventuellement le prix mais leur force contractuelle reste à démontrer.

| Driver (rang provisoire) | Process → hypothèse de valeur | Test et baseline internes | Alternative/condition d'inversion |
|---|---|---|---|
| V-D1, qualité et rendement VMI | découpage/emboutissage, outillage, test → rebut/retouche et capacité ; COST_REDUCTION | ppm, FPY, rebuts € par famille/outillage, coûts garantie, goulot ; SPC et maintenance planifiée contre ML | qualité déjà excellente, défauts rares ou labels insuffisants |
| V-D2, mix et industrialisation Jokon | 3 000 références, NPI/catalogue → délai devis, obsolescence, marge SKU et BFR ; CAPITAL_PRODUCTIVITY / DIFFERENTIATION | marge par SKU/client, stock dormant, prévision par famille, taux de réutilisation design ; règle de réassort contre ML | petites séries erratiques, coûts de service élevés ou prix fermes sans prime |
| V-D3, variabilité aval et contrats | demande loisir 2025 en repli modéré Allemagne, véhicules commerciaux hétérogènes → planification capacité et service ; RISK_RESILIENCE | carnets par client et programme, OTD, changements de commandes, stocks, utilisation ; segmentation VMI/Jokon | poids des clients concernés marginal, capacité flexible, coûts entièrement répercutés |
| V-D4, intégration M&A | acquisition envisagée → standard KPI, articles, clients, qualité et reporting ; COST_AVOIDANCE / intégration | délai et coût d'intégration des cibles, schémas ERP/PLM/MES, doublons, reporting mensuel ; harmonisation sans IA d'abord | pas de deal clos ou accès insuffisant aux données de cibles |

**Priorité business ≠ facilité IA.** V-D1 peut dominer si le coût non-qualité VMI est élevé ; V-D2 si la longue traîne immobilise du cash ; V-D4 si les acquisitions se concrétisent. Ne pas additionner pièces/an, clients et références pour faire un TAM. Stock réduit = cash ponctuel, hausse de marge démontrée = EBITDA ; capacité libérée ≠ revenu sans commandes.

## Tree-of-Thought × contradiction

- **Thèse coût/qualité** : VMI gagne sur ppm et rendement ; contre-hypothèse, qualité déjà sous contrôle et prix matière répercutés.
- **Thèse différenciation/mix** : Jokon gagne sur design, délai et assortiment ; contre-hypothèse, catalogue à forte complexité et faible marge unitaire.
- **Thèse plateforme** : données communes et M&A créent économies d'échelle ; contre-hypothèse, deux chaînes sans synergies de production et M&A incertaines.

La cohérence commune est de préserver deux P&L et deux baselines, puis de mesurer les synergies centrales seulement si les flux et coûts se recoupent. Les sources publiques soutiennent le *mécanisme* et la thèse de sponsor, pas un gain démontré.

## Couverture négative et recherche ciblée

1. **Économie :** comptes VMI et Jokon 2024–2026, CA/marge par segment et client, réconciliation avec ~60 M€ consolidés, concentration, pass-through matière, cash/stock et capex. Owner CFO/Marc Laisné.
2. **Opérations :** performance lignes VMI et Jokon, coûts non-qualité, OTD, mix catalogue vs OEM, nomenclatures/outillage, cohorte SAV. Owners Romain Bontemps et Martin Zavelberg ; Ludovic Weiss pour Jokon, **pas COO groupe**.
3. **Capacité numérique :** DSI groupe inconnu ; systèmes ERP/MES/PLM, qualité des clés article/client, équipe BI/data/ML, déploiements IA, droits et validation intersites. V10 suggère une responsabilité IT de filiale sans prouver une équipe IA.
4. **Marché/position :** homologations actives, concurrents par ligne, pression prix, portefeuille de programmes, parts relatives et croissance du marché **adressable** ; BCG impossible en l'état.
5. **Intégrité :** conserver originaux et hashes hors code, fragments et claims atomiques, bundle `package.json` + `strategic_context.json` conforme v0.2, red-team et gate humain.

**Verdict : RESEARCH_TARGETED.** Les comptes audités de VM INDUSTRIES rendent l’ordre de grandeur VMI vérifiable, mais ne couvrent pas Jokon ni le groupe. Voir VC11–VC18.  Thèse VMI/Jokon pertinente mais business case financier et hiérarchie finale des use cases non validés. Claude peut préparer le texte conditionnel des trois pages, sans le présenter comme rendu final approuvé.
