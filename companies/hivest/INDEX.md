# Hivest — workstream index

**Entity:** Hivest Capital Partners  
**Diagnostic state:** suivre `manifest.json` ; le workstream de note stratégique ci-dessous **ne change pas le gate**.  
**Cutoff note stratégique:** 25 septembre 2026

## Note stratégique / recrutement

1. [NOTE_STRATEGIQUE_2026-09.md](NOTE_STRATEGIQUE_2026-09.md) — mémoire stratégique et registre de sources existants.
2. [reference/NOTE_STRATEGIQUE_REFERENCE_V1.md](reference/NOTE_STRATEGIQUE_REFERENCE_V1.md) — source Markdown du PDF de référence 6 pages ; référence visuelle / structurelle, non source de vérité supplémentaire.
3. [STRATEGIC_NOTE_FEEDBACK_2026-09-25.md](STRATEGIC_NOTE_FEEDBACK_2026-09-25.md) — retours éditoriaux canoniques validés.
4. [STRATEGIC_NOTE_GAPS_2026-09-25.md](STRATEGIC_NOTE_GAPS_2026-09-25.md) — claims à corriger, gaps de preuve et stop conditions.
5. [SOURCE_SUMMARIES_2026-09-25.md](SOURCE_SUMMARIES_2026-09-25.md) — scraping/synthèse canonique des sources externes ; raw hors dépôt.
6. [CLAUDE_CODE_EXECUTION_2026-09-25.md](CLAUDE_CODE_EXECUTION_2026-09-25.md) — contrat d'exécution Claude Code pour la V2.

## Styles

- `renderers/strategic_note/` : renderer et thème de la note C-Level 5–7 pages, dérivés du rendu de référence.
- `templates/strategic-market-note.md` : contrat générique business / evidence.
- `renderers/three_pager_exec/exec_theme.css` : palette / vocabulaire exec existant à réutiliser en cohérence.

## Checkpoint

- Feedback et gaps promus : 25/09/2026.
- Nouvelles sources résumées : 25/09/2026.
- Référence V1 et renderer stratégique promus.
- **Aucun changement** de `program/state.json` ou `companies/hivest/manifest.json`.
- Prochaine procédure pour ce workstream : exécuter `CLAUDE_CODE_EXECUTION_2026-09-25.md` dans Claude Code ; le diagnostic Hivest reste gouverné séparément par le workflow programme.
