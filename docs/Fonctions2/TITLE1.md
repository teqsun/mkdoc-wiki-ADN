# TITLE

## Fonction TITLE

La fonction **TITLE** modifie le titre de la variable passée en argument.

&nbsp;

Il est possible de préfixer la valeur par le signe "=" pour utiliser une fonction de traitement appliquée au titre de la variable en entrée.

Pour plus d'informations, aller voir la section sur les "Traitements textuels"

#### Syntaxe :&nbsp;

Q01.TITLE(Expression)

ou

\_TITLE(Q01; Expression)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Expression | Chaîne de caractères | Chaîne de caractères | Obligatoire |


#### Remarques :

La fonction TITLE conserve toutes les autres propriétés de la variable d'origine

#### Exemples :

S2.TITLE("Age")

S2.TITLE("=TRIM, UPPER")

S2.TITLE("=UPPER(@VALUE)")

&nbsp;

Voir aussi : [Propriétés des variables](<Modifierlesproprietesdesvariable.md>)
