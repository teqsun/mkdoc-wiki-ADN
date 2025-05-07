# CALCSTDEV

## Fonction CALCSTDEV

La fonction **CALCSTDEV** crée une variable numérique constante correspondant à l'écart-type de la variable numérique indiquée en paramètre, le second paramètre permet de choisir entre l'écart-type standard (False) ou l'écart-type estimée (True). Le paramètre par défaut étant False.

&nbsp;

\_CALCSTDEV(varq;False)

#### Syntaxe :&nbsp;

Q01.CALCSTDEV(UseEstimatedCalculation; Weight)

ou

\_CALCSTDEV(Q01; UseEstimatedCalculation; Weight)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | UseEstimatedCalculation | Booléen | Par défaut calcule l'écart-type (divisé par N) | FALSE par défaut |
| &#50; | Weight | Variable | Pondération à appliquer | vide par défaut |


#### Exemples :

\_CALCSTDEV(NOTE)

Crée une nouvelle variable correspondant à l'écart-type standard de la variable numérique NOTE.

&nbsp;

Voir aussi : [Manipuler les variables numériques](<Manipulerlesvariablesnumeriques1.md>)