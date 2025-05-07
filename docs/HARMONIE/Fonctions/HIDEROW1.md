# HIDEROW

## Fonction HIDEROW

La consigne **HIDEROW** permet de cacher des lignes d'une variable sans en modifier la base.

Les arguments correspondent aux listes de éléments à cacher. Chaque liste suit la syntaxe relative aux sélections d'items.

#### Syntaxe :&nbsp;

Q01.HIDEROW(sélection)

ou

\_HIDEROW(Q01; sélection)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | sélection | Liste de valeurs | Liste des&nbsp; éléments à traiter | Obligatoire |


#### Remarques :

Contrairement à REMROW, la fonction HIDEROW ne modifie pas la base de la variable utilisée.

#### Exemples :

\_HIDEROW(Q01; 1)

&nbsp;

Voir aussi :&nbsp;

[Gestion des dimensions](<Gererlesdimensionsdesvariables1.md>)

[Présenter les variables dans les tableaux](<Presenterlesvariablesdanslestab1.md>)