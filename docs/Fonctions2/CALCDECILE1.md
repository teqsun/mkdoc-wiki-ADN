# CALCDECILE

## Fonction CALCDECILE

La fonction **CALCDECILE** crée une variable numérique constante correspondant au décile de la variable numérique indiquée en paramètre, le second paramètre permet de choisir le décile, 1 par défaut.

#### Syntaxe :&nbsp;

Q01.CALCDECILE(Decile; Weight)

ou

\_CALCDECILE(Q01; Decile; Weight)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Decile | Entier | numéro du décile sélectionné, par défaut 1 | &#49; par défaut |
| &#50; | Weight | Variable | Pondération à appliquer | vide par défaut |


#### Exemples :

\_CALCDECILE(NOTE)

Crée une nouvelle variable correspondant à la valeur du premier décile de la variable numérique NOTE.

&nbsp;

Voir aussi : [Manipuler les variables numériques](<Manipulerlesvariablesnumeriques1.md>)
