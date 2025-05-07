# NONE

## Fonction NONE ou \<\>

La fonction **NONE** permet de sélectionner les individus n'ayant cité aucune des modalités listées parmi les répondants de la variable sélectionnée.&nbsp;

L'argument correspond aux différents modalités sélectionnées. La variable résultat est un filtre, une variable logique à une seule modalité, sélectionnant les individus n'ayant répondu à aucune des modalités sélectionnées. Pour créer une sélection, il suffit d'employer la syntaxe relative aux sélections d'items et/ou à la sélection étendue de modalités/détails.

#### Syntaxe :&nbsp;

Q01.NONE(Keys)

ou

\_NONE(Q01; Keys)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Keys | Liste de valeurs | Liste des&nbsp; éléments à traiter | Obligatoire |


#### Remarque :

La base "Répondants" de la variable créée est la base "Répondants" de la variable utilisée.

#### Exemples :

S1.NONE(1 2 3)ou

S1 \<\> 1 2 3

Crée une nouvelle variable filtre sélectionnant les individus n'ayant répondu à aucune des modalités 1, 2 ou 3.

&nbsp;

S1.GRPMOD(NONE(1 2 3).FLT(S1) est une définition équivalente.

&nbsp;

Voir aussi :&nbsp;

[ALL](<ALL1.md>)

[EXACTLY](<EXACTLY1.md>)

[ANY](<ANY1.md>)
