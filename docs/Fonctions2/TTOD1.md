# TTOD

## Fonction TTOD

La fonction **TTOD** est le pendant de la fonction DTOT : elle traduit une variable littérale (TEXT) en variable logique à modalités.&nbsp;

Il est possible de créer une variable multi-réponses en indiquant le délimiteur de réponses.&nbsp;

Enfin, la casse peut être prise en compte ou ignorée.

&nbsp;

Argument 1 : Si TRUE, la casse (majuscules/minuscules) est importante, si FALSE elle est ignorée.

Argument 2 (optionnel) : Le séparateur de réponses utilisé dans les textes, entre double-quotes.

#### Syntaxe :&nbsp;

Q01.TTOD(IgnoreCase; Delimiters)

ou

\_TTOD(Q01; IgnoreCase; Delimiters)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | IgnoreCase | Booléen | Insensible à la casse si TRUE (passe les libellés des modalités en majuscules) | FALSE par défaut |
| &#50; | Delimiters | Chaîne de caractères | Séparateur à utiliser pour les multi-réponses | NUL par défaut |


#### Exemples :

Q01A.TTOD(TRUE; ";")

Crée une modalité par texte rencontré dans les réponses, en ignorant la casse, et en considérant que le point-virgule est un délimiteur de réponse. Cet exemple produit donc une variable multi-réponses.

&nbsp;

Voir aussi : [Traiter les variables littérales](<Traiterlesvariableslitterales.md>)