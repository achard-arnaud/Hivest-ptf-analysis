# THREE_PAGER_PORTFOLIO_AI v0.3 `exec` — rétro-documentation carte par carte

> Document externe reçu pour intégration. Les affirmations ci-dessous sur une validation propriétaire et une identité au pixel près décrivent le run d'origine ; elles ne sont pas certifiées par ce dépôt. Ici, la référence Sphere est une fixture non vérifiée (`tests/fixtures/exec/sphere_unverified_v0.3.json`). Voir `docs/CATCHUP_EXEC_V0.3.md`.

Référence : rendu SPHERE v2 du 24/09/2026, validé par François (« Excellent »). Ce document décrit chaque cadre du rendu pour qu'un autre agent (Codex, Claude, GPT) le reproduise sur une autre participation sans dériver.
Fichiers liés : `sphere_exec_payload.json` (contenu de référence), `render_exec.py` (renderer générique), `exec_theme.css` (tokens), `test_exec_mutations.py` (NRT de cohérence).
Le renderer piloté par payload reproduit la v2 **au pixel près** (écart PNG nul sur les 3 pages) : le template est désormais une donnée, plus un script écrit à la main.

---

## 0. Architecture et règles de lecture

```
bundle preuve (package.json, strategic_context.json, analysis/*, sources)   ← couche preuve, rigueur inchangée
        │  rédaction guidée par ce document (méta-prompts §3–5)
        ▼
payload exec (JSON, une valeur canonique par chiffre, renvois structurés)   ← couche présentation
        │  render_exec.py : mise en page seule + 10 contrôles de cohérence
        ▼
HTML → PDF (Chromium) → PNG → qa.py (DOM : overlap, overflow, <9 pt, padding)  → inspection visuelle
```

| Règle | Détail |
|---|---|
| Lecteur | C-level ou jury d'entretien de direction stratégique IA. Lit en 3 minutes, 15 secondes par page. |
| Une idée par carte | Chaque carte répond à **une** question et se termine par **« À retenir »** : une phrase, jugement ou implication, jamais un résumé du corps. |
| Qualifier, pas s'excuser | On écrit ce qu'on sait et ce qu'on en déduit. Une inconnue n'apparaît que si elle change la décision, et une seule fois (ex. « owner data/IA à attribuer »). |
| Épistémique hors page | Pas de tags, de légende ni de statut de gate. Le niveau de preuve est dans le payload (`figures[].kind`, `lineage`) et se lit dans le verbe : fait → indicatif ; inférence → verbe de jugement (« se joue », « doit ») ; hypothèse → conditionnel ou « à qualifier ». |
| Chiffres | Tout montant ou pourcentage vient de `figures` et s'écrit `{clé}` dans le texte. Le renderer refuse une clé inconnue (G-C5). |
| Identifiants | Aucun ID interne sur la page (A-xx, UC-xx, D0x, DRV-xx). Seuls renvois autorisés : « → cas n », « → transformation MT ». |
| Colonne vertébrale | **Magic Quadrant** : le pied de p.1 classe les activités (Core / Enabler / Support), le pied de p.2 en donne l'impact (commodity / parity / differentiating), le quadrant p.3 en tire les priorités, la conclusion p.3 les relie à la posture TOWS de p.1. |

### 0.1 Niveaux d'élaboration autorisés

| Niveau | Définition | Exemples SPHERE | Où c'est permis |
|---|---|---|---|
| N1 Fait sourcé | Recopié d'une source datée | CA 782 M€, 18 sites, DG V. Legros | partout |
| N2 Calcul | Opération simple sur N1, formule dans `figures[].calc` | ≈10 % de marge, 4,7 M€ = 1 % d'achats | Signalétique, Ordres de grandeur, Bénéfice |
| N3 Inférence d'analyste | Lecture argumentée à partir de plusieurs N1/N2 | « le prix se négocie face aux distributeurs » | « À retenir », Thèse, Lecture, pieds de page |
| N4 Jugement / proposition | Choix de priorisation ou de design | ★, thèmes, quadrant, posture W-O, MT/LT | p.2 ★, p.3, conclusion |
| Interdit | Chiffre inventé, ROI, pair non sourcé, personne non promotrice nommée, maturité notée sans preuve | — | nulle part |

### 0.2 Grammaire visuelle et code couleur

