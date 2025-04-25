# FITCOL

## Fonction FITCOL

La fonction **FITCOL** permet d'aligner les colonnes d'une variable sur une autre.

&nbsp;

L'argument 2 correspond au mode de reconnaissance appliqué pour réaliser cet alignement.

#### Syntaxe :&nbsp;

Q01.FITCOL(Variable;MatchMode)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Variable | variable | Variable de référence | Obligatoire |
| &#50; | MatchMode | caractère | Mode de reconnaissance appliqué | Obligatoire |


&nbsp;

Les modes de reconnaissance :

* C (CODE): recherche par CODES
* E (EXACT): recherche complète (CODE + TEXTE)
* T (TEXT): recherche par texte
* S (SIMPLIFIED): recherche par texte simplifié (ignore accents, blancs etc.)
* N (NUMBER): aligne simplement la taille sans tenir compte d'un quelconque alignement
* R (REPEAT) : répète les modalités de la première variable pour s'accorder avec la variable de référence

#### Remarques :

FITCOL est une sorte de SELCOL dynamique.&nbsp;

Les fonctions FITCOL et FITROW fonctionnent exactement sur le même mode, mais la première s'applique à la dimension "colonnes" et la seconde à la dimension "lignes" de la variable en argument 1.

Cela permet un contrôle fin lors de l'interaction de deux variables (opérateur, FIX, FLT etc.), alignement de modalités, alignement de colonnes, etc.

#### Exemples :

Q01.FITMOD(Q02;"T")

Crée une nouvelle variable dont les colonnes sont les mêmes que celles de Q02 mais avec les données de Q01.

&nbsp;

&nbsp;

Voir aussi :&nbsp;

[Traiter les variables logiques (modalités)](<Traiterlesvariableslogiquesmoda1.md>)

[Combinaisons](<Combinerlesvariables1.md>)

[Gestion des dimensions](<Gererlesdimensionsdesvariables1.md>)

