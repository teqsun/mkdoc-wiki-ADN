# TABMOD

## Fonction TABMOD

La fonction **TABMOD** applique une table de recodification externe à une variable.

&nbsp;

Le nom de la table est indiquée par une chaîne de caractère, selon le principe de repérage des tables externes.

&nbsp;

Cette fonction joue un rôle particulier car elle permet de réaliser toutes les opérations courantes sur les modalités (extractions, groupements...) par analyse du contenu de fichiers texte, au format CSV. La définition est ainsi indépendante des études et peut être utilisée dans des vagues successives, avec des mises à jour qui seront prises en compte automatiquement en cas d'absence de stockage de la variable.&nbsp;

Le résultat est toujours une variable logique, multi-réponses ou discrète.

&nbsp;

La variable traitée peut être numérique ou logique.

Si la variable est numérique, les codes indiqués représentent les valeurs numériques à utiliser et ne sont pas forcément présentes dans les données.

Si la variable est logique, les codes indiqués correspondent à des modalités et doivent être disponibles, donc au plus égaux au nombre de modalités.

La valeur zéro (0), est autorisée pour générer des modalités vides.

&nbsp;

Les colonnes de la table lue suivent la structure décrite ci-après.

&nbsp;

La colonne CODE contient les n ° de modalités à regrouper sur une même ligne.

Il s'agit d'une simple liste.

. 17&nbsp; &nbsp; La modalité correspond aux occurrences du code 17

. 17&nbsp; 19&nbsp; &nbsp; La modalité correspond aux occurrences des codes 17 ou 19

. 17 TO 21&nbsp; &nbsp; La modalité correspond aux occurrences des codes 17, 18, 19, 20 ou 21&nbsp;

&nbsp;

La colonne des libellés indique les textes (forcés) ou non (reprise du libellé initial).

Pour récupérer un libellé initial, mettre un "#".

&nbsp;

Si l'étude comporte plusieurs langues, l’intitulé de la colonne est complété par le code international de la langue, entre parenthèses. Exemple : LONG(FR), SHORT(GB).

&nbsp;

L'insertion de sous-titres est autorisée. Dans ce cas, seule les colonnes de libellés sont remplies.&nbsp;

Le nombre de "\&" qui hiérarchise les sous-titres doit être respecté.

&nbsp;

Les fonctions TABCOL et TABROW fonctionnent exactement sur le même mode, mais la première s'applique à la dimension "colonnes" et la seconde à la dimension "lignes" de la variable source.

#### Syntaxe :&nbsp;

Q01.TABMOD(TableExpression; Indentation)

ou

\_TABMOD(Q01; TableExpression; Indentation)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | TableExpression | Chaîne de caractères | Table descriptive des codes | Obligatoire |
| &#50; | Indentation | Caractère | &nbsp; | ESPACE par défaut |


#### Exemples :

\_TABMOD(Q02A; "COUNTRIES")

Retourne une variable qui est le résultat de l'application de la table de recodification à la variable Q02A.

#### Remarques :

La fonction TABMOD supprime les espaces en fin de libellés.

&nbsp;

&nbsp;

Voir aussi : [Utilitaires \& divers](<TOOLS\_MISC1.md>)
