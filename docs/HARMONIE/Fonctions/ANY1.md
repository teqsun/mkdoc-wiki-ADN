# ANY

## Fonction ANY

La fonction **ANY** permet de sélectionner les individus ayant cité au moins une des modalités ou codes listés.

L'argument correspond aux différents modalités sélectionnées. La variable résultat est un filtre, une variable logique à une seule modalité, sélectionnant les individus ayant répondus au moins une des modalités sélectionnées. Pour créer une sélection, il suffit d'employer la syntaxe relative aux sélections d'items et/ou à la sélection étendue de modalités/détails.

#### Syntaxe :&nbsp;

Q01.ANY(Keys)

ou

\_ANY(Q01; Keys)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Keys | Liste de valeurs | Liste des éléments à traiter | Obligatoire |


#### Exemples :

S1.ANY(1 2 3)

Crée une nouvelle variable filtre sélectionnant les individus ayant au moins une des modalités 1, 2 ou 3.

&nbsp;

S1.GRPMOD(ANY(1 2 3)) ou S1.GRPMOD(1 2 3)sont des définitions équivalentes.

&nbsp;

#### Remarques :

Avec S2 étant une variable continue, les définitions suivantes retournent la même population :

S2.ANY($45)

S2.ANY(45)

S2 = 45

S2 == 45

&nbsp;

Voir aussi :&nbsp;

[ALL](<ALL1.md>)

[EXACTLY](<EXACTLY1.md>)

[NONE](<NONE1.md>)
