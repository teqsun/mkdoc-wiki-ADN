# ANSWERS

## Fonction ANSWERS

La fonction ANSWERS appliquée à une variable multi-réponses retourne une variable numérique qui contient le nombre de réponses citées pour chacun des individus de la variable d'origine.

#### Syntaxe :&nbsp;

Q01.ANSWERS(UseReductor)

ou

\_ANSWERS(Q01; UseReductor)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | UseReductor | Booléen | Prend en compte le réducteur si TRUE (plafonné à 1) | FALSE par défaut |


#### Remarques :

Il est fréquent d'utiliser la fonction [DTOC](<DTOC1.md>) à la place de ANSWERS.&nbsp;

Dans ce cas le réducteur est toujours pris en compte, et ses valeurs ne sont pas plafonnées à 1.

#### Exemples :

S6.ANSWERS(TRUE)

Retourne une variable numérique qui contient le nombre de réponses citées, pour par exemple calculer un nombre moyen de réponses.

&nbsp;

Voir aussi : [Traiter les variables multi-réponses](<Traiterlesvariablesmulti-repons1.md>)
