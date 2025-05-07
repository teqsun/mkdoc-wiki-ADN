# ALL

## Fonction ALL

La fonction **ALL** permet de sélectionner les individus ayant cité toutes les modalités listées.&nbsp;

L'argument correspond aux différentes modalités sélectionnées. La variable résultat est un filtre, une variable logique à une seule modalité, sélectionnant les individus ayant répondu à toutes les modalités sélectionnées. Pour créer une sélection, il suffit d'employer la syntaxe relative à la méthode de sélection des items et/ou à la méthode de sélection étendue de modalités/détails.

#### Syntaxe :&nbsp;

Q01.ALL(Keys)

ou

\_ALL(Q01; Keys)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Keys | Liste de valeurs | Liste des éléments à traiter | Obligatoire |


#### Exemples :

S1.ALL(1 2 3)

Crée une nouvelle variable filtre sélectionnant les individus ayant cités au moins les modalités 1 et 2 et 3.

&nbsp;

S1.GRPMOD(ALL(1 2 3))est une définition équivalente.

&nbsp;

Voir aussi :&nbsp;

[EXACTLY](<EXACTLY1.md>)

[ANY](<ANY1.md>)

[NONE](<NONE1.md>)
