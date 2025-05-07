# QSRT

## Fonction QSRT

La fonction **QSRT** modifie la consigne de hiérarchie automatique de la variable dans les tableaux (dans les propriétés de la variable générée).

Il s'agit donc d'une consigne de mise en forme des tableaux.

#### Syntaxe :&nbsp;

Q01.QSRT(Ascendant; Calculation; Criteria)

ou

\_QSRT(Q01; Ascendant; Calculation; Criteria)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Ascendant | Booléen | Sens du tri : ascendant si TRUE, descendant si FALSE et NONE pour annuler le tri | FALSE par défaut |
| &#50; | Calculation | Chaîne de caractères | Optionnel : Calcul à utiliser pour le tri dans le tableau | NUL par défaut |
| &#51; | Criteria | Chaîne de caractères | Optionnel : Libellé de la colonne de référence à utiliser lors du tri | NUL par défaut |


#### Remarques :

D'une façon générale, lorsqu'une variable est automatiquement hiérarchisée dans un tableau, il est possible de spécifier une modalité de référence dans un critère de tri en débutant le texte de la modalités par une accolade fermante '}'.

#### Exemples :

S6.QSRT(NONE)&nbsp;

Et les modalités de la nouvelle variable ne seront plus triées.

#### Attention :

La fonction QSRT() ne change pas l'ordre des modalités de la variable mais provoque le tri de celles-ci dans un tableau.

&nbsp;

Voir aussi : [Propriétés des variables](<Modifierlesproprietesdesvariable.md>)

PINMOD() pour fixer une modalité.