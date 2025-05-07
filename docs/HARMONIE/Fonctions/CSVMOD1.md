# CSVMOD

## Fonction CSVMOD

La fonction **CSVMOD** regroupe les modalités d'une variable à l'aide de regroupements textuels décrits dans une table externe.

&nbsp;

Le nom de la table est indiquée par une chaîne de caractère, selon le principe de repérage des tables externes.

&nbsp;

La 1ère colonne indique les modalités (et les textes associés) à retenir pour constituer la variable résultat.

Les colonnes qui suivent indiquent les autres modalités à regrouper. Les textes saisis peuvent utiliser les 'jokers' (\* et ?) pour exprimer des sélections plus larges.

&nbsp;

La variable résultante est une variable logique qui possède une modalité par ligne de la table.

#### Syntaxe :&nbsp;

Q01.CSVMOD(TableExpression)

ou

\_CSVMOD(Q01; TableExpression)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | TableExpression | Chaîne de caractères | Chaîne de caractères décrivant le nom et l'onglet du classeur Excel contenant la table externe à utiliser | Obligatoire |
| &nbsp; | NotListed | Booléen | Ajoute les réponses non listées dans la table si TRUE | FALSE par défaut |


#### Remarques :

Les fonctions CSVCOL et CSVROW fonctionnent exactement sur le même mode, mais la première s'applique à la dimension "colonnes" et la seconde à la dimension "lignes" de la variable source.

#### Exemples :

Q01A.CSVMOD("COUNTRIES";TRUE)

Retourne une variable logique dont les modalités correspondent aux regroupements textuels listés dans la table en argument plus les réponses non listées dans la table.

&nbsp;

Voir aussi : [Utilisation de tables externes](<Utilisationdetablesexternes1.md>)