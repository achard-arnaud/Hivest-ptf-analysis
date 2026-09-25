# Template — Note stratégique marché et transformation (5 à 7 pages)

**Version :** 0.2.0. **Lifecycle:** candidate. **Dimension principale :** business ; les dimensions produit/technique ne servent que les décisions du lecteur. **Usage :** fonds, investisseur actif, direction générale ou comité de transformation qui doit décider d'une capacité sur 3 à 5 ans à partir d'un métier, de signaux de marché et de retours d'expérience. Ce format complète `architecture-note` (analyse d'une organisation) et `benchmarking` (comparaison ciblée) ; il n'en duplique pas les sections.

## Contrat d'entrée et de preuve

- Poser une décision explicite, le lecteur et son mandat, le périmètre d'entités, la date d'arrêt des faits et l'horizon projeté ; identifier si la note prépare un échange, une décision ou un investissement.
- Lire d'abord les documents fournis, puis chercher les manques dans sources primaires et retours indépendants. Consigner inventaire lu/non lu. Ne pas assimiler le récit de l'organisation à un déploiement ni une étude fournisseur à une preuve client.
- Tenir une table source → fragment localisé → claim typé (`fact`, `attributed`, `inference`, `hypothesis`, `recommendation`, `unknown`) → fonction dans le raisonnement. Les hypothèses ont un test et une condition d'abandon. Dates, géographies, tailles d'entreprises et devises demeurent explicites.
- Ne pas convertir une tendance de marché en taille de marché adressable, une possibilité technologique en résultat, ou un chiffre de facturation en marge nette. Les données financières restent conservatrices ; toute extrapolation exige dénominateur et modèle.

## Séquence narrative et budget de pages

Un titre raconte la décision, pas le thème. Les sections suivent un mécanisme économique et se lisent sans annexe. Viser environ 2 800 à 3 600 mots **avec** tables et sources pour une composition A4 de 5 à 7 pages ; l'édition finale contrôle effectivement le nombre de pages et la lisibilité.

| Partie | Fonction dans l'argument | Budget cible |
|---|---|---|
| **1. Thèse et pourquoi maintenant** | La décision, le lien à la mission existante, le signal externe daté et l'objection la plus forte | 0,75–1 page |
| **2. Moteurs externes et internes** | Drivers de marché → exposition vérifiée de la cible → mécanisme de valeur ; niveaux de preuve distincts | 0,75–1 page |
| **3. Chaîne réelle du métier** | Étapes pré/deal/post ou autre chaîne pertinente ; friction, baselines, cas sans IA, droits de décision, indicateur et erreur redoutée | 1–1,25 page |
| **4. Trajectoire de transformation** | Fondations → adoption managériale → reconfiguration des processus → différenciation ; dépendances digitales, data, ML, IA, automatisation et robotique seulement si utiles | 1–1,25 page |
| **5. Benchmarks et histoires** | 3 à 5 comparateurs au bon périmètre ; une histoire interne vérifiable et au plus deux histoires illustratives avec contre-test | 0,75–1 page |
| **6. Modèle économique et décision** | Options build/partner/service, coûts complets, gouvernance, conflits d'intérêts, trajectoire 0–60 mois, rôle et questions d'entretien | 0,75–1 page |
| **Registre de sources** | Références de chaque claim matériel, date de consultation, biais, absences et accès incomplets | 0,5–1 page |

## Fils directeurs obligatoires

1. **Mission → changement → preuve de valeur.** Trouver dans les sources de la cible la vocation revendiquée, puis ce que le nouveau levier prolongerait réellement. Une simple analogie est marquée comme inférence.
2. **Marché → cible.** Chaque statistique précise population, date et transposabilité. Séparer ce qu'un pair fait de ce que la cible fait.
3. **Technologie → management.** Décrire l'owner métier, le manager de proximité, l'adoption, la mesure et le droit d'arrêt ; un agent ou modèle ne constitue pas à lui seul une transformation.
4. **Interne → externe.** Distinguer une capacité mutualisée au bénéfice du cœur d'activité d'une nouvelle ligne de revenus. Pour la seconde, tester demande solvable, prix, charges, conventions intragroupe, réglementation, conflit d'intérêts et liberté des clients.
5. **Trajectoire professionnelle.** Si la note soutient un échange de recrutement, expliquer l'apport du candidat à partir de faits autorisés et le mandat évolutif recherché. Ne pas promettre une fonction créée ni transformer un retour d'expérience personnel en fait public.