| Token | Hex | Rôle sémantique (jamais décoratif) | Où |
|---|---|---|---|
| `--navy` | #13213A | Zone de conviction : en-tête, carte d'idée maîtresse (**une carte sombre par rangée au plus**) | en-tête ; p.1 Thèse ; p.3 Transformation MT/LT ; flèche MARGE p.2 |
| `--teal` | #0C7185 | Conclusion et navigation : bande de pied, libellé « À retenir », renvois « → cas n », pastilles numérotées | toutes pages |
| `--blue` | #1F4E8C | Magnitude et rang : barres, numéros de drivers, liseré des activités principales, barres de stratégie | p.1 drivers et breakdown ; p.2 activités principales ; p.3 stratégie dominante |
| `--blue2` / `--blue3` | #6E93C4 / #B5C7E0 | Rangs secondaires de la même série | empilement canaux ; stratégie cash / différenciation |
| `--gold` | #C98A00 | Impact et manque : ★, jauge « Faible », owner manquant, case core × differentiating | p.1 board ; p.2 ★ ; p.3 quadrant, jauge |
| `--soft` | #F3F6FA | Contexte secondaire | activités de soutien p.2 ; cellules SWOT ; Ordres de grandeur |
| `--cyan-dark` | #0E5A79 | Titres de carte (capitales) | toutes cartes |

Typographie Carlito (métrique Calibri). Corps 9,5–10 pt, plancher 9 pt. Titre entité 25 pt, sous-titre 12 pt. A4 paysage, marges 10 mm, gouttière 2,8 mm, rayon 2,6 mm. En-tête 25 mm, pied à 6,5 mm du bas, ligne de sources à 1,6 mm.

### 0.3 En-tête, pied et ligne de sources (communs aux 3 pages)

| Élément | Règle | Méta-prompt |
|---|---|---|
| Kicker | `program`, identique sur les 3 pages | — |
| H1 | Nom de l'entité en capitales, rien d'autre | — |
| Sous-titre | **Message dominant de la page**, ≤ 120 caractères, une proposition + deux-points + mécanisme | « Écris la phrase qu'un associé dirait en tournant la page. Sujet = l'entité ou la chaîne de valeur, verbe au présent, un chiffre ou un nombre de leviers si possible. » |
| Pied (bande teal) | Libellé à gauche, une ou deux phrases à droite, gras autorisé (`**…**`) sur les mots-clés du quadrant | voir chaque page |
| Ligne de sources | ≤ 1 ligne, familles de sources datées, jamais d'URL. P.2 ajoute la définition des ★. | — |

---

## 1. Ordre de rédaction (chaîne de pensée globale)

On ne rédige pas dans l'ordre de lecture. Ordre imposé :

| Étape | Produit | Pourquoi dans cet ordre |
|---|---|---|
| 1 | `figures` (valeurs canoniques + calculs) | Tout le reste y renvoie ; évite les chiffres divergents |
| 2 | Signalétique + Activity breakdown | Base factuelle N1/N2 |
| 3 | Chaîne de Porter (9 activités, ★, bénéfices) | Localise la valeur avant de choisir les priorités |
| 4 | Drivers (5) | Dérivés des maillons ★★★ et des tensions financières |
| 5 | Thèmes (3–5) + Transformation MT/LT | Chaque driver est couvert par un thème ou par MT/LT (G-C2) |
| 6 | Renvois p.2 → thèmes | Fermeture de la traçabilité (G-C1) |
| 7 | Magic Quadrant | Placement des activités ; thèmes numérotés (G-C3) |
| 8 | Board's empowerment | Qui peut porter les thèmes 1–3 |
| 9 | SWOT → posture TOWS | Les forces et faiblesses sont maintenant connues |
| 10 | Diagnostic public IA + Stratégie dominante | Dérivés des thèmes et de la recherche |
| 11 | Thèse | Écrite en dernier des cartes : résume sans répéter |
| 12 | Sous-titres, « À retenir », pieds, conclusion | Couche de conviction, relue d'un bloc pour la cohérence |
| 13 | Contrôles | `render_exec.py` (cohérence) puis `qa.py` (mise en page) puis lecture des PNG |

---

## 2. Graphe des renvois entre cadres

