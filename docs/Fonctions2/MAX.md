# MAX

## Fonction MAX

La fonction **MAX** s'applique à une liste de variables/constructions numériques et retourne une variable dont les valeurs sont le maximum des valeurs rencontrées dans les arguments .

&nbsp;

La base du résultat est celle des répondants aux 2 variables.

Pour que les sans-réponses soient "neutralisés", et que la base englobe les répondants à au moins une des variables, utilisez MAXNA.

#### Syntaxe :&nbsp;

\_MAX(Selection)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Selection | Sélection de variables | Expression de sélection de variables (ex: '$"S?"') ou liste de variables séparées par un ";" | Obligatoire |


#### Exemples :

\_MAX(Q04A; Q04B)

Retourne une variable qui plafonne Q04A et Q04B, pour ceux qui ont répondu aux deux questions.

&nbsp;

\_MAXNA(Q04A; Q04B)

Retourne une variable qui plafonne Q04A et Q04B, pour ceux qui ont répondu à au moins une des deux questions.

&nbsp;

Voir aussi : [Manipuler les variables numériques](<Manipulerlesvariablesnumeriques1.md>)