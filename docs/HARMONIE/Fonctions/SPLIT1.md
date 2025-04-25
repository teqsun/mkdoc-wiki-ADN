# SPLIT

## Fonction SPLIT

La fonction **SPLIT** appliquée à une variable littérale découpe les textes cités en autant de 'détails' qu'il y a des parties délimitées rencontrées dans les réponses.

Quelle que soit la variable traitée, elle est automatiquement convertie en variable littérale, et le résultat est toujours une variable littérale.

#### Syntaxe :&nbsp;

Q01.SPLIT(Delimiters; ExpectedPartCount)

ou

\_SPLIT(Q01; Delimiters; ExpectedPartCount)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Delimiters | Chaîne de caractères | Délimiteurs à employer pour découper la chaîne en entrée | Obligatoire |
| &#50; | ExpectedPartCount | Entier | Nombre optionnel de parties attendues : permet de forcer le nombre de détails dans la variable résultat. | \-1 par défaut |


#### Exemples :

Q01A.SPLIT(" "; 5)

Retourne une variable littérale dimensionnée à 5 détails et dont les modalités correspondent aux différents 'mots' (séparés par des blancs) rencontrées dans les données d'origine.

&nbsp;

Q01A.SPLIT(" ")

Pareil que précédemment, mais le nombre de détails dépend directement du nombre maximum de mots rencontrés dans les données.

&nbsp;

Voir aussi : [Traiter les variables littérales](<Traiterlesvariableslitterales.md>)
