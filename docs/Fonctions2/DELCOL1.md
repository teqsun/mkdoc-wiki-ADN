# DELCOL

## Fonction DELCOL

La fonction **DELCOL** supprime la dimension colonnes d'une variable (si elle existe) à l'aide d'un [opérateur de réduction](<Reductions1.md>).&nbsp;

&nbsp;

Une batterie d'items est ainsi synthétisée en une variable simple par combinaison logique de ses modalités.

&nbsp;

Il est possible de spécifier un opérateur de réduction particulier en argument (son nom entre double-quotes).

Consultez la [table des opérateurs de réduction](<Reductions1.md>) pour avoir la liste des différentes possibilités.

#### Syntaxe :&nbsp;

Q01.DELCOL(Reducer)

ou

\_DELCOL(Q01; Reducer)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Reducer | Chaîne de caractères | Opérateur&nbsp; de réduction, par défaut OU pour les variables logiques, SUM pour les variables numériques | NUL par défaut |


#### Exemples :

S1.DELCOL()

Supprime les colonnes d'une variable à l'aide de l'opérateur standard (OU pour les logiques et SUM pour les numériques).

&nbsp;

S1.DELCOL("MEAN")

Supprime les colonnes d'une variable continue à l'aide de l'opérateur de calcul des moyennes.

&nbsp;

Voir aussi : [Gestion des dimensions](<Gererlesdimensionsdesvariables1.md>)

&nbsp;

&nbsp;
