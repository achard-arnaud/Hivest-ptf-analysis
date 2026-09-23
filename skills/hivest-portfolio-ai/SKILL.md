---
name: hivest-portfolio-ai
description: Piloter le diagnostic de maturité et création de valeur IA du portefeuille Hivest, reprendre une entreprise ou consolider le portefeuille avec preuve, chaîne de valeur, huit dimensions, use cases et trois pages. Utiliser pour ce programme et ses gates ; exclure product matching et recommandations fournisseur.
---

# Hivest portfolio AI
Lire AGENTS.md et program/state.json dans le dépôt Hivest-ptf-analysis, puis le manifest de l'entité. Si le dépôt n'est pas local, récupérer uniquement ces fichiers depuis https://github.com/achard-arnaud/Hivest-ptf-analysis. Ne pas réinventer ses contrats.
Charger une procédure métier selon l'étape :
- Intake/recherche/wiki : [evidence](references/evidence.md).
- Chaîne/VRIO/7S/maturité : [diagnostic](references/diagnostic.md).
- Inventaire/9-box/priorité : [opportunities](references/opportunities.md).
- Red-team/HITL : [review](references/review.md).
- Storytelling/freeze/rendu : [composition](references/composition.md) ; profil exec : [exec-writing](references/exec-writing.md) et `templates/THREE_PAGER_EXEC_v0.3.md` dans le dépôt.
- Loopback/consolidation : [learning](references/learning.md).

Préserver fact/inference/hypothesis/recommendation/unknown, source→fragment→claim, dates, contre-preuves, périmètre et propriétaire. Inconnu = null, jamais zéro. Pas de moyenne de maturité, pas de vérité entreprise issue du seul secteur, pas de score qui compense un hard gate.
Garder les runs temporaires hors code ; ne promouvoir que les connaissances canoniques et fixtures revues. Business est la dimension primaire ; technical et product servent le diagnostic.
Ne pas rédiger le trois-pages audit final sans GO_DRAFT humain référencé au dossier. Le profil exec de démonstration peut être composé à partir d'un bundle validé non gelé ; consigner ses gates uniquement dans le manifeste. Une fixture non sourcée sert aux tests de rendu et ne vaut pas bundle validé. Deux pilotes et loopback avant production par clusters. Les tests structurels ne remplacent pas la lecture des sources ni la QA visuelle.

## Contexte externe obligatoire
Avant diagnostic et shortlist, charger `references/market-drivers.md` : collecte sites/études → segmentation et concurrence → drivers industriels priorisés → stratégie de valeur → use cases → trois pages. Cette étape s’applique aussi aux reprises.

Le complément market-drivers obligatoire s’ajoute à la procédure métier unique sélectionnée pour l’étape.

Pour reprise, portefeuille, leadership/ML ou loopback, appliquer [research-graph](references/research-graph.md). Les nouveaux dossiers exigent le bundle v0.2, vérifié sur données réelles avant HITL ; la validation legacy seule ne suffit pas.
