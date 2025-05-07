# DAYS

## Fonction DAYS

La fonction **DAYS** traduit une variable de durée en variable numérique.

#### Syntaxe :&nbsp;

Q01.DAYS(TotalCount; NaValue)

ou

\_DAYS(Q01; TotalCount; NaValue)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | TotalCount | Booléen | Si TRUE, comptabilise la durée complète (nombre décimal possible) Si FALSE, extrait simplement la composante "JOURS" | TRUE par défaut |
| &#50; | NaValue | Nombre | Valeur à utiliser pour les sans réponses | Sans réponse par défaut |


#### Exemples :

DURATION.DAYS(FALSE)

Retourne une variable numérique qui représente le composant "jour" de la variable DURATION.

&nbsp;

DURATION.DAYS(TRUE)

Retourne une variable numérique qui représente la durée totale exprimée en nombre de jours.

&nbsp;

Voir aussi : [Manipuler les variables temporelles et de durées](<Manipulerlesvariablestemporelle1.md>)