# HOURS

## Fonction HOURS

La fonction **HOURS** traduit une variable de durée en variable numérique.

Le résultat est une variable numérique similaire à la variable temporelle à convertir, dont les valeurs numériques dépendent des arguments spécifiés

#### Syntaxe :&nbsp;

Q01.HOURS(TotalCount; NaValue)

ou

\_HOURS(Q01; TotalCount; NaValue)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | TotalCount | Booléen | Si TRUE, comptabilise la durée complète (nombre décimal possible) Si FALSE, extrait simplement la composante "HEURES" | TRUE par défaut |
| &#50; | NaValue | Nombre | Valeur à utiliser pour les sans réponses | Sans réponse par défaut |


#### Exemples :

DURATION.HOURS(FALSE)

Retourne une variable numérique qui représente le composant "heures" de la variable DURATION.

&nbsp;

DURATION.HOURS(TRUE)

Retourne une variable numérique qui représente la durée totale exprimée en nombre de heures.

&nbsp;

Voir aussi : [Manipuler les variables temporelles et de durées](<Manipulerlesvariablestemporelle1.md>)