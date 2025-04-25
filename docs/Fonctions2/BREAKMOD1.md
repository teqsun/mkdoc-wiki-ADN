# BREAKMOD

## Fonction BREAKMOD

La fonction **BREAKMOD** définit des saut de pages ou des espacements sur les modalités de la variable traitée.

#### Syntaxe :&nbsp;

Q01.BREAKMOD(Selection; Value; BreakBefore; SpaceBreak)

ou

\_BREAKMOD(Q01; Selection; Value; BreakBefore; SpaceBreak)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Selection | Liste de valeurs | Positions des éléments à modifier | Obligatoire |
| &#50; | Value | Booléen | Par défaut, ajoute le saut de page. | TRUE par défaut |
| &#51; | BreakBefore | Booléen | Par défaut, le saut est avant la sélection | TRUE par défaut |
| &#52; | SpaceBreak | Booléen | TRUE : remplace de saut de page par un espacement | FALSE par défaut |


#### Exemples :

S1.BREAKMOD(3; TRUE; TRUE; TRUE)

Crée un espacement devant la 3ème modalité, visible dans les tableaux.

&nbsp;

Voir aussi :&nbsp;

[Présenter les variables dans les tableaux](<Presenterlesvariablesdanslestab1.md>)
