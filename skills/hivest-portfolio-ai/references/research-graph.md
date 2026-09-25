# Wiki de recherche et contrats de reprise

**Contrat conditionnel.** Entrée : manifest, index/graph s'ils existent et question décisionnelle. Sortie : questions bornées, dépendances et checkpoint ; aucune promotion automatique en fait. **Retour :** étape suspendue, généralement [evidence.md](evidence.md) ou [review.md](review.md). Contrat complet : [workflow.md](workflow.md).


## Granularité et contexte
Ne pas maximiser profondeur ou nombre de fichiers. Une page par question décisionnelle stable,300–900 mots indicatifs ; scinder seulement quand les sources ou cycles de mise à jour divergent. Ne pas créer un fichier par phrase. Index court, liens typés et chemins exacts ; profondeur habituelle≤4 niveaux sous racine. Lire manifest→index→artefact cible→claims décisifs, jamais le corpus entier. Budget initial12 claims, élargir pour contradictions ; aucune perte silencieuse si budget dépassé.

Séparer raw/extraits acquis immuables hors code, fragments exacts, claims, wiki sectorielle, analyse entreprise et vues rendues. Le rapport final est une projection, pas la mémoire primaire. Registre central par source, hashes des octets réellement conservés et capture_kind explicite : un extrait n’est pas un HTML/PDF complet. Ne pas fabriquer un hash d’original avec une synthèse. Promouvoir dans le dépôt uniquement références, connaissances canoniques et fixtures revues ; runs et archives raw restent externes.

## Graphe exécutable, mind map comme vue
Nœuds typés : source/claim/analysis/question/output ; arêtes supports/depends_on/contradicts/answers. Une question porte état, owner, déclencheur, impact, bornes de recherche et condition d’arrêt. Un changement de source, contradiction, fraîcheur dépassée ou question critique invalide uniquement les descendants ; aucune recherche permanente ou automatique sans déclencheur matériel. Le routeur émet un paquet de travail, l’agent exécute la recherche au prochain run autorisé. Ce n’est pas une tâche planifiée en arrière-plan.

Les contrats et artefacts sources restent autorité ; la mind map est une vue navigable du graphe, pas un moteur autonome. Les dépendances des outputs doivent inclure les critères absents, pas seulement les faits connus.

## Travail parallèle et intégration
Paralléliser angles indépendants marché, leadership, technique avec même cutoff, IDs réservés et fichiers distincts. Chaque rôle reçoit question/scope/entrées attendues/budget, rend source+fragment+claim+limite. Un intégrateur unique déduplique origines, résout entités et contradictions ; seul lui modifie package, index et état. Aucun agent ne fusionne une conclusion d’un autre sans preuve. Verrou optimiste par hash/version avant promotion ; pas de remplacement aveugle des edits concurrents.

## Contrat de contenu avant shortlist
Produire segmentation produit/canal/pays séparée ; CA et croissance datés et réconciliés ; 4P ; cinq forces Porter par segment ; concurrence nationale/internationale avec ownership ; SWOT dérivée ; VRIO et couverture7S. Ne pas appeler top3 un panel. BCG exige croissance du marché EXTERNE et part RELATIVE ; CA interne ne suffit pas. Un manque connu devient question ciblée, pas valeur estimée pour remplir.

## Leadership et champ ML obligatoires
Pour chaque ligne : COO et DSI, noms nullable, titre exact, groupe/filiale, dates, URL, statut de preuve et prochaine validation. Pour les mandataires : registre légal du holding → nominations datées → cas clients citant un dirigeant → LinkedIn public indexé ; puis rechercher les rôles opérationnels, le recrutement et les prestataires. Pas de contournement d’accès. Ne pas substituer CEO→COO ou CIO filiale→groupe. Distinguer inconnue et absence. Renseigner `promoter_signal` et `ownership_scope` seulement si leur preuve est liée au rôle. Équipes data/BI/ML/IA : effectif, manager, interne/externe, projets, production, MLOps ; chaque inconnu reste visible dans le pitch.

Séparer stratégie ML observée et proposée ; modèle candidat, baseline sans ML, données/labels, validation temporelle et intersites, risque de fuite, coût d’erreur, monitoring/owner/repli. Distinguer vision, prévision, optimisation mathématique, scoring et GenAI. Capacité éditeur≠installation entreprise ; versions/connecteurs/licences et droits d’écriture doivent être vérifiés. Aucun code de table ne justifie écriture directe en base.

## Loopback et tests
Après revue : défaut→cause→règle→contrat→artefact touché→NRT. Trois revues séparées (conformité, explication alternative, utilité) avec verdict codé. Exécuter tests sur le dossier réel et tests de mutation (faux scope, null→score, BCG sans variables, source modifiée). Différencier package structurellement valide, preuves intègres, contenu sémantiquement couvert et décision humaine GO_DRAFT. Les versions legacy sont lisibles mais ne permettent pas un nouveau freeze.

Respecter les gates du dépôt actif après fusion concurrente : les extraits vérifiés ne ferment pas le gate d’archivage des originaux. Garder RESEARCH tant que check_prehitl échoue. La projection contenu reste v0.1 ; ne pas déclarer un freeze v0.2 disponible avant migration du contrat de rendu.
