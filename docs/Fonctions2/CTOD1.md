# CTOD

## Fonction CTOD

La fonction CTOD transforme une variable numérique en variable logique (Discrète). Il suffit de lister les bornes inférieures des différentes tranches pour créer une nouvelle variable dont chaque modalité correspond à une tranche.

#### Syntaxe n°1 : Création de classes d'effectif constant

Q01.CTOD(Nb; Factor)

ou

\_CTOD(Q01; Nb; Factor)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Nb | Entier | Nombre de classes à créer | Obligatoire |
| &#50; | Factor | Entier | Si N, les bornes sont des multiples de N | \-1 par défaut |


#### Remarque :

Si la variable de abse est dimensionnée, les bornes des classes sont determinées par le premier item et appliquées à toutes les items.

#### &nbsp;

#### &nbsp;

#### Syntaxe n°2 : Création de classes par indication des bornes inférieures&nbsp;

Q01.CTOD(Boundaries)

ou

\_CTOD(Q01; Boundaries)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Boundaries | Liste de nombres | Liste des bornes inférieures des classes à créer | Obligatoire |


#### Syntaxe n°3 : Création d'une modalité par valeur rencontrée (distribution)

Q01.CTOD()

ou

\_CTOD(Q01)

#### Exemples :

S2.CTOD()

Détermine la distribution des valeurs rencontrées (crée une tranche par valeur rencontrée).

&nbsp;

AGE.CTOD(0 25 50)

Crée les tranches "moins de 25", "de 25 à moins de 50" et "50 et plus".

&nbsp;

AGE.CTOD(4)

Crée les quartiles.

&nbsp;

AGE.CTOD(0 50)

Crée une tranche moins de 50 et une tranche "50 et plus".

&nbsp;

Voir aussi : [Manipuler les variables numériques](<Manipulerlesvariablesnumeriques1.md>)
