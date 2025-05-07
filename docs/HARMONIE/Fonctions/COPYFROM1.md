# COPYFROM

## Fonction COPYFROM

La fonction **COPYFROM** copie les propriétés d'une variable "donneuse" dans la variable traitée.

&nbsp;

Les propriétés à copier sont définies à l'aide du 1er argument :

* TITLE&nbsp; : le titre
* SHORT\_TITLE : le titre court
* COMMENT : les commentaire
* UNIVERSE : l'univers associé à la variable
* WEIGHT : le poids associé à la variable
* LABELS : les modalités
* COLUMNS : les colonnes&nbsp;
* ROWS : les lignes

#### Syntaxe :&nbsp;

Q01.COPYFROM(Argument; PropertyMask)

ou

\_COPYFROM(Q01; Argument; PropertyMask)

#### Exemples :

Q2R.COPYFROM(Q2;SHORT\_TITLE)

Le titre court de la variable Q2R se voit attribuer le même texte que le titre court de la variable Q2.

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Argument | Variable | Variable source | Obligatoire |
| &#50; | PropertyMask | Chaîne de caractères | Eléments à copier séparés par un espace | UNIVERSE WEIGHT LABELS COLUMNS ROWS&nbsp; TITLE SHORT\_TITLE&nbsp; COMMENT |


&nbsp;

Voir aussi :&nbsp;

[Gestion des libellés](<Gererleslibelleslestextes1.md>)

[Propriétés des variables](<Modifierlesproprietesdesvariable.md>)

[Combiner les variables](<Combinerlesvariables1.md>)