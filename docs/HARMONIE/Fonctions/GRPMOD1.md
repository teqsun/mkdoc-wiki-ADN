# GRPMOD

## Fonction GRPMOD

La fonction **GRPMOD** permet de regrouper les modalités d'une variable.&nbsp;

Les arguments correspondent aux différents groupements souhaités. La variable résultat comporte autant de modalités qu'il y a de groupements. Pour créer un groupe, il suffit d'employer la syntaxe relative aux sélections d'items et/ou à la sélection étendue de modalités/détails.

#### Syntaxe :&nbsp;

Q01.GRPMOD(Keys)

ou

\_GRPMOD(Q01; Keys)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Keys | Liste de valeurs | Liste des&nbsp; éléments à traiter | Obligatoire |


#### Remarques :

GRPMOD et SELMOD sont très proches \! En réalité, la seule différence vient du comportement par défaut lorsqu'un argument correspond à une liste d'items : GRPMOD crée un sous-total et SELMOD en liste le détail.

Les fonctions GRPCOL et GRPROW fonctionnent exactement sur le même mode, mais la première s'applique à la dimension "colonnes" et la seconde à la dimension "lignes" de la variable source.

Dans le cas d'une variable logique, 0 crée une modalité vide alors que dans le cas d'une variable continue, 0 sélectionne bien le code 0.

#### Exemples :

S1.GRPMOD(1 2; 1; 2; -1)

Crée une nouvelle variable dont les modalités sont :

\- le groupement des modalités 1 et 2 de S1

\- la première modalité de S1

\- la deuxième modalité de S1&nbsp;

\- la dernière de S1.

&nbsp;

S1.GRPMOD(1 2; 1; 2; $O)

Crée une nouvelle variable dont les modalités sont :

\- le groupement des modalités 1 et 2 de S1

\- la première modalité de S1

\- la deuxième modalité de S1&nbsp;

\- les modalités non citées

&nbsp;

## S1.GRPMOD(1; ~1)

Crée une nouvelle variable dont les modalités sont :

\- la sélection de la modalité 1 de S1

\- la sélection du complément de la modalité 1 de S1, sur la base des répondants à S1

&nbsp;

Voir aussi :&nbsp;

[Traiter les variables logiques (modalités)](<Traiterlesvariableslogiquesmoda1.md>)

[Gestion des dimensions](<Gererlesdimensionsdesvariables1.md>)

&nbsp;
