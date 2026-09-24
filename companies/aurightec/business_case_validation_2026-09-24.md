# Aurightec — validation du business case, best effort

**Verdict de recherche : `REOPEN_TARGETED`.** Le problème économique est démontré **pour Tallinn** par des comptes audités : pression sur les ventes, perte nette, achats de matières dominants et investissements qualité [S-AUR-02]. La thèse de création de valeur par le pilotage sourcing–NPI–test est plausible pour le groupe ; le gain incrémental, la transférabilité Chine/Estonie/Malaisie et le ROI ne sont **pas validés**. L'IA en Chine est une déclaration circonstanciée de mise en service [S-AUR-09,10], pas une preuve auditée des gains ni un niveau de maturité du groupe. Registre et contexte : [sources](source_register_2026-09-24.md), [marché](market_context_2026-09-24.md).

## Chaîne de valeur et tests de captation

| Étape Porter | Activité observée / mécanisme candidat | Baseline, test et limite |
|---|---|---|
| Logistique amont | Achats matières 22,79 M€ Tallinn ; hub sourcing Shanghai déclaré [S-AUR-02,05,07]. | Prix BOM, ruptures, obsolescence, couverture stock ; MRP/règles et négociation vs prédiction. Contrats d'achat et répercussion à l'OEM inconnus. |
| Opérations | NPI, SMT, inspection/test ; capex Tallinn 1,09 M€ en 2025 [S-AUR-02,05,06]. | Rendement premier passage, retouches, temps de test, OEE par famille ; SPC/automatisation existante vs ML. Valeur du capex déjà réalisé à isoler. |
| Logistique aval | Livraison multi-sites annoncée [S-AUR-05,08]. | OTIF et coût expédition par programme, sans attribuer une économie groupe à Tallinn. |
| Marketing/ventes | Portefeuille multi-sectoriel déclaré ; concurrence de Kitron/Cicor/Scanfil [S-AUR-05,11–13]. | Devis gagnés, prix, marge de programme et migration intersites : non publics. Pas de différenciation prouvée par « trois sites » seul. |
| Services | Réparation, pièces et obsolescence déclarées [S-AUR-05]. | Revenus service, récurrence, garantie, délai réparation et droit sur données client : inconnus. |
| Infrastructure / RH | Changement de groupe et réduction d'effectif Tallinn ; 208 ETP moyens 2025 [S-AUR-02]. | Mandats de décision, charge et compétences intersites à vérifier. |
| Développement technique | Plateforme locale, DWH et applications IA annoncés **en Chine** [S-AUR-09,10]. | Architecture, accès, labels, performance, monitoring, adoption, factures et bénéfices contresignés : inconnus. |
| Approvisionnements | Coordination groupe et entité Shanghai annoncées [S-AUR-05,07]. | Mesurer prix, qualité, délais et contribution après transferts intra-groupe. |

**H1 — amélioration du coût complet de sourcing :** besoin tangible à Tallinn ; le levier IA n'est retenu que si prévision d'obsolescence ou substitution qualifiée bat règles simples, après contrôle qualité et droits BOM. Valeur = écart de contribution effectivement conservé par Aurightec, moins coût de mise en œuvre ; stock libéré = cash distinct d'EBITDA.

**H2 — qualité/test :** si les données de défauts ont des labels stables et un coût de faux rejet maîtrisé, une aide au diagnostic pourrait réduire retouches et retours. L'investissement AOI/X-ray 2025 est déjà une baseline ; les baisses TPM déclarées en Chine ne sont pas un effet causal IA.

**H3 — NPI, capacité et flux intersites :** harmoniser nomenclatures, versions et décisions de transfert pourrait protéger délais et marge ; prouver droits, qualification client et temps de bascule. Comparer APS/optimisation classique et processus existant avant modèle ML.

**H4 — usages IA Chine :** OCR, commandes, AIOps, connaissance et qualité 8D sont des déploiements **affirmés par Aurightec China**. Le « +125 % » d'efficacité AIOps n'a ni dénominateur ni période : exclu du calcul. Audit de 2–3 cohortes, coût de run et contrôle humain avant reprise par groupe.

## Red-team et inconnues qui changent la décision

1. **Finance et captation.** Compte Tallinn 2025 : 36,47 M€ de ventes, −10,6 % ; résultat net −0,90 M€. La perte 2024 de −4,62 M€ inclut 3,19 M€ de créances douteuses en autres charges ; l'amélioration apparente n'est donc pas une preuve de redressement organique [S-AUR-02, p. 22]. Obtenir comptes consolidés 2025–26, ventes/marges par programme, impact de la cession et transferts intra-groupe. Le 62,5 % de matières est un **ratio comptable Tallinn**, pas une marge de négociation.
2. **Contrats, données, causalité.** Identifier les droits OEM sur BOM, logs AOI/test, données fournisseurs et modèles ; confirmer baseline et coûts variables évités. Les déclarations China ont une seule origine, métrique non définie et aucune comparaison indépendante [S-AUR-09,10]. Les fournisseurs EMS concurrents offrent aussi NPI et services ; un « moat » n'est pas établi.
3. **Ownership et réplication.** COO groupe, DSI groupe, équipe BI/ML et stratégie ML observée restent `unknown`. Le mandataire de Tallinn ne devient pas COO par inférence. Valider les owners des systèmes Chine, la possibilité de transfert des données et les contraintes OT/qualité des trois sites.

**Hard gates :** `data_rights=unknown`, `security_ot=unknown`, `human_control=unknown`, `ownership=unknown`, `feasibility=unknown` pour les nouveaux cas. Aucun score compensatoire, classement 9-box ferme, maturité globale ou ROI chiffré. SWOT/VRIO/7S restent candidats : valeur des compétences de sourcing/test plausible ; rareté/imitabilité non prouvées face aux pairs ; organisation intersites inconnue. Stratégie dominante provisoire = **résilience de marge et qualité**, à confirmer par contribution programme. NO-ACTION et amélioration de processus sans IA restent comparateurs.

**Gate programme :** état `RESEARCH`, `package_ref=null`. Il manque originaux immuables et hashes, fragments/claims machine vérifiables, `package.json` + `strategic_context.json` v0.2 validés sur le réel, pilotes Sphere/STG et loopback, puis GO_DRAFT humain référencé au dossier. Cette note valide un **angle de recherche et des mécanismes testables**, pas le trois-pages final.
