# MEAN

## Fonction MEAN

La fonction **MEAN** s'applique à une liste de variables/constructions numériques et retourne une variable dont les valeurs sont les moyennes des valeurs rencontrées dans les arguments.

&nbsp;

La base du résultat est celle des répondants aux 2 variables.

Pour que les sans-réponses soient "neutralisés", et que la base englobe les répondants à au moins une des variables, utilisez MEANNA.

#### Syntaxe :&nbsp;

\_MEAN(Selection)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Selection | Sélection de variables | Expression de sélection de variables (ex: '$"S?"') ou liste de variables séparées par un ";" | Obligatoire |


#### Exemples :

\_MEAN(Q04A; Q04B)

Retourne une variable qui représente la moyenne arithmétique de Q04A et Q04B, pour ceux qui ont répondu aux deux questions.

&nbsp;

Voir aussi :&nbsp;

[Manipuler les variables numériques](<Manipulerlesvariablesnumeriques1.md>)

&nbsp;
