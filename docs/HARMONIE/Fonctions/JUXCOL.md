# JUXCOL

## Fonction JUXCOL

La fonction **JUXCOL** juxtapose les variables en arguments sur la dimension des colonnes.

Les variables qui n'ont pas de colonnes sont automatiquement adaptées.&nbsp;

&nbsp;

IMPORTANT : Les modalités de la variable résultante obéissent au principe de l'harmonisation des dimensions.

&nbsp;

Il est donc toujours possible de juxtaposer n'importe quelles variables sur les colonnes : la fonction se charge de tout harmoniser si besoin.

&nbsp;

La fonction JUXCOL est l'équivalent de la fonction JUXROW sur la dimension des lignes.

#### Syntaxe :&nbsp;

\_JUXCOL(selection)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Selection | Sélection de variables | Expression de sélection de variables (ex: '$"S?"') ou liste de variables séparées par un ";" | Obligatoire |


#### Exemples :

\_JUXCOL(Q1:Q2:Q3)

\_JUXCOL("Q\*")

#### Remarque :

Dans le cas de juxtaposition de plusieurs variables simples, les items colonnes récupèrent un libellé constitué par la partie variable du titre des variables d'origines. Alors que la partie commune devient le titre de la&nbsp;

nouvelle variable.

Pour juxtaposer des variables sans tenir compte des libellés, il faut utiliser au préalable les fonctions [NOTXT](<NOTXT1.md>), CLRCOL ou CLRROW

&nbsp;

Voir aussi :&nbsp;

[Gestion des dimensions](<Gererlesdimensionsdesvariables1.md>)

[Combiner les variables](<Combinerlesvariables1.md>)