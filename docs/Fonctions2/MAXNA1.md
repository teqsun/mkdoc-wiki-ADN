# MAXNA

## Fonction MAXNA

La fonction **MAXNA** calcule la valeur maximum entre plusieurs variables numériques (maximum entre X et NA = X quelque soit X).

#### Syntaxe :&nbsp;

\_MAXNA(Selection)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Selection | Sélection de variables | Expression de sélection de variables (ex: '$"S?"') ou liste de variables séparées par un ";" | Obligatoire |


#### Exemples :

\_MAXNA(Q04A; Q04B)

Retourne une variable qui plafonne Q04A et Q04B, pour ceux qui ont répondu à au moins une des deux questions.

&nbsp;

\_MAX(Q04A; Q04B)

Retourne une variable qui plafonne Q04A et Q04B, pour ceux qui ont répondu aux deux questions.

&nbsp;

&nbsp;

Voir aussi : [Manipuler les variables numériques](<Manipulerlesvariablesnumeriques1.md>)
