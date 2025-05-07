# SUBSTRING

## Fonction SUBSTRING

La fonction **SUBTRING** extrait une partie de texte d'une variable littérale à l'aide d'un délimiteur et d'une position.

#### Syntaxe :&nbsp;

Q01.SUBSTRING(Index; LengthOrDelimiter)

ou

\_SUBSTRING(Q01; Index; LengthOrDelimiter)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Index | Entier | indice de la partie à extraire&nbsp; (1 : 1er caractère, 2: 2e caractère, -1: dernier caractère) | Obligatoire |
| &#50; | LengthOrDelimiter | Valeur | Délimiteur à utiliser.&nbsp; Le délimiteur peut être un nombre ou un caractère.&nbsp; Si c'est un nombre, on considère que chaque partie est composée d'autant de caractères | Obligatoire |


#### Exemples :

EMAIL.SUBSTRING(1; "@")

Retourne la partie 'gauche' d'une adresse électronique (celle qui précède le '@').

&nbsp;

Voir aussi : [Traiter les variables littérales](<Traiterlesvariableslitterales.md>)