| Cadre source | Alimente | Nature du lien |
|---|---|---|
| P1 Signalétique | P1 Drivers, P2 Ordres de grandeur, P3 thème 1 et 3 (bénéfices) | mêmes `figures` |
| P1 Activity breakdown | P1 SWOT (menace distributeurs), P2 Marketing et ventes, P3 thème 1 (indexation) | canal GD 65 % → pouvoir de prix |
| P1 Drivers | P3 Thèmes (via `themes[].drivers`), P3 Transformation (`covers`) | couverture 100 % (G-C2) |
| P1 Board | P3 Transformation, P3 Diagnostic public | sponsors des MT/LT ; owner manquant = frein |
| P1 SWOT → posture | P3 Conclusion | même posture, même libellé (G-C4) |
| P1 pied (lecture activité) | P3 Magic Quadrant (lignes) | classement Core / Enabler / Support |
| P2 Porter ★★★ | P3 Thèmes | renvoi « → cas n » obligatoire (G-C1) |
| P2 pied (impact) | P3 Magic Quadrant (colonnes) | parity vs differentiating |
| P2 Ordres de grandeur | P3 Bénéfices des thèmes 1 et 3 | mêmes chiffres |
| P3 Thèmes | P3 Stratégie dominante | calcul automatique par `strategy_family` (G-C6) |
| P3 Thèmes + Quadrant | P3 Conclusion | ordre des priorités |

---

## 3. Page 1 — Où se crée la valeur

Grille : rangée haute 76 mm (3 colonnes 1,12 / 0,92 / 1 fr), rangée basse (0,86 / 0,92 / 1,42 fr). Sous-titre SPHERE : « Un leader européen de l'emballage en consolidation : la valeur se joue sur la marge matière, l'usine et le cash ».

### 3.1 Signalétique — rangée haute, colonne 1, carte blanche

| Axe | Spécification |
|---|---|
| Question | « Qui est l'entreprise, combien pèse-t-elle, où est sa tension économique ? » |
| Entrées | Communiqué le plus récent (taille), rapport annuel (P&L, bilan), communiqué d'entrée de l'actionnaire, acquisitions. SPHERE : S02, S03, S06. |
| Niveau | N1 et N2 uniquement. |
| Forme | 6 lignes clé/valeur, clés ≤ 14 caractères : Activité · Actionnariat · Taille · Économie (année) · Capital (année) · Croissance. Une ligne ≤ 2 lignes rendues. Chiffres via `{clé}`. |
| « À retenir » | La tension économique principale traduite en sensibilité : « marge étroite et 60 % du CA en matière : 1 % d'achats en moins vaut ≈6 % de l'EBITDA ». |
| Renvois | Mêmes chiffres que P2 Ordres de grandeur et P3 bénéfices (G-C5). |

> **Méta-prompt** — « À partir des sources financières et corporate datées, remplis 6 lignes. Une ligne = un fait ou un calcul simple, avec son année. N'écris ni classement de marché, ni qualificatif. Choisis pour "À retenir" le ratio qui met le plus d'EBITDA en jeu (achats/CA, stocks/CA, masse salariale/CA, énergie/CA) et exprime-le en sensibilité : 1 point de ce poste = x % de l'EBITDA. »

Chaîne de pensée : (1) repérer le poste de coût ou de capital dominant ; (2) calculer 1 % de ce poste ÷ EBITDA ; (3) vérifier l'année de chaque chiffre ; (4) écrire la croissance à périmètre constant si publiée, sinon la croissance publiée + l'acquisition.
Pièges : mélanger CA 2025 et EBITDA 2024 sans l'année ; écrire une capacité (235 kt) comme taux d'utilisation.
Audit rétrospectif SPHERE : cohérent. Point faible : « Polyex acquis (09/2026) », la date juridique de closing n'étant pas établie (le communiqué dit « has acquired »). Acceptable en `exec`.

### 3.2 Thèse — rangée haute, colonne 2, carte navy

| Axe | Spécification |
|---|---|
| Question | « Quelle est l'histoire de création de valeur, en deux phrases ? » |
| Entrées | Signalétique, drivers, posture TOWS, thèmes (écrite en dernier). |
| Niveau | N3. |
| Forme | 2 paragraphes : (1) ce qu'est l'entreprise, structurellement (≤ 15 mots) ; (2) le mécanisme de création de valeur + le rôle exact de l'IA (≤ 40 mots). Corps 11 pt. |
| « À retenir » | Maxime de 3 à 5 mots, impérative : « intégrer avant d'innover ». |
| Renvois | Doit annoncer la conclusion p.3 sans la répéter. |

