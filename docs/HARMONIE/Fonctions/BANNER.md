# BANNER

## Fonction BANNER

La fonction **BANNER** permet de regrouper plusieurs critères pour constituer une bannière (groupement de plusieurs variables). C'est une version plus évoluée de JUXVAR.

#### Syntaxe :&nbsp;

\_BANNER(Source;PropertyMask)

&nbsp;

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Source | Sélection de variables | liste de variables séparées par un ";" | Obligatoire |
| &#50; | PropertyMask | Chaîne de caractères | Un ou plusieurs caractères (les options peuvent se cumuler) | A : ajoute la base totale sur chaque source N : ajoute la base sans-réponse sur chaque source B : ajoute un [AUTOBASE](<AUTOBASE1.md>) global (inutile si A est spécifié) O : ajoute un [ORDMOD(1)](<ORDMOD1.md>) sur chaque source Q : supprime la partie numérique de chaque source&nbsp; |


&nbsp;

#### Exemples :

\_BANNER(S1; S3)

La variable résultante est, et pour chaque variable la suppression des modalités numériques, passsage de l'ordonnateur à 1 et ajout de la base répondants en 1e modalités, la concaténation de S1 et S3.

&nbsp;

\_BANNER(S1; S3;"O")

La variable résultante est la concaténation de S1 et S3 après passage des ordonnateurs à 1.

&nbsp;

#### Remarques :

La définition \_BANNER(S1; S3) est équivalente à \_BANNER(S1; S3; "AOQ")

&nbsp;

&nbsp;

Voir aussi :&nbsp;

[JUXVAR](<JUXVAR1.md>)
