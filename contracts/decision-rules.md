# Règles canoniques v0.1.0

## Maturité
`score=null, status=unknown` = aucune mesure publique défendable. Le code 0 du handoff est conservé comme libellé historique « non établi », jamais comme nombre dans les graphiques/calculs.
1 = exploration observée ; 2 = pratique répétée avec responsabilité et processus identifiables ; 3 = production gérée avec contrôles et suivi ; 4 = réplication à l'échelle avec résultats suivis et allocation stratégique. Chaque dimension a ses ancres spécifiques dans la procédure diagnostic. Le niveau maximal prouvé ne résume pas toute l'entreprise ; toujours préciser son périmètre et les bottlenecks.
Une note numérique exige des claims entreprise, une confiance justifiée et un motif ; aucune moyenne globale. L'absence de communication n'est ni contre-preuve ni maturité zéro.

## Priorisation
Huit dimensions ordinales low/medium/high/unknown : economic_value, strategic_value, feasibility, time_to_value, repeatability, adoption, risk, portfolio_reuse. Pour risk, high est défavorable ; pour adoption, high = readiness élevée. Pas de total automatique. Exposer dominance, désaccord et sensibilité aux inconnues ; si une inconnue inverse le classement, classer « à valider ».
Hard gate fail/unknown → blocked/validation_required avant tout classement. Gate pass sans preuve n'est pas défendable. Quick win implique faibles dépendances, réversibilité, owner plausible et preuve de valeur accessible ; l'horizon seul ne suffit pas.
Ensemble obligatoire des gates : data_rights, security_ot, human_control, ownership, feasibility. Un pass s'appuie sur un fait entreprise. Une non-applicabilité doit être justifiée dans reason avec sa preuve, pas supprimée de la liste.
0–6, 6–18, 18–36 mois sont des horizons indicatifs, jamais des promesses. Le bénéfice net retranche intégration, licences, supervision, change et run. Aucun ROI chiffré sans baseline, unité, période et hypothèses sourcées.

## Sourcing 3×3
Support/commodity : BUY ou OUTSOURCE ; support/parity : BUY ; support/differentiating : tester valorisation vs standardisation.
Enabler/commodity : BUY ou PARTNER ; enabler/parity : PARTNER ; enabler/differentiating : PARTNER ou BUILD.
Core/commodity : conserver les contrôles, simplifier l'exécution ; core/parity : acquérir/configurer sélectivement ; core/differentiating : BUILD ou PARTNER avec maîtrise des actifs.
Ce sont des présomptions à challenger, pas une fonction automatique. Toujours comparer baseline sans IA et NO-ACTION, TCO, données/IP, responsabilité, réversibilité et dépendance. Le renderer n'infère jamais la posture à partir de la case.

## Gates de contenu et de fin
GO_DRAFT exige une décision humaine datée avec référence au dossier/version. Une modification matérielle après validation réouvre HITL. FROZEN exige hash canonique du payload et GO_DRAFT correspondant. Le rendu doit préserver ce hash dans son manifeste.
Le validateur de contenu accepte uniquement un checkpoint FROZEN. Il n'atteste jamais RENDERED ni DONE. Les transitions finales et attestations QA/wiki/loopback sont contrôlées par l'orchestrateur et le dossier de revue, pas automatisées dans cette version.

Le profil `exec` peut produire une démonstration sur bundle validé non gelé, avec statut, hash et gates ouverts dans `render_manifest.json`. Le renderer seul ne valide pas ce bundle. Sans bundle, un payload ne sert que de fixture technique. Diffusion en comité d'investissement : GO_DRAFT référencé, gel et QA visuelle obligatoires.
DONE entreprise : identité/roster, signalétique/finance sourcées ou explicitement inconnues, thèse, chaîne, VRIO, 7S, SWOT, huit dimensions, séparation entreprise/secteur, use cases/horizons/sourcing, contradictions/inconnues, trois revues, HITL, freeze, trois pages et QA visuelle/reader, wiki/loopback.
DONE portefeuille : onze DONE, comparabilité contrôlée, heatmap avec couverture, mutualisations argumentées avec lineage vers au moins deux entreprises indépendantes et spécificités locales conservées. Deux occurrences seules ne prouvent pas une économie de mutualisation.

Gate marché : la revue pré-HITL contient une segmentation, une couverture sectorielle avec manques, des pairs comparables, une matrice drivers sourcée et le mapping vers les trois pages. Le gate est une revue sémantique humaine ; les schémas existants seuls ne le certifient pas.

Nouveaux dossiers : bundle v0.2 requis. Exécuter validate_bundle avec archive d’extraits pour intégrité ; les captures déclarent leur nature. Les reviews doivent toutes survivre avant freeze ; validation humaine inclut bundle_sha256 et accepted_unknown_ids. Segments/4P/Porter,COO/DSI et stratégie ML obligatoires même inconnus.
