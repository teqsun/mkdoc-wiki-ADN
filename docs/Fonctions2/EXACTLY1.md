# EXACTLY

## Fonction EXACTLY

La fonction **EXACTLY** permet de sélectionner les individus ayant cité exactement toutes les modalités listées et rien d'autre.&nbsp;

L'argument correspond aux différents modalités sélectionnées. La variable résultat est un filtre, une variable logique à une seule modalité, sélectionnant les individus ayant répondus exactement toutes les modalités sélectionnées et rien d'autres. Pour créer une sélection, il suffit d'employer la syntaxe relative aux sélections d'items et/ou à la sélection étendue de modalités/détails.

#### Syntaxe :&nbsp;

Q01.EXACTLY(Keys)

ou

\_EXACTLY(Q01; Keys)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Keys | Liste de valeurs | Liste des&nbsp; éléments à traiter | Obligatoire |


#### Exemples :

S1.EXACTLY(1 2 3)

Crée une nouvelle variable filtre sélectionnant les individus ayant cités exactement les modalités 1 et 2 et 3.

&nbsp;

S1.GRPMOD(EXACTLY(1 2 3) est une définition équivalente.

&nbsp;

Voir aussi :&nbsp;

[ALL](<ALL1.md>)

[ANY](<ANY1.md>)

[NONE](<NONE1.md>)
