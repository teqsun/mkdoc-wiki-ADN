# AUTOBASE

## Fonction AUTOBASE

La fonction **AUTOBASE** calcule les bases manquantes par analyse de l'ordonnateur.

&nbsp;

Chaque "groupe de modalités" (modalités qui partagent la même valeur d'ordonnateur) peut posséder une base, définie par un ordonnateur négatif et dont la valeur absolue correspond au numéro du groupe.

La présence de cette base détermine le comportement du calcul du complément lors des tests statistiques.

Par défaut, le complément est calculé par soustraction de la modalité de la base répondant de la variable.

Si la modalité appartient à un groupe qui dispose d'une base explicite, alors le calcul de complément utilise cette base.

#### Syntaxe :&nbsp;

Q01.AUTOBASE(ShowBases; MoveAtEnd)

ou

\_AUTOBASE(Q01; ShowBases; MoveAtEnd)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | ShowBases | Booléen | Par défaut, n'affiche pas les bases calculées, si TRUE affiche les bases | FALSE par défaut |
| &#50; | MoveAtEnd | Booléen | Par défaut, les bases sont en premières positions, si TRUE les bases sont en dernières modalités | FALSE par défaut |


#### Remarques :

Il n'est pas rare de trouver la fonction AUTOBASE dans la création de critères et en complément de la fonction ORDMOD.

Entre en interaction avec les options des test statistiques

#### Exemples :

S1.AUTOBASE()

S1.AUTOBASE(TRUE; TRUE)

&nbsp;

Voir aussi : [Critères](<Creerdescriteresoubannieres1.md>)
