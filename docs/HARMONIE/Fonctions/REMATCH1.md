# REMATCH

## Fonction REMATCH

La fonction **REMATCH** retourne un filtre qui indique si la variable littérale testée vérifie l'expression régulière en argument.

Cette fonction est très pratique pour vérifier la bonne écriture des codes complexes, emails, adresses, etc.

&nbsp;

Arguments :

\- regex&nbsp; : l'expression régulière testée

#### Syntaxe :&nbsp;

Q01.REMATCH(Expression)

ou

\_REMATCH(Q01; Expression)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Expression | Chaîne de caractères | Expression régulière de séléction | Obligatoire |


#### Remarques :

Pour plus d'information sur les expressions régulières :

http://lgmorand.developpez.com/dotnet/regex/

&nbsp;

Pour tester et construire les expressions régulières :

http://regexstorm.net/tester

http://www.ultrapico.com/expresso.htm

#### Exemples :

CODES.REMATCH("\^\\\\w+$")

Retourne un filtre qui donne 'vrai' pour les individus qui ont donné un code alpha-numérique et 'faux' pour les autres.

&nbsp;

Voir aussi : [Expressions régulières](<REGULAR\_EXPRESSIONS1.md>)