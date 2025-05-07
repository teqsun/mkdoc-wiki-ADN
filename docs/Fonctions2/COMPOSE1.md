# COMPOSE

## Fonction COMPOSE

La fonction **COMPOSE** s'impose lorsqu'il s'agit de créer un critère complexe depuis une table externe.

&nbsp;

Le nom de la table est indiquée par une chaîne de caractère, selon le principe de repérage des tables externes.

&nbsp;

La table attendue possède autant de colonnes que désiré sachant que :

\- la dernière colonne contient les définition à exécuter pour chacune des modalités. A noter que la sélection des répondants de la définition est automatique : inutile de les spécifier.

\- les colonnes qui précèdent représentent les textes des modalités selon les différents niveaux hiérarchiques nécessaires.

#### Syntaxe :&nbsp;

Q01.COMPOSE(Expression)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Expression | Chaîne de caractères | Chaîne de caractères décrivant le nom et l'onglet du classeur Excel contenant la table externe à utiliser | Obligatoire |


#### Exemples :

\_COMPOSE(Q01;"PDT\!CRITERES")

Retourne une nouvelle variable depuis la table stockée dans le fichier Excel "PDT.xlsx" présent dans le répertoire de l'étude, dans l'onglet "CRITERES". Le résultat a autant de modalités qu'il y en a dans la table. Les répondants de chaque modalité sont ceux des définitions saisies dans la dernière colonne de chaque ligne de la table.

&nbsp;

Voir aussi :&nbsp;

[Utilisation de tables externes](<Utilisationdetablesexternes1.md>)

[Critères](<Creerdescriteresoubannieres1.md>)