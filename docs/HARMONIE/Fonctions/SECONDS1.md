# SECONDS

## Fonction SECONDS

La fonction **SECONDS** traduit une variable de durée en variable numérique.

&nbsp;

Arguments

* La variable à traduire
* Le type de conversion :
  * Si TRUE, retourne la durée totale exprimée en nombre de secondes
  * Si FALSE, retourne simplement le composant "secondes" de la durée exprimée

&nbsp;

Valeur de retour

Une variable numérique similaire à la variable temporelle à convertir, dont les valeurs numériques dépendent des arguments spécifiés

#### Syntaxe :&nbsp;

Q01.SECONDS(TotalCount; NaValue)

ou

\_SECONDS(Q01; TotalCount; NaValue)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | TotalCount | Booléen | Si TRUE, comptabilise la durée complète (nombre décimal possible) Si FALSE, extrait simplement la composante "SECONDES" | TRUE par défaut |
| &#50; | NaValue | Nombre | Valeur à utiliser pour les sans réponses | Sans réponse par défaut |


#### Exemples :

DURATION.SECONDS(FALSE)

Retourne une variable numérique qui représente le composant "secondes" de la variable DURATION.

&nbsp;

DURATION.SECONDS(TRUE)

Retourne une variable numérique qui représente la durée totale exprimée en nombre de secondes.

&nbsp;

Voir aussi : [Manipuler les variables temporelles et de durées](<Manipulerlesvariablestemporelle1.md>)
