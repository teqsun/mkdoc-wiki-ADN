# CALCVARIANCE

## Fonction CALCVARIANCE

La fonction **CALCVARIANCE** crée une variable numérique constante correspondant à la variance de la variable numérique indiquée en paramètre, le second paramètre permet de choisir entre la variance standard (False) ou la variance estimée (True). Le paramètre par défaut étant False.

#### Syntaxe :&nbsp;

Q01.CALCVARIANCE(UseEstimatedCalculation; Weight)

ou

\_CALCVARIANCE(Q01; UseEstimatedCalculation; Weight)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | UseEstimatedCalculation | Booléen | Par défaut calcule la variance (divisée par N) | FALSE par défaut |
| &#50; | Weight | Variable | Pondération à appliquer | vide par défaut |


#### Exemples :

\_CALCVARIANCE(NOTE)

Crée une nouvelle variable correspondant à la variance standard de la variable numérique NOTE.

&nbsp;

Voir aussi : [Manipuler les variables numériques](<Manipulerlesvariablesnumeriques1.md>)
