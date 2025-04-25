# RANKCOL

## Fonction RANKCOL

La fonction **RANKCOL** détermine, pour chaque indivdu, le rang de chaque détail (colonne) de ses réponses à une variable cotinue dimensionnée.

#### Syntaxe :&nbsp;

Q01.RANKCOL(Descendant; RankingMode)

ou

\_RANKCOL(Q01; Descendant; RankingMode)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Descendant | Booléen | FALSE (par défaut) pour un tri ascendant, FALSE pour un tri descendant. | Obligatoire |
| &#50; | RankingMode | Chaîne de caractères | Gestion des ex aequo&nbsp; **STANDARD** (défaut) : Les ex eaquo reçoivent le rang minimal possible parmi leurs rangs possibles. Pour \[10, 10, 5, 7, 15, 15\], on obtient \[3, 3, 1, 2, 5, 5\] **DENSE**&nbsp; : Les ex eaquo reçoivent le même rang, mai il y a des "trous" dans la séaquence des rangs. Pour \[10, 10, 5, 7, 15, 15\], on obtient \[3, 3, 1, 2, 4, 4\] **MAXIMAL** : Les ex eaquo reçoivent le rang maximal possible. C'est l'inverse du mode STANDARD. Pour \[10, 10, 5, 7, 15, 15\], on obtient \[4, 4, 1, 2, 6, 6\] | &nbsp; |


#### Exemples :

Q01.RANKCOL()

Retourne une variable continue dimensionnée contenant les rangs des réponses dans l'ordre descendant de Q01 pour chaque individus.

&nbsp;

#### Remarques :

Equivalent à la fonction IDXCOL de DAISIE.