> **Méta-prompt** — « Écris la thèse comme un associé d'investissement. Phrase 1 : la nature structurelle de l'entreprise (plateforme, leader de niche, groupe familial en transition…). Phrase 2 : ce qui crée la valeur maintenant, puis la place de l'IA (accélérateur, levier, prérequis) en une proposition. Interdit : liste de technologies, promesse chiffrée. "À retenir" = maxime d'action de 3 à 5 mots. »

Audit : cohérent avec la posture W-O et la conclusion. C'est la seule carte navy de la rangée.

### 3.3 Drivers de valeur — rangée haute, colonne 3, carte blanche

| Axe | Spécification |
|---|---|
| Question | « Sur quels 5 leviers la valeur se joue-t-elle, par ordre ? » |
| Entrées | Maillons ★★★ de P2, ratios de la signalétique, drivers du bundle (DRV-xx, hiérarchie D01–D06). |
| Niveau | N3 (hiérarchie d'analyste). |
| Forme | Exactement 5 drivers numérotés (pastilles bleues). Libellé en gras de 1 à 2 mots, tiret, mécanisme ≤ 12 mots. Ordre : protection (marge, rendement, cash) puis construction (intégration, différenciation). |
| « À retenir » | La logique de l'ordre : « les trois premiers protègent marge et cash ; les deux derniers construisent l'avantage ». |
| Renvois | Chaque `drivers[].id` est couvert par un thème p.3 ou par la transformation MT/LT (G-C2). |

> **Méta-prompt** — « Traduis la hiérarchie des drivers du bundle en 5 leviers métier, sans code. Mets en premier les leviers qui protègent l'EBITDA et le cash, puis ceux qui construisent l'avantage. Chaque mécanisme dit ce qu'on pilote, pas l'outil. »

Audit : le bundle compte 9 drivers techniques (D01a/b, D03a/b/c…). Le regroupement en 5 est une compression assumée. D03b/c (créances, fournisseurs) sont absorbés dans « Cash ».

### 3.4 Activity breakdown — rangée basse, colonne 1, carte blanche

| Axe | Spécification |
|---|---|
| Question | « Où se fait le CA, et qu'est-ce que cela dit du pouvoir de négociation ? » |
| Entrées | Ventilation produits, clients et géographie du rapport annuel (SPHERE : S03 p.17). |
| Niveau | N1 pour les barres ; N3 pour « À retenir ». |
| Forme | Barres horizontales à une seule teinte (bleu), normalisées sur la plus grande valeur ; un empilement canaux (bleu → bleu2 → bleu3), libellés dans les segments ; une ligne géographie. Pas de légende. Graphe validé avec la skill `dataviz` (une série = une teinte). |
| « À retenir » | Concentration + canal dominant → conséquence sur prix ou mix. |
| Renvois | Menace « pouvoir des distributeurs » (SWOT) ; activité « Marketing et ventes » (P2) ; thème 1 (indexation). |

> **Méta-prompt** — « Montre la ventilation publiée la plus récente. Dans "À retenir", additionne les 2 ou 3 premières familles, nomme le canal dominant et déduis-en qui détient le pouvoir de prix. Si une dimension n'est pas publiée, ne l'affiche pas : n'écris pas qu'elle manque. »

Audit : titre en anglais (« Activity breakdown ») conservé à la demande de François ; les autres titres sont en français. Le libellé « Entr. 32 % » est abrégé pour tenir dans le segment.

### 3.5 Board's empowerment & ownership — rangée basse, colonne 2, carte blanche

| Axe | Spécification |
|---|---|
| Question | « Qui a le mandat et l'intérêt de porter une transformation par la donnée ? » |
| Entrées | Registre légal (mandataires), communiqués de nomination, communiqué de l'actionnaire, cas clients cabinet (sponsors nommés). SPHERE : Pappers, ponts.org, S06, P01. |
| Niveau | N1 pour les rôles ; N3 pour le rôle de promoteur (déduit du parcours ou du chantier sponsorisé). |
| Forme | Ligne d'intention (« Objectif : qui peut porter la transformation data ? »), puis 3 promoteurs max au format **Nom, titre (année)** — preuve du parcours ou du chantier : *rôle naturel* (teal). Dernière ligne en or : l'owner manquant. |
| Filtre | Ne lister que les promoteurs ou owners naturels (mandat + signal de parcours ou de sponsoring). **Ignorer** les salariés sans mandat groupe (ex. DSI de filiales). Jamais de COO/DSI déduit d'un titre voisin. |
| « À retenir » | Niveau d'empowerment (fort / partiel / faible) + ce qui manque pour l'ownership de la plateforme. |
| Renvois | Sponsors de la transformation MT/LT (P3) ; l'owner manquant explique la jauge « Faible » (P3 Diagnostic public). |

> **Méta-prompt** — « Cherche d'abord le registre légal du holding, puis les nominations récentes, puis les cas clients où un dirigeant est cité. Retiens au plus 3 promoteurs. Pour chacun : fonction exacte, année, une preuve de parcours ou de sponsoring, puis le rôle naturel qu'il peut tenir. Termine par la fonction absente qui bloquerait l'ownership (owner industriel, DSI, CDO). Ne nomme jamais un salarié non mandataire. »

Chaîne de pensée : mandataires → parcours (industriel, financier, commercial) → chantier sponsorisé visible → rôle naturel (excellence opérationnelle, cash, croissance) → fonction manquante.
Audit : c'est la carte la plus sensible. V. Legros (DG) est daté par le RNE au 20/01/2026 et par l'annonce ponts.org au 26/05/2026 ; « (2026) » neutralise l'écart. **À confirmer par une source primaire avant l'entretien.**

### 3.6 SWOT → posture TOWS — rangée basse, colonne 3 (la plus large), carte blanche

| Axe | Spécification |
|---|---|
| Question | « Quelle posture stratégique l'entreprise adopte-t-elle aujourd'hui ? » |
| Entrées | Tous les faits de la page, marché (analysis/02), réglementation, preuves d'innovation, recherche Ishikawa. |
| Niveau | N1 dans les cases ; N3/N4 pour la posture. |
| Forme | 2×2 sur fond `soft`, 3 puces ≤ 7 mots par case. En dessous, 4 postures TOWS en pastilles : Offensive S-O · Défensive S-T · Veille W-T · **Opportuniste W-O**. La posture actuelle est en navy, avec « · actuelle ». |
| Règle de posture | Déduire de ce que l'entreprise **fait** : acquisitions, réorganisations, offres. Utiliser des opportunités pour corriger des faiblesses → W-O ; exploiter des forces sur des opportunités → S-O ; défendre des forces contre des menaces → S-T ; réduire l'exposition → W-T. |
| « À retenir » | « posture [libellé] ([code]) : [actions observées] servent à [effet] ». Le couple libellé + code doit être repris mot pour mot dans la conclusion p.3 (G-C4). |
| Renvois | Conclusion p.3 ; l'option offensive (S-O) de la conclusion vient d'une force de cette carte (brevets biosourcés). |

> **Méta-prompt** — « Remplis la SWOT avec des faits courts. Puis regarde les 3 derniers mouvements de l'entreprise et demande-toi : répondent-ils à une faiblesse ou exploitent-ils une force ? Face à une opportunité ou à une menace ? Allume une seule posture. Écris-la avec son libellé et son code, exactement comme tu l'écriras dans la conclusion. »

Audit : « Leader européen du ménager » est une revendication de l'entreprise, recopiée comme force. C'est acceptable en `exec`, mais c'est la phrase la plus exposée à une objection en entretien.

### 3.7 Pied p.1 — « Magic Quadrant · lecture activité »

> **Méta-prompt** — « Classe toutes les activités en trois rôles. **Core** : ce qui transforme ou vend le produit et porte la différenciation possible. **Enabler** : ce qui coordonne les flux (planification, stocks, ERP, données). **Support** : ce qui administre (finance, conformité, encaissement). Une phrase par rôle, en commençant par le mot en gras. »

Règle clé : le rôle (Core / Enabler / Support) est **indépendant** du type Porter de la p.2. Exemple SPHERE : « Logistique aval » est une activité principale de Porter mais un Enabler au quadrant, parce qu'elle coordonne les flux sans porter de différenciation.

---

## 4. Page 2 — Où agir dans la chaîne de valeur

Grille : bloc Porter (activités de soutien en haut, activités principales en bas, flèche MARGE à droite) ; rangée basse de 36 mm (Ordres de grandeur 1,25 fr, Lecture 1 fr). Sous-titre : nombre de maillons ★★★ et leur nom.

### 4.1 Cellule d'activité Porter (×9) — cartes `soft` (soutien) ou blanches à liseré bleu (principales)

| Axe | Spécification |
|---|---|
| Question | « En quoi consiste ce maillon chez cette entreprise, et quel bénéfice y viser ? » |
| Structure | 4 activités de soutien (Approvisionnement, Développement technologique, Infrastructure, Ressources humaines) et 5 principales (Logistique amont, Production, Logistique aval, Marketing et ventes, Services). Les noms Porter sont fixes et l'ordre ne change pas (G-S6). |
| Entrées | Signalétique, activités du bundle (value_chain), innovations, cas cabinet. |
| Niveau | Description N1 (un fait chiffré par cellule si possible) ; bénéfice N3 ; ★ N4. |
| Forme | Titre en gras + ★ (or, 1 à 3) ; description ≤ 20 mots avec **un fait propre à l'entreprise** ; « **Bénéfice :** » ≤ 6 mots ; pastille teal « → cas n », « → transformation MT » ou « hors priorités » (gris). |
| Barème ★ | ★★★ = poste qui pèse directement sur la marge ou le cash (≥ 10 % du CA, ou tension documentée) ; ★★ = levier réel mais indirect ou plus long ; ★ = hygiène. |
| Règle de renvoi | Tout ★★★ renvoie à un thème ou à la transformation (G-C1). L'ensemble des renvois = l'ensemble des thèmes (G-C1). |

> **Méta-prompt** — « Pour chacune des 9 activités de Porter, écris ce que l'entreprise y fait en un fait concret (montant, volume, brevets, sites, outil observé). Si l'activité est obscure pour un lecteur non spécialiste (ex. R&D matériaux), décris son actif (brevets, filiale, équipe) plutôt que son process. Donne le bénéfice attendu en 2 à 6 mots, attribue les ★ selon le barème, puis relie chaque ★★★ au thème qui le traite. »

Audit : « Ressources humaines — compétences data et IA non visibles » est la seule mention d'un manque sur la page. Elle est justifiée, car elle prépare la jauge « Faible » de p.3.

### 4.2 Flèche MARGE — colonne de droite, navy

Rappel visuel de Porter : la marge naît de la chaîne. Sous-libellé = `EBITDA {marge}`. Aucune autre information.

### 4.3 Ordres de grandeur — rangée basse gauche, carte `soft`

| Axe | Spécification |
|---|---|
| Question | « Quel levier pèse le plus, en euros ? » |
| Niveau | N2 exclusivement, avec formule dans `figures[].calc`. |
| Forme | 3 métriques côte à côte : valeur 15 pt + une ligne d'explication. Pas de disclaimer (« pas un business case » est interdit, G-P4). |
| « À retenir » | Le levier dominant, en une phrase. |
| Renvois | Mêmes clés que la signalétique et les bénéfices p.3 (G-C5). |

> **Méta-prompt** — « Choisis 3 sensibilités : 1 % du poste de coût dominant, 10 % du capital immobilisé dominant, et un troisième poste significatif (énergie, masse salariale, transport). Chaque valeur vient d'un calcul explicite dans figures. N'annonce ni gain ni ROI. »

### 4.4 Lecture — rangée basse droite, carte blanche

> **Méta-prompt** — « Compte les maillons ★★★ et regroupe-les en deux familles (ex. matière et usine / flux et vente). Une phrase. "À retenir" dit où l'IA crée de la valeur et où elle n'en crée pas. »

Audit : le compte « quatre maillons ★★★ » doit correspondre au sous-titre ; `page2.top_count` le déclare et le renderer le vérifie (G-C7).

### 4.5 Pied p.2 — « Magic Quadrant · impact »

> **Méta-prompt** — « Donne l'impact bottom line par zone du quadrant : quelles activités Core sont en parité (impact fort mais sans différenciation), quel est le seul candidat différenciant, ce que les Enablers libèrent (souvent le cash). 2 à 3 phrases, mots-clés en gras. »

---

## 5. Page 3 — Quelles priorités

Grille : rangée haute (Magic Quadrant 108 mm | tableau des priorités) ; rangée basse de 40 mm (Transformation navy 1,15 fr | Diagnostic public 1 fr | Stratégie dominante 1 fr). Sous-titre : nombre de priorités + ordre + condition de la différenciation.

### 5.1 Magic Quadrant — carte blanche, grille 3×3

| Axe | Spécification |
|---|---|
| Question | « Où sont les capacités, et laquelle peut différencier ? » |
| Axes | Lignes Core / Enabler / Support (issues du pied p.1) ; colonnes Commodity / Parity / Differentiating (issues du pied p.2). Ce n'est pas une matrice BCG. |
| Forme | Cases vides en pointillés, cases occupées en bleu pâle, case Core × Differentiating en or (zone cible). Pastilles « activité » avec numéro teal du thème qui la traite. 8 à 10 pastilles. |
| « À retenir » | Priorité core + seul candidat différenciant. Si l'information publique ne suffit pas : « l'information publique ne permet pas d'aller plus loin ». |
| Contrôles | Chaque thème apparaît au moins une fois dans le quadrant (G-C3) ; au moins 2 lignes occupées, ou la phrase de limite (G-C3). |

> **Méta-prompt** — « Place chaque activité selon deux questions. Centralité : transforme-t-elle ou vend-elle le produit (Core), coordonne-t-elle (Enabler), administre-t-elle (Support) ? Différenciation : les pairs font-ils pareil (Parity), est-ce standardisé et achetable (Commodity), existe-t-il un actif rare et prouvé (Differentiating) ? Ne mets en Differentiating que ce qui a une preuve d'actif (brevets, part de marché, prime de prix). »

Audit : « Ventes, SPHERE PRO » porte le thème 4 en Core × Parity alors que le thème 4 figure aussi en Core × Differentiating (biosourcés). C'est voulu : un même thème mobilise deux capacités.

### 5.2 Priorités IA · bénéfice, avantage, caractéristique — tableau

| Axe | Spécification |
|---|---|
| Question | « Quelles 3 à 5 priorités, dans quel ordre, et pourquoi elles créent un avantage ? » |
| Structure | 5 colonnes : Priorité · Changement · Bénéfice · Avantage compétitif · Caractéristique (grille **B-A-C**). La colonne Priorité contient pastille, nom en gras, ★, puis en gris « activité → stratégie · horizon ». |
| Reranker | Regrouper les cas du bundle par workflow en 3 à 5 thèmes (G-S9). Classer par ★ puis par famille de stratégie (coûts > cash > différenciation) sauf thèse contraire. Les cas hors thème restent dans le bundle et ne sont pas mentionnés. |
| Niveau | Changement N4 ; bénéfice N2/N3 (réutiliser `figures`) ; avantage N3/N4 ; caractéristique = classe technique (ML, vision, optimisation, GenAI), jamais un fournisseur. |
| Forme | Cellules ≤ 12 mots ; aucune légende sous le tableau. |
| « À retenir » | La logique d'enchaînement des priorités (« trois priorités d'efficience financent la quatrième… »). |

