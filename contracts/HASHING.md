# Hashes de preuves et de gel

- Fragment : SHA-256 des octets UTF-8 de l'extrait normalisé en Unicode NFC. Ne pas normaliser les espaces ni remplacer les caractères typographiques : vérifier l'extrait sur la capture d'origine.
- Package et payload : `json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))` encodé UTF-8, puis SHA-256. Conserver les nombres entiers et éviter les floats pour les montants financiers : utiliser des chaînes décimales documentées.
- Le hash du snapshot source porte sur les octets du fichier capturé, sans transformation. Le validateur actuel ne télécharge pas les snapshots ; une revue d'acquisition distincte doit vérifier URI, contenu et droits avant HITL.
- Changer une méthode de canonicalisation exige une migration explicite des hashes et une nouvelle revue humaine des packages gelés.
