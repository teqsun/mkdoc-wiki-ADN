# TPROCMOD

## Fonction TPROCMOD

La fonction **TPROCMOD** applique un traitement textuel aux modalités d'une variable logique.

Les traitements à opérer sont spécifiés dans l'argument sous la forme d'une chaîne de caractère et suivent les traitements disponibles dans le moteur de lecture de données (champ 'PREPROCESS' des DATAMAP 2.0).

&nbsp;

Les fonctions TPROCCOL et TPROCROW fonctionnent exactement sur le même mode, mais la première s'applique à la dimension "colonnes" et la seconde à la dimension "lignes" de la variable source.

#### Syntaxe :&nbsp;

Q01.TPROCMOD(Expression; sélection)

ou

\_TPROCMOD(Q01; Expression; sélection)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Expression | Chaîne de caractères | Instruction de traitement | Obligatoire |
| &#50; | sélection | Liste de chaînes de caractères | Sélection des positions | NUL par défaut |


#### Exemples :

S1.TPROCMOD("TRIM, UPPER")

Retourne une variable logique dont les modalités sont successivement débarrassées des blancs en début et en fin, puis passées en majuscules.

&nbsp;

S1.TPROCMOD('UPPER(LEFT(@VALUE, 2)) \& " \!"')

Retourne une variable logique qui prend pour modalités les 2 premiers caractères des modalités d'origine, les passe en majuscules, puis y ajoute un point d'exclamation.

&nbsp;

Voir aussi :&nbsp;

[Gestion des libellés](<Gererleslibelleslestextes1.md>)

[Traiter les variables littérales](<Traiterlesvariableslitterales.md>)
