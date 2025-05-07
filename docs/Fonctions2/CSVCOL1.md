# CSVCOL

## Fonction CSVCOL

La fonction **CSVCOL** regroupe les colonnes d'une variable à l'aide de regroupements textuels décrits dans une table externe.

Le nom de la table est indiquée par une chaîne de caractère, selon le principe de repérage des tables externes.

&nbsp;

La 1ère colonne indique les items à retenir (et les textes associés) pour constituer la variable résultat.

Les colonnes qui suivent indiquent les items à regrouper. Les textes saisis peuvent utiliser les 'jokers' (\* et ?) pour exprimer des sélections plus larges.

La variable résultante est une variable dimensionnée qui possède une colonne par ligne de la table.

#### Syntaxe :&nbsp;

Q01.CSVCOL(TableExpression)

ou

\_CSVCOL(Q01; TableExpression)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | TableExpression | Chaîne de caractères | Chaîne de caractères décrivant le nom et l'onglet du classeur Excel contenant la table externe à utiliser | Obligatoire |


#### Exemples :

Q01A.CSVCOL("COUNTRIES")

Retourne une variable dont les colonnes correspondent aux regroupements textuels listés dans la table en argument.

&nbsp;

Voir aussi : [Utilisation de tables externes](<Utilisationdetablesexternes1.md>)