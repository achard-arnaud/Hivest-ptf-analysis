# Aurightec — recherche business case, 24 septembre 2026

**État : RESEARCH, cutoff 23/09/2026.** Ce dossier intègre le [brief ToT fourni](intake_brief_tot_2026-09-24.md). Il s'agit d'un registre de vérifications à partir de pages consultées, et non d'une archive intégrale de pages ou d'un paquet v0.2. Les pages dynamiques sans date de publication sont des constats au jour de consultation, non une chronologie démontrée. Aucun ROI, score de maturité ou GO_DRAFT.

## Sources et claims décisifs

| ID | Source primaire, date de publication / consultation, localisation | Claim et périmètre | Limite |
|---|---|---|---|
| A01 | [Aurightec, site principal](https://aurightec.com/), n.d. / 24/09/2026, «About us», «Services», «Quality Assurance» | Offre EMS de complexité élevée et volume moyen, conception → fin de vie, transport/énergie/industrie/médical/communications ; sourcing, logistique, réparation. Certifications affichées. | Déclaration commerciale ; certification site par site et chiffre d'affaires par marché non établis. La mention d'un R&D corporate en France doit être vérifiée après la cession. |
| A02 | [Aurightec, sites](https://aurightec.com/locations/), n.d. / 24/09/2026, «Estonia/China/Malaysia» | Implantations Tallinn, Suzhou, Kulim. | Pas de volumes ni de contribution financière comparables. |
| A03 | [Aurightec, Suzhou](https://aurightec.com/locations/china/), n.d. / 24/09/2026, «Facility overview» | 11 400 m², 7 lignes SMT, 4 lignes de soudure à vague, 3 sélectives, 6 coating ; NPI, PCB, box build, tests. | Capacités déclarées, utilisation et rendement inconnus ; ne pas généraliser aux trois sites. |
| A04 | [Cicor, communiqué](https://www.cicor.com/en/news/article/market-entry-in-france-cicor-acquires-significant-business-activities-of-eolane/), 18/04/2025 / 24/09/2026, transaction ; [rapport annuel 2025](https://report.cicor.com/ar25/category/notes-group_en), publié 2026 / 24/09/2026, «Acquisition of business» | Transfert effectif 22/04/2025 : cinq sites français et deux marocains à Cicor, environ 890 salariés. | Les CHF 125m annualisés et résultats Cicor concernent les actifs cédés, **pas Aurightec**. Deux publications du même acteur/origine, pas deux confirmations indépendantes. |
| A05 | [Aurightec Malaysia, communiqué de lancement](https://www.aurightec.my/aurightec-launches-as-independent-ems-leader-with-global-reach-and-a-commitment-to-customer-service-quality-and-sustainability/), mai 2025 / 24/09/2026 | Nouvelle identité Aurightec après repositionnement Éolane ; Olivier Clément cité comme CEO. | Communication d'entreprise, pas preuve de performance ni d'IA déployée. |
| A06 | [Registre officiel estonien](https://ariregister.rik.ee/est/company/10092440/Aktsiaselts-Eolane-Tallinn), exercice 2025 déposé le 11/06/2026 / 24/09/2026 | La personne morale «Aurightec Estonia» a pour anciens noms Eolane Tallinn et Elcoteq Tallinn ; un compte 2025 existe. | Compte et tableaux non extraits de façon fiable ici ; **aucun chiffre groupe** extrapolé. |
| A07 | [Commission européenne, Chips Act](https://digital-strategy.ec.europa.eu/en/policies/european-chips-act), version consultée 24/09/2026 | La résilience et la dépendance aux chaînes de semi-conducteurs sont des enjeux européens. | Contexte amont, ni pénurie courante prouvée pour Aurightec ni impact marge chiffré. |
| A08 | [Cicor, résultats H1 2025](https://www.cicor.com/en/news/article/cicor-grows-double-digit-again-and-creates-strong-foundation-for-further-expansion/), 2025 / 24/09/2026 | Le pair a mis en place un reporting opérationnel et financier lors de l'intégration des actifs Éolane France. | Cas d'un concurrent sur actifs cédés ; benchmark de méthode, aucune preuve de capacité Aurightec. |

**Contre-preuve de périmètre :** A04 retire les sites FR/MA et les 890 salariés du périmètre à analyser. Le site Aurightec conserve une formulation historique sur le R&D en France (A01) : vérifier qui détient réellement équipes, IP et contrats. L'annonce de «technologies avancées» (A05) n'est pas une preuve de smart factory ou d'IA en production.

## Structure sectorielle et économie transférable avec précaution

EMS high-mix : les OEM contrôlent spécifications et homologation ; la concurrence porte sur coût total, qualité, fiabilité, NPI et disponibilité, avec qualification et changement de fournisseur coûteux dans les marchés régulés. Amont : composants électroniques à cycles de vie et délais hétérogènes ; aval : livraisons de programmes et services après-vente. Les trois pays offrent des options de localisation, **sans** prouver une capacité de bascule fluide entre usines. Cicor est un pair européen pertinent mais détient précisément les actifs sortis du périmètre : ne pas utiliser son CA/marge comme proxy. Les chiffres agrégés nord-américains EMS de l'association sectorielle seraient un autre marché, pas le TAM d'Aurightec. Sources de cadre : A01–A04, A07–A08 ; parts de marché, clients et concurrence locale à documenter.

| Driver prioritaire (hypothèse) | Mécanisme et stratégie de valeur | Baseline et test falsifiable | Inversion / risque |
|---|---|---|---|
| A-D1, continuité composants et obsolescence | nomenclature + alternatives approuvées → service et risque évité, éventuellement BFR ; règle métier d'abord | ruptures BOM, achats spot, coûts d'arrêt, stock âgé par client/site ; tester alerte précoce contre suivi manuel | contrats imposent les composants, données ERP et autorisations client indisponibles |
| A-D2, rendement/test high-mix | dérive de procédé par produit/lot/ligne → coûts de rebut/reprise et qualité ; SPC avant ML | FPY, défauts, retouches, heures de test, coût non-qualité par famille ; pilote sur une ligne Suzhou | faible volume/labels et changements de gamme rendent le modèle instable |
| A-D3, NPI et devis | industrialisation/design-to-cost → délai de lancement et marge projet ; checklist/optimisation classiques avant GenAI | délai devis→SOP, écarts coût prévu/réel, ingénierie, changements ECO | secrets clients, faible réutilisation des designs ou données cloisonnées |
| A-D4, orchestration intersites | planification capacité, service, BFR et résilience ; simulation et optimisation sous contraintes avant prédiction | OTD, charge lignes, transports, qualification client par site ; scénario d'incident réel | impossibilité contractuelle/réglementaire de transférer les programmes |

**Ordre de décision provisoire :** A-D1/A-D2 selon coût réel de rupture vs coût non-qualité ; A-D3 si conversion NPI/marge documentée ; A-D4 seulement si arbitrages multisites autorisés. Aucun montant EBITDA ou cash à additionner sans baseline. Économie : économies d'achat effectivement capturées et rebut évité → EBITDA net des coûts ; stock réduit → cash ponctuel, jamais EBITDA récurrent ; capacité libérée → revenu uniquement si commande et goulot démontrés.

## Trois lectures contradictoires du business case

1. **Achats/résilience** : la valeur viendrait de la nomenclature et de l'obsolescence ; réfutée si les OEM imposent tout et supportent le risque financier.
2. **Qualité/capacité** : la valeur viendrait du test et du rendement ; réfutée si le FPY est déjà élevé ou les rebuts négligeables.
3. **Différenciation NPI/service** : la valeur viendrait de cycles projet et maintenance ; réfutée si l'essentiel du CA est build-to-print à prix figé.

Consensus limité : A01–A03 établissent les processus, pas leur poids économique. A04 impose de repartir des comptes 2025 des seules entités conservées. Aucune des trois thèses n'est validée financièrement à ce stade.

## Couverture et questions qui changent la décision

- **Périmètre/finance :** organigramme légal post-cession, comptes consolidés 2025 et 2026, marge par site/marché, dette, BFR, transfert IP/R&D. Owner à interroger : CFO groupe.
- **Marché/clients :** mix clients, géographies et contrats, concentration top 10, quotas, clauses d'approvisionnement et qualification multisite, pairs comparables et puissance de négociation. Owner : CEO/commercial.
- **Opérations/data :** FPY, rebuts, downtime, OTD, inventaire, ERP/MES/PLM et données de test, équipes data/BI/ML, usages IA réellement en production, gouvernance qualité. Owner : COO et DSI groupe **non identifiés publiquement** ; Olivier Clément est CEO selon A05, pas COO.
- **Archives et intégrité :** acquérir originaux immuables et SHA-256 hors code, fragments à locators, sources/claims JSON, revue de contradictions et bundle v0.2 réel avant HITL. Ces lectures web ne prétendent pas fournir de capture complète.

**Verdict : RESEARCH_TARGETED.** Le mécanisme industriel est plausible, mais la baseline et la borne post-cession manquent. Le trois-pages peut être préparé comme brouillon sourcé, pas publié comme diagnostic final.
