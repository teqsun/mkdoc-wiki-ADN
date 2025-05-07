# DIV

## Fonction DIV

La fonction **DIV** s'applique à une liste de variables/constructions numériques et retourne une variable dont les valeurs sont le résultat de la division des arguments.

La base du résultat correspond aux répondants aux 2 variables.

#### Syntaxe :&nbsp;

Q01.DIV(Variables)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Selection | Sélection de variables | Expression de sélection de variables (ex: '$"S?"') ou liste de variables séparées par un ";" | Obligatoire |


#### Remarques :

Pour que les sans-réponses soient ramenés à la valeur neutre, et que la base englobe les répondants à au moins une des variables, utilisez DIVNA.

#### Exemples :

\_DIV(Q04A; Q04B)

Retourne une variable qui représente la division numérique de Q04A par Q04B, pour ceux qui ont répondu aux deux questions.

&nbsp;

Voir aussi :&nbsp;

[Manipuler les variables numériques](<Manipulerlesvariablesnumeriques1.md>)

[Combiner les variables](<Combinerlesvariables1.md>)