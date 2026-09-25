# Agent routeur — Hivest Portfolio AI

Profil François-Pro. Objet : diagnostiquer les entreprises du portefeuille et la création de valeur IA ; exclure product matching et recommandations fournisseur.

1. Lire `program/state.json`, **un** `companies/<id>/manifest.json`, puis `companies/<id>/INDEX.md` s'il existe. Vérifier le gate courant avant de choisir l'étape. Le manifest, les contrats et les preuves priment sur un ancien handoff ou un document narratif.
2. Lire le [workflow de la skill unique](skills/hivest-portfolio-ai/references/workflow.md) ; charger **une seule procédure métier de l'étape** et ses seules références conditionnelles. Les entrées, sorties et passages à la suite y sont indiqués. Ne pas charger tout `docs/`, `companies/` ou `tests/`.
3. Appliquer les [invariants et gates](docs/agent/gates.md). Pour une reprise, une recherche en branches ou un changement d'étape, appliquer le [contrat de contexte et checkpoint](docs/agent/context-and-resume.md).
4. Vérifier les fichiers, références, décisions et contrôles de sortie avant de changer le manifest ou de passer la main. Une validation de schéma, un PDF existant ou une fixture ne valent pas approbation humaine.

Rôles : l'orchestrateur route, vérifie les gates et intègre ; le rôle research collecte et qualifie. Un rôle n'impose ni un nouvel agent ni une nouvelle skill. Les procédures peuvent être exécutées séquentiellement par un seul agent. Garder le contexte limité à une entreprise, une étape, les claims décisifs et leurs contre-preuves.

Carte des commandes et capacités réellement codées : [docs/architecture/code-map.md](docs/architecture/code-map.md). Ce fichier est le point d'entrée ; les règles détaillées restent à leurs chemins explicites ci-dessus.
