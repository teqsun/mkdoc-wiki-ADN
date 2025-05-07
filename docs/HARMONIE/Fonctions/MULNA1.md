# MULNA

## Fonction MULNA

La fonction **MULNA** calcule la multiplication de plusieurs variables numériques (NA \* 1 = 1).

Pour exclure les sans-répons, voir la fonction MUL

#### Syntaxe :&nbsp;

\_MULNA(Selection)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Selection | Sélection de variables | Expression de sélection de variables (ex: '$"S?"') ou liste de variables séparées par un ";" | Obligatoire |


#### Exemples :

\_MULNA(Q04A; Q04B)

Retourne une variable qui est le produit de Q04A et Q04B, pour ceux qui ont répondu à au moins une des deux questions.

&nbsp;

Voir aussi :&nbsp;

[Manipuler les variables numériques](<Manipulerlesvariablesnumeriques1.md>)

[Combiner les variables](<Combinerlesvariables1.md>)
