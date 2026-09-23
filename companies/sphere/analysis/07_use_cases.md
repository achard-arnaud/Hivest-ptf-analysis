# Cas IA/ML et chaîne de valeur — vue générée

Tous les cas sont hypothétiques, non éligibles au déploiement tant que les gates restent inconnus. Horizons exploratoires6–18mois,18–36mois pour UC07/10, sans engagement. UC-S01 est reclassé EN-S01, prérequis MDM.

| Cas | Processus | Driver / stratégie | Méthode et baseline | KPI / owner proposé |
|---|---|---|---|
| UC-S02 — Configuration catalogue assistée | Vente | D05 / DIFFERENTIATION_GROWTH | RAG/GenAI borné, classification ; baseline : Recherche catalogue et règles de compatibilité | Taux de conversion/marge nette ; validation du devis ; commercial (mandat non confirmé) |
| UC-S03 — Prévision et politiques de stock | Stocks et service | D03a / CAPITAL_PRODUCTIVITY | ML prévision probabiliste + optimisation ; baseline : S&OP actuel, saisonnier naïf,ABC/XYZ | DIO moyen+OTIF ; backtest temporel puis pilote ; supply chain (mandat non confirmé) |
| UC-S04 — Allocation et mix matière | Achats | D01b / COST_REDUCTION | Modèles qualité supervisés si données ; baseline : Formulation/règles et optimisation classique | Coût/t conforme ; essais physiques et contraintes produit ; achats/qualité (mandat non confirmé) |
| UC-S05 — Inspection visuelle qualité | Extrusion qualité | D02 / COST_REDUCTION | Computer vision supervisée ; baseline : Contrôle humain, capteurs,SPC | Défauts échappés, faux rejets, scrap évitable ; qualité (mandat non confirmé) |
| UC-S06 — Dérives process et énergie | Extrusion qualité | D02 / COST_REDUCTION | Anomaly detection / modèle supervisé ; baseline : SPC, alarmes, standard réglages | kg rebut/t et kWh/t conforme ; contrôle intersites ; industriel (mandat non confirmé) |
| UC-S07 — Ordonnancement multisites | Planification | D04 / COST_AVOIDANCE | Recherche opérationnelle ; ML optionnel ; baseline : Planification actuelle / solveur contraintes | Délais/capacité utile ; goulot prouvé avant capex évité ; opérations (mandat non confirmé) |
| UC-S08 — Dossiers qualité et connaissances | Conformité | D06 / RISK_RESILIENCE | RAG/GenAI avec citations ; baseline : GED, moteur lexical et checklist | Erreurs dossier et délai ; validation expert ; qualité/réglementaire (mandat non confirmé) |
| UC-S09 — Pricing et indexation matière | Pricing indexation | D01a / RISK_RESILIENCE | Détection anomalies ; élasticité seulement identifiable ; baseline : Clauses contractuelles et BI marge | Asymétrie pass-through ; marge durable distincte du timing ; commercial/finance (mandat non confirmé) |
| UC-S10 — Formulation et plan d’essais | R&D | D05 / DIFFERENTIATION_GROWTH | Modèles supervisés / optimisation bayésienne ; baseline : Expertise matériaux et plans expérimentaux | Nombre essais et performance validée ; pas de recette auto-libérée ; R&D (mandat non confirmé) |
| UC-S11 — Recouvrement et résolution litiges | Order to cash | D03b / CAPITAL_PRODUCTIVITY | Scoring retard + GenAI brouillons ; baseline : Balance âgée, règles relance et workflow litiges | DSO et cash incrémental par cohortes ; envoi humain ; finance/crédit (mandat non confirmé) |
| UC-S12 — MOQ, lots et fréquence de livraison | Achats et livraison | D03c / CAPITAL_PRODUCTIVITY | Optimisation contrainte alimentée par prévision ML ; baseline : EOQ/règles contractuelles/optimisation classique | Coût total livré et OTIF ; pas transport gagné contre surstock ; achats/supply chain (mandat non confirmé) |

## Gates et ratings par cas
Les cinq gates data_rights,security_ot,human_control,ownership,feasibility sont évalués séparément dans package.json, avec raison propre à chaque cas : tous unknown à ce stade. Les huit ratings (valeur économique,stratégique,faisabilité,time-to-value,répétabilité,adoption,risque,réutilisation) restent unknown faute de baseline suffisante. Inconnu ne vaut ni zéro ni feu vert.

La chaîne couvre achats → R&D → extrusion/qualité → planification/conversion → stocks/livraison → pricing/indexation → vente → order-to-cash ; conformité et données sont transversales. Chaque activité possède ses contrôles, contraintes et cas liés dans package.json. Le sourcing est provisoire : PARTNER pour méthodes industrielles spécifiques ; BUY/configurer pour fonctions standard. Aucune sélection de fournisseur.
