# SUB

## Fonction SUB

La fonction **SUB** s'applique à une liste de variables/constructions numériques et retourne une variable dont les valeurs sont la différence des valeurs rencontrées dans les arguments.

&nbsp;

La base du résultat est celle des répondants aux 2 variables.

Pour que les sans-réponses soient "neutralisés", et que la base englobe les répondants à au moins une des variables, utilisez SUBNA.

#### Syntaxe :&nbsp;

\_SUB(Selection)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Selection | Sélection de variables | Expression de sélection de variables (ex: '$"S?"') ou liste de variables séparées par un ";" | Obligatoire |


#### Exemples :

\_SUB(Q04A; Q04B)

Retourne une variable qui représente la différence de Q04A et Q04B, pour ceux qui ont répondu aux deux questions.

&nbsp;

Voir aussi :&nbsp;

[Manipuler les variables numériques](<Manipulerlesvariablesnumeriques1.md>)

[Combiner les variables](<Combinerlesvariables1.md>)
