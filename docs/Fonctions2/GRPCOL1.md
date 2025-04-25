# GRPCOL

## Fonction GRPCOL

La fonction **GRPCOL** permet de regrouper les colonnes d'une variable.&nbsp;

Les arguments correspondent aux différents groupements souhaités. La variable résultat comporte autant de colonnes qu'il y a groupements. Pour créer un groupe, il suffit d'employer la syntaxe relative aux sélections d'items et/ou à la sélection étendue de modalités/détails.

#### Syntaxe :&nbsp;

Q01.GRPCOL(Keys)

ou

\_GRPCOL(Q01; Keys)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Keys | Liste de valeurs | Liste des&nbsp; éléments à traiter | Obligatoire |


#### Remarques :

L'opérateur de regroupement est :&nbsp;

* OU pour les variables logiques,
* SUM pour les variables numériques.

#### Exemples :

S1.GRPCOL(1 2; 1; 2; -1)

Crée une nouvelle variable dont les colonnes sont :

\- le groupement des colonnes 1 et 2 de S1

\- la première colonne de S1

\- la deuxième colonne de S1&nbsp;

\- la dernière de S1.

&nbsp;

S1.GRPCOL(1 2; 1; 2; $O)

Crée une nouvelle variable dont les colonnes sont :

\- le groupement des colonnes 1 et 2 de S1

\- la première colonne de S1

\- la deuxième colonne de S1&nbsp;

\- les colonnes non citées

&nbsp;

Voir aussi : [Gestion des dimensions](<Gererlesdimensionsdesvariables1.md>)

