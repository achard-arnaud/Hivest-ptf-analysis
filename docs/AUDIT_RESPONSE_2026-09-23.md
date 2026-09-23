# Relecture de l'audit du commit bb797e5

Ce document relève les points confirmés et les limites de l'audit. Les références ci-dessous visent le **commit audité**, avant les correctifs ; celles du code courant diffèrent.

## Points confirmés et citations corrigées

| Constat | Lignes exactes au commit bb797e5 | Suite |
|---|---|---|
| Une offre d'emploi ou un claim périmé peut lever un hard gate | `scripts/validate.py:100-104` ; la fraîcheur n'est contrôlée que pour la maturité à `:74` | Règles + tests ajoutés |
| Deux origines déclarées peuvent masquer le même document et un score 4 hors delivery peut passer sans preuve scaled | `scripts/validate.py:76-82` (la restriction `delivery` est précisément `:81`, le test de stage `:82`) | Déduplication URL/hash + stage exigé pour chaque dimension |
| UC fact peut reposer sur une annonce | `scripts/validate.py:92-93` | Stage expérimental ou ultérieur exigé |
| Passage au contenu gelé sans vérification d'une archive source | `scripts/validate.py:110-145` ; le validateur vérifie l'extrait mais pas le snapshot | Non résolu : capture et contrôle des originaux nécessaires |
| Sphere n'a pas de package JSON ; le registre ne revendique pas de raw hash | `companies/sphere/manifest.json:4` ; `companies/sphere/source_register.md:3` | Statut RESEARCH, package_ref null, gate pré-HITL explicite |
| Marché obligatoire mais non modélisé dans le package v0.1 | `skills/hivest-portfolio-ai/references/market-drivers.md:1-16` ; `contracts/company-package.schema.json:6` | Contrat package v0.2 candidat ajouté |
| Référence de priorité « 9-box » ambiguë | `AGENTS.md:20` au commit audité | À renommer avec migration documentaire cohérente |

## Nuances et décisions de conception

1. **« Les 8 sondes passent » ne signifie pas « huit défaillances de même gravité ».** La date d'observation antérieure à la publication, l'inférence non ancrée et une confiance haute sur source partielle ne produisent pas la même exposition qu'un gate indûment levé. Les tests séparent ces cas.
2. **Un score 3 ou 4 dans toute dimension conditionné à un déploiement** est un défaut conservateur de l'audit, mais il peut pénaliser une dimension de gouvernance observable sans déploiement IA. Une grille par dimension reste à trancher et à formaliser avant toute notation réelle.
3. **Le hash seul n'établit pas la fidélité d'un extrait.** Le validateur ne récupère pas les snapshots. Aucun PASS package ne doit être interprété comme une certification de la vérité des sources.
4. **Sphere ne peut pas devenir conforme par simple conversion Markdown → JSON.** Il faut capturer les documents consultés, retrouver les locators, vérifier les droits et soumettre les claims révisés à une revue. Les références sources de la note ne sont pas des archives.
5. **Une migration automatique 0.1 → 0.2 serait une fabrique d'hypothèses implicites.** La lecture historique 0.1 reste possible ; la construction d'un package 0.2 exige des données collectées et qualifiées.
6. **Les estimations achats et stocks de l'audit sont des sensibilités arithmétiques, pas des bénéfices incrémentaux démontrés.** Il faut préciser l'assiette réellement adressable, la marge, la durée, la situation de référence, la part imputable à l'IA et éviter le double compte EBITDA/BFR avant toute projection sur les pages.

## État après patch

Fait : durcissement des preuves de gates/maturité/UC, fraîcheur, origine, canonicalisation NFC, contrat marché v0.2 pour le package, CLI JSON, 19 nouveaux tests ciblés, gate Sphere pré-HITL. Les tests de contrats passent.

À faire avant STG : captures source Sphere avec hashes réels, package v0.2 et revue des claims ; contrat de projection trois pages ; protocole d'états et checkpoints ; rendu et QA ; DRL et arbitrages métier. Le présent correctif ne revendique ni un pilote validé ni un pipeline de bout en bout.
