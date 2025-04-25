# DYNCOL

## Fonction DYNCOL

Sur la base d'une table de référence qui liste un ensemble d'éléments codifiés, crée des regroupements dynamiques avec hiérarchie, le tout piloté dans des tables externes.

#### Syntaxe :&nbsp;

Q01.DYNCOL(Table; Index; MatchMode; Sorters; Groupers; CodeColumn; TextColumn)

ou

\_DYNCOL(Q01; Table; Index; MatchMode; Sorters; Groupers; CodeColumn; TextColumn)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Table | Chaîne de caractères | Table descriptive des codes | Obligatoire |
| &#50; | Index | Chaîne de caractères | table des modalités à construire | Obligatoire |
| &#51; | MatchMode | Chaîne de caractères | Repérage par code ou position ou texte. Code par défaut | "CODE"/POSITION/TEXT par défaut |
| &#52; | Sorters | Chaîne de caractères | Liste des noms de colonnes de tables utilisées pour trier | "" par défaut |
| &#53; | Groupers | Chaîne de caractères | liste des noms de colonnes de tables utilisées pour regrouper | "" par défaut |
| &#54; | CodeColumn | Chaîne de caractères | nom de la colonne indiquant les codes de ref | Obligatoire |
| &#55; | TextColumn | Chaîne de caractères | nom de la colonne indiquant les textes de ref | "" par défaut |


#### Exemples :

&nbsp;

Voir aussi : [Utilisation de tables externes](<Utilisationdetablesexternes1.md>)
