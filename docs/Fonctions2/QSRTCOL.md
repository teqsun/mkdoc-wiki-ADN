# QSRTCOL

## Fonction QSRTCOL

La fonction **QSRTCOL** modifie la consigne de hiérarchie automatique des colonnes de la variable dans les tableaux (dans les propriétés de la variable générée).

Il s'agit donc d'une consigne de mise en forme des tableaux.

&nbsp;

#### Syntaxe :&nbsp;

Q01.QSRTCOL(Ascendant; Anchor; Calculation; Criteria)

ou

\_QSRTCOL(Q01; Ascendant; Anchor; Calculation; Criteria)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Ascendant | Booléen | Sens du tri : ascendant si TRUE, descendant si FALSE et NONE pour annuler le tri | FALSE par défaut |
| &#50; | Anchor | Numérique ou expression | Numéro ou libellé de la modalité de reférence&nbsp; | &nbsp; |
| &#51; | Calculation | Chaîne de caractères | Optionnel : Calcul à utiliser pour le tri dans le tableau | NUL par défaut |
| &#52; | Criteria | Chaîne de caractères | Optionnel : Libellé de la colonne de référence à utiliser lors du tri | NUL par défaut |


#### Remarques :

D'une façon générale, lorsqu'une variable est automatiquement hiérarchisée dans un tableau, il est possible de spécifier une modalité de référence dans un critère de tri en débutant le texte de la modalités par une accolade fermante '}'.

Dans la cas d'une variable logique, le paramètre "Anchor" permet de choisir la modalité de référence pour appliquer le tri des items colonnes.

#### Exemples :

Q02C.QSRTCOL(False;1;PV;2)&nbsp;

Les items sont triés sur la base des pourcentages verticaux de la colonne n° 2 du tableau et sur la modalité 1 de la variable Q02C.

#### Attention :

La fonction QSRTCOL() ne change pas l'ordre des colonnes de la variable mais provoque le tri de celles-ci dans un tableau.

&nbsp;

Voir aussi : [Propriétés des variables](<Modifierlesproprietesdesvariable.md>)

PINCOL() pour fixer une colonnes.
