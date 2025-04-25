# TODATE

## Fonction TODATE

La fonction **TODATE** construit une variable temporelle (date/heure) depuis une variable textuelle ou continue (nombre de jours depuis le 1/1/1900).

Si la variable est textuelle, il faut indiquer une liste de masques de lecture.

&nbsp;

**ATTENTION, une variable temporelle DATE ne doit pas être utilisée directement dans un tableau, il faut la convertir au préalabe en lui appliquant par exemple la fonction DTOT().**

&nbsp;

&nbsp;

Arguments&nbsp;

La liste d'arguments correspond aux différents masques de lectures possibles.

Un masque décrit la date/heure à lire sous la forme d'une chaîne de caractères composée des caractères suivants :

&nbsp;

| y | Année |
| --- | --- |
| M | Mois |
| d | Jours |
| H | Heures |
| m | Minutes |
| s | Secondes |
| f | Fractions de seconde |


&nbsp;

Attention \! dans l'expression du format, la casse est importante : respectez bien les majuscules et les minuscules \!

&nbsp;

Valeur de retour

Une variable temporelle dont les dates correspondent au décodage de la variable littérale selon les différents formats listés.

Les valeurs qui ne correspondent pas à un format iront en sans-réponses.

#### Syntaxe :&nbsp;

Q01.TODATE(Formats; FormatDelimiter; DefaultValue)

ou

\_TODATE(Q01; Formats; FormatDelimiter; DefaultValue)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Formats | Chaîne de caractères | Format de lecture | NUL par défaut |
| &#50; | FormatDelimiter | Chaîne de caractères | Séparateur | NUL par défaut |
| &#51; | DefaultValue | Chaîne de caractères | Valeur des sans-réponse | NUL par défaut |


#### Exemples :

DATES.TODATE("d/M/yyyy")

Décode la variable littérale DATES et lit les jours, les mois et les années pour des saisies telles que 12/1/2016 et 12/11/2016.

&nbsp;

DATEC.TODATE()

Décode la variable continue DATEC&nbsp;

&nbsp;

TIMES.TODATE("yyyy-MM-dd HH:mm:ss,fff")

Décode la variable littérale TIMES et lit les années, les mois, les jours, les heures, les minutes, les secondes et les fraction de secondes telles que rencontrées dans "2016-11-29 16:49:52,531".

&nbsp;

Voir aussi : [Manipuler les variables temporelles et de durées](<Manipulerlesvariablestemporelle1.md>)
