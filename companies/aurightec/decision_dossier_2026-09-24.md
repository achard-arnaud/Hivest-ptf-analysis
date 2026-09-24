# Aurightec — dossier de décision pré-HITL, 24/09/2026

**Décision proposée : `RESEARCH_TARGETED` pour le rendu final.** Les [sept claims revus](claims_promoted_2026-09-24.json) autorisent une thèse et un plan de validation. Ils n'autorisent ni ROI, ni classement ferme des cas d'usage, ni GO_DRAFT du trois pages. État canonique : `RESEARCH`, `package_ref=null` ; aucun GO_DRAFT humain n'est enregistré. Le programme est en phase `PILOTS` avec `production_allowed=false` et sans loopback des deux pilotes. Ce dossier n'est pas un bundle v0.2 validé.

## Proposition resserrée et éléments adverses

| Proposition transmissible à Claude | Preuve / portée | Explication adverse, falsificateur |
|---|---|---|
| La base de coûts matières et la perte de Tallinn justifient un test de contribution par programme, incluant sourcing et qualité. | AUR-C04, comptes audités de la filiale. | Les coûts sont répercutés aux OEM, les économies ne sont pas captées ou le capex inspection a déjà traité la non-qualité. |
| Les ventes de Tallinn ont baissé comptablement ; la demande externe n'est pas isolée. | AUR-C01–03 ; 91,35 % de la baisse en montant coïncide avec la réduction des ventes intragroupe publiées. | Transfert de facturation et cession des entités France/Maroc ; une évolution de mix ou de classification peut rendre même le calcul hors intragroupe non comparable. |
| Les comptes consolidés 2025 existent mais leur performance chiffrée n'est pas encore vérifiée. | AUR-C05, avis officiel BODACC ; agrégats Pappers S-AUR-16 exclus des chiffres promus. | L'original pourrait modifier périmètre, retraitements et interprétation de la reprise opérationnelle. |
| La Chine dispose d'un signal de discipline opérationnelle indépendant et revendique des cas IA locaux. | AUR-C06, JIPM ; AUR-C07, articles de l'entreprise. | Prix TPM ≠ impact IA ; les applications peuvent être pilotes peu adoptés, sans droits de transfert ni ROI. |

**Chaîne à tester :** signal externe de rivalité EMS [S-AUR-11–13] → exposition Tallinn (matières/qualité) [AUR-C04] → D1/D2 → coût évité ou qualité mesurée par programme → test MRP/SPC et processus sans IA → éventuellement pilote ML sous hard gates. D3 demande une réconciliation préalable des flux intragroupe. D4 dépend des revenus de service et des contrats. Chaque étape doit conserver un owner et une baseline ; cash de stock et EBITDA ne s'additionnent pas. Les pairs prouvent une concurrence, pas un écart de productivité transférable.

## Trois revues distinctes

1. **Conformité aux contrats — `REOPEN_TARGETED`.** Fragments localisés et claims typés existent, mais aucune capture originale immuable avec URI/hash, aucun `package.json` et `strategic_context.json` v0.2 réel validé ; autres exigences segmentation/4P/Porter/VRIO/7S/shortlist et pilote loopback non satisfaites. Ne pas changer l'état.
2. **Meilleure explication alternative — `SURVIVES_WITH_NARROWING` pour la thèse de test, `REOPEN_TARGETED` pour la thèse de demande.** La cession et les facturations intragroupe expliquent potentiellement l'essentiel du recul comptable. Une économie IA n'est pas démontrée par la seule taille du poste matières ni par un prix TPM.
3. **Utilité décisionnelle — `REOPEN_TARGETED` pour GO_DRAFT, utile pour collecte ciblée.** Le lecteur peut décider quelles données demander et quels mécanismes tester, mais ne peut arbitrer budget, site ou portefeuille de cas sans contribution par programme, droit sur données et owner.

## Recherches bornées et conditions d'arrêt

| Question qui inverse le verdict | Owner à solliciter | Pièce ou test attendu | Stop |
|---|---|---|---|
| Quelles ventes et marges 2025 restent dans le périmètre consolidé post-cession ? | DAF groupe | Original consolidé 2025 ; pont 2024–25 à périmètre constant ; réconciliation note 18 Tallinn, Maroc, cession ; contribution par programme. | Chiffres, audit/périmètre et pont documentés ; sinon maintenir unknown. |
| Aurightec capte-t-il une économie matières/qualité mesurable ? | Direction opérations/qualité et DAF | Top programmes, clause de répercussion BOM, rebut/retouche/garantie, stocks dormants, base avant/après AOI ; contre-test MRP/SPC. | Baseline, coût évitable net, attribution et droits validés ou cas écarté. |
| Quels cas IA chinois sont réellement exploités et transférables ? | Responsable site Chine, DSI/data et juridique | Journal d'usage, coûts de run, performance par cohorte, système/owner, sécurité OT, droits client, capacité de repli ; titres exacts COO/DSI groupe. | Deux cohortes et décision sur réplication, ou décision de ne pas répliquer. |

## Décision humaine ultérieure

Après dépôt des originaux et vérification du bundle v0.2, diagnostic/shortlist/red-team sur données réelles et loopback des pilotes Sphere/STG, présenter le dossier actualisé et son SHA-256 à l'humain pour choisir `GO_DRAFT`, `RESEARCH_TARGETED`, `NARROW_SCOPE` ou `PIVOT`. Une validation de l'angle de recherche ne constitue pas un GO_DRAFT. Claude peut reprendre les recherches et préparer une structure de contenu, mais le trois pages final attend le gate explicite.
