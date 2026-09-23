# Catch-up sur `main` — profil exec v0.3

## Provenance et état

Le dépôt local initial était en retard ; après `git fetch`, `origin/main` était au commit `3ebd6a8`, base exacte du loopback Claude. L'intégration a été rebasée sur ce commit. Sphere dispose d'un package et d'un contexte v0.2 dont la validation structurelle passe. Les originaux de trois sources matérielles (S02, S03, S06) et l'archive des extraits ne sont pas vérifiés localement ; le pré-HITL échoue explicitement. Les sources S-L01, S-L02 et S-I01 citées dans le rendu reçu ne sont pas dans ce bundle.

Le PDF et le payload externes sont datés du 24/09/2026, alors que le bundle Sphere est arrêté au 23/09/2026. Le payload est conservé comme fixture de présentation et le manifeste est `UNVERIFIED_DEMO`. La déclaration externe d'une validation propriétaire et d'une identité visuelle « au pixel près » n'est pas une attestation issue de ce dépôt.

## Changements intégrés

- Profil exec séparé du profil audit : schéma, template rétro-documenté, renderer HTML/PDF/PNG, QA DOM, NRT de cohérence. Le PDF reçu a été inspecté sur trois pages ; le renderer PDF intégré n'a pas pu être exécuté ici faute de Chromium. Job `render-qa` déclenchable en CI.
- Schéma détaillé pour leaders, segments, liens d'opportunité et reviews ; montants financiers en chaînes décimales. Le validateur autorise des dirigeants groupe **sourcés**, conserve COO/DSI et rejette une promotion de dirigeant de filiale.
- `compose_dossier.py` lit l'identité, la date, le statut et la version du manifest/package. Le test de registre n'impose plus exactement 22 lignes.
- Capture par source : l'original est exigé pour les sources matérielles déclarées et les registres/filings ; les extraits autorisés par les droits requièrent hash et archive contrôlée. Aucune donnée manquante n'a été fabriquée.
- Liaison facultative du rendu à un bundle contrôlé (`--bundle` et `--archive`) : cutoff, sources des figures et hash du bundle sont comparés. Sans ces entrées, le renderer reste une démonstration non vérifiée.

## Travail restant

1. Archiver et vérifier les captures originales de S02/S03/S06 ainsi que les extraits autorisés ; recouper les claims. La politique de capture est un gate technique, pas un jugement de vérité.
2. Acquérir et dater S-L01/S-L02/S-I01, puis seulement ensuite décider si les mandataires et chiffres ajoutés au payload peuvent entrer dans le bundle. Régénérer les hashes des artefacts touchés.
3. Passer le template sur STG après l'intake et la recherche, avec un payload seul et la QA des trois PNG. Le cadre est candidat jusqu'à ce deuxième essai et au loopback.
4. Rendre le graphe de dépendances granulaire à la carte, renforcer la rédaction du diagnostic Porter/TOWS et produire les revues avant tout GO_DRAFT.

Ni les tests du renderer ni la validation structurelle du bundle ne clôturent `GO_DRAFT`, `FROZEN`, `RENDERED` ou `DONE`.