## Forme des histoires

`Signal daté → friction concrète du métier → décision humaine → capacité mise en place → mesure observée ou manquante → contre-test.` Une histoire illustrative porte explicitement l'étiquette *scénario*, et n'ajoute pas de preuve. Faire revenir la première histoire à la conclusion lorsque cela éclaire la décision.

## Gates de rédaction et de publication

- Trois propositions hiérarchisées au maximum en première page ; pas de liste de fournisseurs présentée comme recommandation implicite.
- Au moins une alternative non IA et un scénario d'absence d'action dans la chaîne du métier ; les gains de temps incluent la vérification et les erreurs.
- L'objection la plus forte change le plan ou le niveau de confiance, plutôt que d'être reléguée aux risques génériques.
- Tout revenu facturé est séparé des gains des participations et des frais de gestion ; source, périmètre et charges correspondantes visibles.
- Questions de clôture adressables à un owner et capables de modifier la décision ; aucune attribution de rôle ou de compétence interne sans preuve.
- Garder le dossier de recherche et les itérations hors dépôt ; promouvoir uniquement le template, sa fixture, les sources contrôlées et la note candidate. Une validation humaine distincte promeut le template au statut validé.

## Profil de rendu `exec` (v0.2.0) — livre blanc C-Level 5 à 7 pages

Le profil `exec` sert quand la note circule auprès d'associés, d'un comité ou d'un recruteur. Il garde toute la chaîne de preuve dans le dossier de travail et n'affiche sur la page que la décision, les faits utiles et leurs sources numérotées.

**Composition imposée (A4 portrait) :**

| Bloc | Rôle | Directive du renderer |
|---|---|---|
| Bandeau de couverture | Kicker, titre-thèse, sous-titre, auteur, date, horizon, public | front matter |
| En bref | Trois messages numérotés, lisibles seuls | `::: tldr` |
| Bande KPI | Quatre chiffres datés et sourcés, un par driver | `::: kpis` |
| Sections numérotées | `## 1 — Titre` + phrase d'accroche (`{: .lede}`) | Markdown |
| Figures | 3 à 4 Mermaid rendus en PNG, légendés, seuil de 70 % ou transposition | ```` ```mermaid ```` + `%% caption:` |
| Encadrés | Message clé (`callout`), point d'attention (`callout-gold`), retour d'expérience (`story`) | `:::` |
| Double colonne | Drivers de marché / drivers internes | `::: cols` + `+++` |
| Sources | Notes numérotées dans l'ordre de première citation, sur deux colonnes | `[^id]` |

**Règles d'écriture exec :**

- Phrases directes et affirmatives. Réécrire toute construction en balancement (« X n'est pas Y mais Z », « plutôt que »).
- Pas d'étiquettes de preuve sur la page (`fait`, `inférence`…) ; la nuance passe par le verbe (« revendique », « déclare ») et par la note de source.
- Une seule ligne de périmètre, placée dans l'introduction des sources.
- Tableaux de 3 à 4 colonnes, première colonne en libellé court ; puces pour toute énumération de trois éléments ou plus.
- Une synthèse de recherche en tableau `Thème | Convergence | Constat | Implication` (inspirée de `design:research-synthesis`).
- En contexte de recrutement : un encadré `story` pour l'expérience du candidat, un tableau d'alignement réciproque, trois questions d'échange.

**Gates QA automatiques (`renderers/strategic_note/build.py`) :** pages dans `page_range` ; échelle de chaque figure ≥ 0,70 sinon transposition LR↔TB ; corps ≥ 9 pt, texte secondaire ≥ 8 pt ; rapport `qa_report.json`. La relecture visuelle de chaque page reste obligatoire après le dernier changement (lignes orphelines de tableau, blancs de fin de page).