> **Méta-prompt** — « Regroupe les cas d'usage en 3 à 5 thèmes nommés comme des programmes de direction ("Pilotage de la marge matière", pas "détection d'anomalies"). Pour chacun : quelle activité, quelle stratégie de valeur, quel changement concret dans le travail, puis Bénéfice (ce que gagne l'entreprise, chiffré via figures si possible), Avantage (ce que cela change face aux pairs), Caractéristique (la classe technique). Le thème de différenciation vient en dernier sauf si la posture est offensive. »

Audit : « Répercuter la volatilité plus vite que les pairs » et « Délais face aux importations » sont des hypothèses N4. La formulation sans conditionnel est assumée en `exec`, mais ces deux points doivent être défendus à l'oral.

### 5.3 Transformation MT / LT — carte navy

| Axe | Spécification |
|---|---|
| Question | « Vers quoi l'entreprise se transforme-t-elle, au-delà des priorités ? » |
| Forme | 2 paragraphes en gras : **MT, 12–24 mois** (pilotage unifié par la donnée des opérations) et **LT, 24–48 mois** (passage à un modèle prédictif de bout en bout). |
| Couverture | Couvre les drivers transverses non traités par un thème (SPHERE : Intégration) via `transformation.covers` (G-C2). |
| « À retenir » | Formule de trajectoire de 3 à 5 mots : « de l'intégration au prédictif ». |

