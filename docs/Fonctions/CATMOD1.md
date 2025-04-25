# CATMOD

## Fonction CATMOD

La fonction **CATMOD** applique une table de regroupement externe à une variable.

&nbsp;

Le nom de la table est indiquée par une chaîne de caractère, selon le principe de[ repérage des tables externes.](<Utilisationdetablesexternes1.md>)

&nbsp;

Cette fonction joue un rôle particulier car elle permet de réaliser les opérations de regroupement hiérarchique sur les modalités, lignes ou colonnes par analyse du contenu de la table externe, au format Excel. La définition est ainsi indépendante des études et peut être utilisée dans des vagues successives, avec des mises à jour qui seront prises en compte automatiquement en cas d'absence de stockage de la variable.&nbsp;

Le résultat est toujours une variable logique, multi-réponses ou discrète.

&nbsp;

La variable traitée est logique.

&nbsp;

#### Syntaxe :&nbsp;

Q01.CATMOD(TableExpression; Field1; Field2)

ou

\_CATMOD(Q01; TableExpression; ; Field1; Field2)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | TableExpression | Chaîne de caractères | Table descriptive des codes (TAMOD) | Obligatoire |
| &#50; | Field1 | Chaîne de caractères | Nom de la colonne en entrée | Obligatoire |
| &#51; | Field2 | Chaîne de caractères | Nom de la colonne de sortie | Obligatoire |


#### Exemples :

Soit Q1, une variable logique avec les modalités qui représentent des villes du monde (ex:Paris, Lyon, Beijing...).

Les colonnes de la table (GEO.xlsx, onglet PAYS) lue suivent une structure du type :

&nbsp;

| **VILLE** | **PAYS** | **REGION** |
| --- | --- | --- |
| Paris | France | Europe |
| Lyon | France | Europe |
| Rome | Italie | Europe |
| Alexandrie | Egypte | Afrique |
| Beijing | Chine | Asie |


&nbsp;

Q1.CATMOD("GEO.XLSX\!PAYS";"VILLE";"PAYS")

Le résultat est une variable logiques avec 4 modalités Chine, Egypte, France, Italie qui sont les regroupement des modalités Paris + Lyon pour France, Rome pour Italie, Egypte pour Alexandrie et Chine pour Beijing.

Sur le même exemple la définition Q1.CATMOD("GEO.XLSX\!PAYS";"VILLE";"REGION")donne une variable avec les modalités Afrique, Asie et Europe.

