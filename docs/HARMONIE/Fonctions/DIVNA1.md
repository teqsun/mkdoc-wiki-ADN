# DIVNA

## Fonction DIVNA

La fonction **DIVNA** s'applique à une liste de variables/constructions numériques et retourne une variable dont les valeurs sont le résultat de la division des arguments.&nbsp;

La base du résultat correspond aux interrogés aux 2 variables. DIVNA&nbsp; est insensible aux sans-réponses (NA).

#### Syntaxe :&nbsp;

Q01.DIVNA(sélection)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Selection | Sélection de variables | Expression de sélection de variables (ex: '$"S?"') ou liste de variables séparées par un ";" | Obligatoire |


#### Exemples :

\_DIVNA(Q04A; Q04B)

Retourne une variable qui représente la division numérique de Q04A par Q04B.

&nbsp;

Voir aussi :&nbsp;

[Manipuler les variables numériques](<Manipulerlesvariablesnumeriques1.md>)

[Combiner les variables](<Combinerlesvariables1.md>)

[\_DIV](<DIV1.md>)