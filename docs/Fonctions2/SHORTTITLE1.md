# SHORTTITLE

## Fonction SHORTTITLE

La fonction **SHORTTITLE** modifie le titre court de la variable passée en argument.

&nbsp;

Il est possible de préfixer la valeur par le signe "=" pour utiliser une fonction de traitement appliquée au titre de la variable en entrée.

Pour plus d'informations, voir la section sur les "Traitements textuels"

#### Syntaxe :&nbsp;

Q01.SHORTTITLE(Expression)

ou

\_SHORTTITLE(Q01; Expression)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Expression | Chaîne de caractères | Expression à utiliser pour fixe le nouveau titre court | Obligatoire |


#### Remarques :

La fonction SHORTTITLE conserve toutes les autres propriétés de la variable d'origine. Si le titre court est présent et pour facilité la lecture, il est affiché dans la vue "Variables" à la place du titre long.

#### Exemples :

S2.SHORTTITLE("Age")

S2.SHORTTITLE("=TRIM, UPPER")

S2.SHORTTITLE("=UPPER(@VALUE)")

&nbsp;

Voir aussi : [Propriétés des variables](<Modifierlesproprietesdesvariable.md>)
