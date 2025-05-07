# REREPLACE

## Fonction REREPLACE

La fonction **REREPLACE** remplace des parties d'une variable littérale par une autre.

Cette fonction très puissante permet de reformuler un texte.

&nbsp;

Arguments :

\- regex&nbsp; : l'expression régulière qui identifie ce qu'il faut remplacer

\- replacement&nbsp; : ce par quoi il faut remplacer ($1, $2 etc. pour utiliser des groupes de regex)

#### Syntaxe :&nbsp;

Q01.REREPLACE(Expression; Replacement)

ou

\_REREPLACE(Q01; Expression; Replacement)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Expression | Chaîne de caractères | Expression régulière de séléction | Obligatoire |
| &#50; | Replacement | Chaîne de caractères | Nouvelle chaîne | Obligatoire |


#### Remarques :

Pour plus d'information sur les expressions régulières :

http://lgmorand.developpez.com/dotnet/regex/

&nbsp;

Pour tester et construire les expressions régulières :

http://regexstorm.net/tester

http://www.ultrapico.com/expresso.htm

#### Exemples :

DATES.REREPLACE("\\\\d\\\\d/(\\\\d\\\\d)/\\\\d\\\\d\\\\d\\\\d"; "\!$1")

Retourne une variable littérale dans laquelle les dates au format JJ/MM/AAAA sont remplacées par le numéro de mois préfixé par un point d'exclamation.

&nbsp;

Voir aussi : [Expressions régulières](<REGULAR\_EXPRESSIONS1.md>)