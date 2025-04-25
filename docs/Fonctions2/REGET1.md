# REGET

## Fonction REGET

La fonction **REGET** extrait une partie d'une variable littérale à l'aide d'une expression régulière.

Très pratique pour extraire le mois d'une date, la première partie d'une phrase, etc.

&nbsp;

Arguments :

\- regex&nbsp; : l'expression régulière d'extraction. Chaque groupe entre parenthèses sera extrait.

\- delimiter : le délimiteur à utiliser pour 'coller' les différentes parties extraites (optionnel)

#### Syntaxe :&nbsp;

Q01.REGET(Expression; Delimiter)

ou

\_REGET(Q01; Expression; Delimiter)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Expression | Chaîne de caractères | Expression régulière de séléction | Obligatoire |
| &#50; | Delimiter | Chaîne de caractères | séparateur | "" par défaut |


#### Remarques :

Pour plus d'information sur les expressions régulières :

http://lgmorand.developpez.com/dotnet/regex/

&nbsp;

Pour tester et construire les expressions régulières :

http://regexstorm.net/tester

http://www.ultrapico.com/expresso.htm

#### Exemples :

DATES.REGET("\\\\d\\\\d/(\\\\d\\\\d)/\\\\d\\\\d\\\\d\\\\d")

Retourne une variable littérale qui contient le mois (la partie entre parenthèses) depuis une variable qui contient des dates au format JJ/MM/AAAA.

&nbsp;

Voir aussi : [Expressions régulières](<REGULAR\_EXPRESSIONS1.md>)
