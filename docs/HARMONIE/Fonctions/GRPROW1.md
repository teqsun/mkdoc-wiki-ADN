# GRPROW

## Fonction GRPROW

La fonction **GRPROW** permet de regrouper les colonnes d'une variable.&nbsp;

Les arguments correspondent aux différents groupements souhaités. La variable résultat comporte autant de lignes qu'il y a groupements. Pour créer un groupe, il suffit d'employer la syntaxe relative aux sélections d'items et/ou à la sélection étendue de modalités/détails.

#### Syntaxe :&nbsp;

Q01.GRPROW(Keys)

ou

\_GRPROW(Q01; Keys)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Keys | Liste de valeurs | Liste des&nbsp; éléments à traiter | Obligatoire |


#### Remarques :

L'opérateur de regroupement est :&nbsp;

* OU pour les variables logiques,
* SUM pour les variables numériques.

#### Exemples :

S1.GRPROW(1 2; 1; 2; -1)

Crée une nouvelle variable dont les lignes sont :

\- le groupement des lignes 1 et 2 de S1

\- la première ligne de S1

\- la deuxième ligne de S1&nbsp;

\- la dernière de S1.

&nbsp;

S1.GRPMOD(1 2; 1; 2; $O)

Crée une nouvelle variable dont les lignes sont :

\- le groupement des lignes 1 et 2 de S1

\- la première ligne de S1

\- la deuxième ligne de S1&nbsp;

\- les modalités non citées

&nbsp;

Voir aussi : [Gestion des dimensions](<Gererlesdimensionsdesvariables1.md>)