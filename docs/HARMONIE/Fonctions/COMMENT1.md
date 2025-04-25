# COMMENT

## Fonction COMMENT

La fonction **COMMENT** modifie le commentaire de la variable passée en argument.

#### Syntaxe :&nbsp;

Q01.COMMENT(Expression)

ou

\_COMMENT(Q01; Expression)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Expression | Chaîne de caractères | Texte du commentaire ou fonction de traitement appliquée au commentaire | Obligatoire |


#### Remarques :

Il est possible de préfixer la valeur par le signe "=" pour utiliser une fonction de traitement appliquée au commentaire de la variable en entrée.

Pour plus d'informations, aller voir la section sur les Traitements textuels

#### Exemples :

S2.COMMENT("Age")

S2.COMMENT("=TRIM, UPPER")

S2.COMMENT("=UPPER(@VALUE)")

&nbsp;

S1.COMMENT("A tous").SHORTITLE("\[NAME\]. \[TITLE\] (COMMENT\])")

Ainsi le titre court de S1 devient "S1. Le titre (A tous)"

Avec NAME = "S1" et&nbsp; TITLE = "Le titre".

&nbsp;

La fonction COMMENT conserve toutes les autres propriétés de la variable d'origine

&nbsp;

Voir aussi : [Propriétés des variables](<Modifierlesproprietesdesvariable.md>)