> **Méta-prompt** — « MT : quel pilotage unifié par la donnée rend la plateforme gouvernable (rythme de production, qualité, consommables, flux) ? LT : quel modèle prédictif relie la demande aux opérations et aux achats ? Pas de technologie nommée, pas de budget. »

### 5.4 Diagnostic public · IA, data, ML — carte blanche

| Axe | Spécification |
|---|---|
| Question | « Que montre l'extérieur de la maturité data/IA ? » |
| Forme | Jauge à 3 cases (Faible / Partiel / Établi, la case active en or) + 2 à 3 faits observés. Aucune note sur 8 dimensions en page (elle reste dans le bundle). |
| Règle de jauge | Faible = socle ERP/process sans équipe ni cas IA publics ; Partiel = équipe data ou cas IA publics isolés ; Établi = cas en production cités + organisation data visible. |
| « À retenir » | Socle existant + capacité à construire. |

> **Méta-prompt** — « Liste ce qui est observable publiquement (ERP, S&OP, équipe data, offres d'emploi, cas IA cités). Choisis la case de la jauge selon la règle. Formule le manque comme un chantier ("capacité IA à construire"), pas comme un disclaimer. »

### 5.5 Stratégie dominante — carte blanche

| Axe | Spécification |
|---|---|
| Question | « Quelle stratégie de valeur domine le portefeuille de priorités ? » |
| Calcul | **Dérivée automatiquement** des `themes[].strategy_family` : la famille qui regroupe le plus de thèmes prend la barre pleine. Aucune saisie manuelle (G-C6). |
| Forme | 2 à 4 lignes : libellé + barre bleue graduée avec « priorités n et m ». |
| « À retenir » | Séquence stratégique (« résilience de marge et efficience d'abord ; différenciation ensuite »). |

### 5.6 Pied p.3 — « Conclusion »

> **Méta-prompt** — « Une ou deux phrases stratégiques. Commence par la posture de p.1 (même libellé, même code). Dis ce que l'entreprise doit devenir, l'ordre dans lequel l'IA sert les priorités, puis l'option offensive (S-O) et sa condition. Aucun chiffre nouveau. »

Audit SPHERE : « Posture opportuniste (W-O) : SPHERE doit transformer sa consolidation en plateforme pilotée par la donnée. L'IA sert d'abord la marge matière et l'usine, puis le cash ; la différenciation biosourcée devient l'option offensive (S-O) une fois la donnée unifiée. » Elle reprend p.1 (posture), p.3 (ordre des thèmes) et le quadrant (seul différenciant).

---

## 6. Contrôles et tests associés

| Code | Contrôle | Où | Test |
|---|---|---|---|
| G-P1 | Chaque carte a un « À retenir » non vide | renderer | `test_missing_takeaway` |
| G-P2..P5 | Expressions interdites et IDs internes absents | renderer | `test_forbidden_disclaimer`, `test_internal_id` |
| G-S6 | Porter = 4 + 5 | renderer | `test_porter_shape` |
| G-S9 | 3 à 5 thèmes | renderer | `test_too_many_themes` |
| G-C1 | Renvois p.2 = thèmes p.3 ; tout ★★★ renvoie | renderer | `test_orphan_theme_p2`, `test_three_star_without_ref` |
| G-C2 | Tout driver couvert | renderer | `test_driver_not_covered` |
| G-C3 | Thèmes présents dans le quadrant ; quadrant non dégénéré | renderer | `test_theme_missing_in_quadrant` |
| G-C4 | Posture identique p.1 / conclusion | renderer | `test_posture_mismatch` |
| G-C5 | Chiffres canoniques uniquement | renderer | `test_non_canonical_figure` |
| G-C6 | Stratégie dominante dérivée des thèmes | renderer | `test_strategy_family_without_theme` |
| G-C7 | Nombre de ★★★ = `page2.top_count` annoncé au sous-titre | renderer | `test_top_count_mismatch` |
| QA-L | 3 pages, 0 overlap/overflow, ≥ 9 pt, padding ≥ 9 pt | qa.py | `qa.json pass: true` |
| QA-V | Lecture des 3 PNG à 100 % | humain / agent | obligatoire |

## 7. Ce qui reste un jugement humain

- Le barème ★ et le placement dans le quadrant : deux analystes peuvent diverger d'un cran.
- La posture TOWS : elle se défend par les 3 mouvements observés ; à reformuler si l'entreprise change de cap.
- Les promoteurs du board : l'inférence « promoteur de… » repose sur le parcours, pas sur une déclaration.
- Les avantages compétitifs des thèmes : hypothèses à tester en entretien ou en due diligence.
