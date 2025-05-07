# CALCQUARTILE

## Fonction CALCQUARTILE

La fonction **CALCQUARTILE** crée une variable numérique constante correspondant au quartile de la variable numérique indiquée en paramètre, le second paramètre permet de choisir le quartile, 1 par défaut et le troisième paramètre permet de choisir une pondération à appliquer.

#### Syntaxe :&nbsp;

Q01.CALCQUARTILE(Quartile; Weight)

ou

\_CALCQUARTILE(Q01; Quartile; Weight)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Quartile | Entier | Quartile sélectionné, par défaut 1 | &#49; par défaut |
| &#50; | Weight | Variable | Pondération à appliquer | vide par défaut |


#### Exemples :

\_CALCQUARTILE(NOTE;1)

Crée une nouvelle variable correspondant à la valeur du premier quartile de la variable numérique NOTE, sans pondération.

&nbsp;

Voir aussi : [Manipuler les variables numériques](<Manipulerlesvariablesnumeriques1.md>)