# JUXROW

## Fonction JUXROW

La fonction **JUXROW** juxtapose les variables en arguments sur la dimension des lignes.&nbsp;

Les variables qui n'ont pas de lignes sont automatiquement adaptées.&nbsp;

&nbsp;

IMPORTANT : Les modalités de la variable résultante obéissent au principe de l'harmonisation des dimensions.

&nbsp;

Il est donc toujours possible de juxtaposer n'importe quelles variables sur les lignes : la fonction se charge de tout harmoniser si besoin.

&nbsp;

La fonction JUXROW est l'équivalent de la fonction JUXCOL sur la dimension des colonnes.

#### Syntaxe :&nbsp;

\_JUXROW(Selection)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Selection | Sélection de variables | Expression de sélection de variables (ex: '$"S?"') ou liste de variables séparées par un ";" | Obligatoire |


#### Exemples :

\_JUXROW(Q1:Q2:Q3)

\_JUXROW("Q\*")

#### Remarque :

Une variable ayant une dimension ligne a obligatoirement une dimension colonne.

Autrement dit, seule une variable doublement dimensionnée a des lignes et des colonnes. Une variable simplement dimensionnée n'a jamais de lignes.&nbsp;

Dans le cas de juxtaposition de plusieurs varaibles simples, les items colonnes récupèrent un libellé constitué par la partie variable du titre des variables d'origines. Alors que la partie commune devient le titre de la&nbsp;

nouvelle variable.

Pour juxtaposer des variables sans tenir compte des libellés, il faut utiliser au préalable les fonctions [NOTXT](<NOTXT1.md>), CLRCOL ou CLRROW

Voir aussi :&nbsp;

[Gestion des dimensions](<Gererlesdimensionsdesvariables1.md>)

[Combiner les variables](<Combinerlesvariables1.md>)