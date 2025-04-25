# CRANGE

## Fonction CRANGE

La fonction CRANGE transforme une variable numérique en variable logique (Discrète) en tranches de même taille.&nbsp;

#### Syntaxe :

Q01.CRANGE(Mini; Maxi; Factor)

ou

\_CRANGE(Q01; Mini; Maxi; Factor)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Mini | Entier | Borne minimum | Obligatoire |
| &#50; | Maxi | Entier | Borne maximum | Obligatoire |
| &#51; | Factor | Entier | Taille des classes | Obligatoire |


#### Exemples :

S2.CRANGE(0;100;10)

Crée une variable logique constituée de 10 modalités ayant chacun une taille de 10.

&nbsp;

S2.CRANGE(0;100;5)

Crée une variable logique constituée de 20 modalités ayant chacun une taille de 5.

&nbsp;

&nbsp;

Voir aussi : [Manipuler les variables numériques](<Manipulerlesvariablesnumeriques1.md>)
