# CALCPERCENTILE

## Fonction CALCPERCENTILE

La fonction **CALCPERCENTILE** crée une variable numérique constante correspondant au percentile (ou centile) de la variable numérique indiquée en paramètre, le second paramètre permet de choisir le percentile, 1 par défaut.

#### Syntaxe :&nbsp;

Q01.CALCPERCENTILE(Percentile; Weight)

ou

\_CALCPERCENTILE(Q01; Percentile; Weight)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Percentile | Entier | Percentile sélectionné, par défaut 1 | &#49; par défaut |
| &#50; | Weight | Variable | Pondération à appliquer | vide par défaut |


#### Exemples :

\_CALCPERCENTILE(NOTE)

Crée une nouvelle variable correspondant à la valeur du premier percentile de la variable numérique NOTE.

&nbsp;

Voir aussi : [Manipuler les variables numériques](<Manipulerlesvariablesnumeriques1.md>)
