# REFORMAT

## Fonction REFORMAT

La fonction **REFORMAT** réécrit une variable littérale à l'aide d'une expression régulière.

&nbsp;

Arguments :

\- regex&nbsp; : l'expression régulière qui identifie ce qu'il faut traiter

\- format&nbsp; : le format de réécriture (utiliser $1, $2 etc. pour utiliser des sous-groupes de regex)

#### Syntaxe :&nbsp;

Q01.REFORMAT(Expression; Format)

ou

\_REFORMAT(Q01; Expression; Format)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Expression | Chaîne de caractères | Expression régulière de sélection | Obligatoire |
| &#50; | Format | Chaîne de caractères | Format | NUL par défaut |


#### Remarques :

Pour plus d'information sur les expressions régulières :

http://lgmorand.developpez.com/dotnet/regex/

&nbsp;

Pour tester et construire les expressions régulières :

http://regexstorm.net/tester

http://www.ultrapico.com/expresso.htm

#### Exemples :

DATES.REFORMAT("(\\\\d\\\\d)/(\\\\d\\\\d)/(\\\\d\\\\d\\\\d\\\\d)")

Retourne une variable littérale qui ne contient plus que la date au format JJ/MM/AAAA.

&nbsp;

Voir aussi : [Traiter les variables littérales](<Traiterlesvariableslitterales.md>)