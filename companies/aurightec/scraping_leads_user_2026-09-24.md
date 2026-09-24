# Pistes de collecte reçues — Aurightec, 24/09/2026

**Statut : input utilisateur, non preuve.** Périmètre proposé : Tallinn, Suzhou, Kulim et holding française ; cutoff 23/09/2026. Le texte source contient des grades suggérés et des règles d'ingestion non validés. Aucun résultat négatif, certificat, brevet, poste, client ou fournisseur n'en est déduit.

## Règles de reprise corrigées

- Filtrer par **entité juridique, date, relation et activité**, pas par présence/absence de tokens dans une page entière. La France est indispensable pour la holding et la cession française/marocaine sert de contre-périmètre. Garder les captures avec un tag `OUT_OF_SCOPE` et justification ; ne pas détruire un original acquis.
- Une recherche sans résultat visible s'enregistre comme `not_found_in_query` avec moteur, requête, date et limites de couverture ; elle ne prouve ni absence de brevet, ni absence d'équipe.
- Conserver les octets originaux et leur SHA-256, URI externe et type de capture. Un MD5 de DOM ou une extraction ne satisfait pas le gate d'intégrité des originaux. Un court fragment localisé est distinct de la capture.
- Une base de contacts, un agrégateur, des données douanières commerciales ou BuiltWith ne deviennent pas automatiquement grade A. Un détecteur web ne prouve pas ERP/MES ou cloud industriel. Les grades sont attribués après lecture du document précis, indépendance et portée.

## Cibles ordonnées et décision d'ingestion

| Branche | URL fournie | Décision / limite |
|---|---|---|
| Identité Tallinn | https://ariregister.rik.ee/eng/company/10574032/Eolane-Tallinn-AS | **Rejet de l'ID :** l'entité vérifiée est Aurightec Estonia AS `10092440` [S-AUR-01,02]. Utiliser https://ariregister.rik.ee/est/company/10092440 et les comptes liés. |
| Holding | https://www.pappers.fr/recherche?q=Aurightec | Requête exploratoire ; la note 18 Tallinn nomme Financière de l'Ombrée, SIREN 413101957, et le BODACC confirme le dépôt des consolidés [S-AUR-02,15]. Pappers agrégateur [S-AUR-16], pas preuve primaire d'actionnariat ultime ou de chiffres. |
| Scission | https://vipress.net/aurightec-un-nouveau-nom-de-la-sous-traitance-bati-sur-ce-quil-reste-du-groupe-eolane/ | Presse spécialisée secondaire ; Cicor [S-AUR-04] et documents juridiques pour confirmer les actifs et dates. Ne pas exclure l'article parce qu'il mentionne France/Maroc. |
| Fiscalité/emploi | https://score.teatmik.ee/en/company/10574032/ | **ID erroné :** n'ingérer aucun chiffre sur cette base. Le rapport audité `10092440` contient déjà masse salariale et effectif [S-AUR-02]. |
| Positionnement | https://aurightec.com/ | Communication de l'entreprise ; offres et sites déclarés, pas parts de marché ni mix de ventes [S-AUR-05–08]. |
| Flux douaniers | https://www.volza.com/p/eolane-suzhou-co-ltd/ | Piste commerciale à identité et couverture à vérifier ; ne pas nommer NXP, STMicro ni des clients sans manifeste primaire lu et réconcilié. |
| Dirigeants | https://rocketreach.co/aurightec-profile_b48f9d | Piste de contacts faible, URL tronquée dans l'input ; vérifier titres, dates et périmètre dans registres et communications directes. COO/DSI restent inconnus. |
| IT web | https://builtwith.com/aurightec.com | Empreinte du site public uniquement ; aucune inférence sur ERP, cloud de production ou sécurité OT. |
| Certifications | https://www.iaob.org/ | Portail de recherche ; exiger certificat et organisme, entité/site, portée et dates. Aucun IATF Suzhou/Kulim promu. |
| Recrutement | https://www.cvkeskus.ee/joboffers/aurightec | Une annonce datée établirait un besoin, pas une équipe data ou une installation IA ; aucune annonce spécifique vérifiée. |
| Aides publiques | https://investinestonia.com/?s=Eolane+OR+Aurightec | Requête, pas décision de subvention ; ne pas intégrer de montant sans attribution officielle. |
| Brevets | https://patents.google.com/?assignee=Eolane+OR+Aurightec | Requête large à dédoublonner et vérifier par titulaire légal ; zéro résultat éventuel ≠ absence de brevet. |
| Partenariats | https://luminovo.com/customers | Aucun partenariat Aurightec attesté ; même règle pour Calcuquote. Aucun fournisseur recommandé. |

**Routage éditorial suggéré :** page 1 identité, périmètre, économie et contexte marché ; page 2 chaîne sourcing–NPI–production/test–service ; page 3 diagnostic et options sous baselines/hard gates. Cette carte n'est pas une preuve, une shortlist ni un contenu gelé.
