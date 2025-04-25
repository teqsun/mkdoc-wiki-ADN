# HIDECOL

## Fonction HIDECOL

La consigne **HIDECOL** permet de cacher des colonnes d'une variable sans en modifier la base.

Les arguments correspondent aux listes de éléments à cacher. Chaque liste suit la syntaxe relative aux sélections d'items.

#### Syntaxe :&nbsp;

Q01.HIDECOL(sélection)

ou

\_HIDECOL(Q01; sélection)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | sélection | Liste de valeurs | Liste des&nbsp; éléments à traiter | Obligatoire |


#### Remarques :

Contrairement à REMCOL, la fonction HIDECOL ne modifie pas la base de la variable utilisée.

#### Exemples :

Q01.HIDECOL(1)

Retourne une variable dont la 1e colonne est cachée dans les tableaux

&nbsp;

Voir aussi :&nbsp;

[Gestion des dimensions](<Gererlesdimensionsdesvariables1.md>)

[Présenter les variables dans les tableaux](<Presenterlesvariablesdanslestab1.md>)
