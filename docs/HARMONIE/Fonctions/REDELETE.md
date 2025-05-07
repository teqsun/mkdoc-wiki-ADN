# REDELETE

## Fonction REDELETE

La fonction **REDELETE** supprime une partie d'une variable littérale à l'aide d'une expression régulière.

C'est un peu le pendant de REGET

&nbsp;

Arguments :

\- regex&nbsp; : l'expression régulière qui identifie ce qu'il faut supprimer

#### Syntaxe :&nbsp;

Q01.REDELETE(Expression)

ou

\_REDELETE(Q01; Expression)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Expression | Chaîne de caractères | Expression régulière de sélection des modalités | Obligatoire |


#### Remarques :

Pour plus d'information sur les expressions régulières :

http://lgmorand.developpez.com/dotnet/regex/

&nbsp;

Pour tester et construire les expressions régulières :

http://regexstorm.net/tester

http://www.ultrapico.com/expresso.htm

#### Exemples :

DATES.REDELETE("\\\\d\\\\d/\\\\d\\\\d/\\\\d\\\\d\\\\d\\\\d")

Retourne une variable littérale dans laquelle les dates au format JJ/MM/AAAA sont supprimées.

&nbsp;

Voir aussi :&nbsp;

[Traiter les variables littérales](<Traiterlesvariableslitterales.md>)

[Expressions régulières](<REGULAR\_EXPRESSIONS1.md>)