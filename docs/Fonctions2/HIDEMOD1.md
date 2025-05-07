# HIDEMOD

## Fonction HIDEMOD

La consigne **HIDEMOD** permet de cacher des modalités d'une variable sans en modifier la base.

Les arguments correspondent aux listes de modalités à cacher. Chaque liste suit la syntaxe relative aux sélections d'items.

#### Syntaxe :&nbsp;

Q01.HIDEMOD(sélection)

ou

\_HIDEMOD(Q01; sélection)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | sélection | Liste de valeurs | Liste des&nbsp; éléments à traiter | Obligatoire |


#### Remarques :

Contrairement à REMMOD, la fonction HIDEMOD ne modifie pas la base de la variable utilisée.

#### Exemples :

S1.HIDEMOD(1 -1)

Crée une nouvelle variable dans laquelle la première et la dernière modalités sont cachées dans les tris. En termes de manipulations, ces modalités sont toujours présentes (par exemple pour un tri, une sélection ultérieure, etc.).

&nbsp;

Voir aussi :&nbsp;

[Traiter les variables logiques (modalités)](<Traiterlesvariableslogiquesmoda1.md>)

[Présenter les variables dans les tableaux](<Presenterlesvariablesdanslestab1.md>)