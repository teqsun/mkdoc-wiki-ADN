# MILLISECONDS

## Fonction MILLISECONDS

La fonction **MILLISECONDS** traduit une variable de durée en variable numérique.

&nbsp;

Arguments

* La variable à traduire
* Le type de conversion :
  * Si TRUE, retourne la durée totale exprimée en nombre de millisecondes
  * Si FALSE, retourne simplement le composant "millisecondes" de la durée exprimée

&nbsp;

Valeur de retour

Une variable numérique similaire à la variable temporelle à convertir, dont les valeurs numériques dépendent des arguments spécifiés

#### Syntaxe :&nbsp;

Q01.MILLISECONDS(TotalCount; NaValue)

ou

\_MILLISECONDS(Q01; TotalCount; NaValue)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | TotalCount | Booléen | Si TRUE, comptabilise la durée complète (nombre décimal possible) Si FALSE, extrait simplement la composante "MILLISECONDES" | TRUE par défaut |
| &#50; | NaValue | Nombre | Valeur à utiliser pour les sans réponses | Sans réponse par défaut |


#### Exemples :

DURATION.MILLISECONDS(FALSE)

Retourne une variable numérique qui représente le composant "millisecondes" de la variable DURATION.

&nbsp;

DURATION.MILLISECONDS(TRUE)

Retourne une variable numérique qui représente la durée totale exprimée en nombre de millisecondes.

&nbsp;

Voir aussi : [Manipuler les variables temporelles et de durées](<Manipulerlesvariablestemporelle1.md>)
