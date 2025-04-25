# TOMOD

## Fonction TOMOD

La fonction **TOMOD** est une consigne qui permet de représenter une variable numérique sous forme de modalité et d'en contrôler le calcul affiché.

Cette fonction est très utile pour le traitement des échelles ou des multi-réponses pour lesquelles on souhaite ajouter un nombre moyen ou un écart-type (etc.).

&nbsp;

#### Attention : Ne pas utiliser cette fonction sur une variable dimensionnée.

#### Syntaxe :&nbsp;

Q01.TOMOD(Calculations; Label; PreserveTitle)

ou

\_TOMOD(Q01; Calculations; Label; PreserveTitle)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Calculations | Chaîne de caractères | Liste des calculs à appliquer séparés par des ',' ou des ',,' | NUL par défaut |
| &#50; | Label | Chaîne de caractères | Libellé de la modalité | NUL par défaut |
| &#51; | PreserveTitle | Booléen | Si TRUE, crée un sous-titre qui correspond au titre de la variable traitée | FALSE par défaut |


#### Remarques :

Attention, TOMOD est une consigne : elle est évaluée dynamiquement lors du calcul des tableaux (comme RECAP).

Pour ajouter l'affichage des tests de significativité dans les tableaux, utilisez le nom de calcul TESTQ1 (TEST statistique appliqué au Quantités).

Si le contrôle du calcul affiché n'est pas nécessaire, il est préférable d'utiliser la fonction [JUXVAR](<JUXVAR1.md>).

**La méthode Q01.MOD($M $Q) est plus généralisable en particulier pour les variables dimensionnées.**

#### Exemples :

\_JUXVAR(Q1; Q1Q.TOMOD("MEAN,,TESTQ1"; "Moyenne et test")

&nbsp;

Voir aussi :&nbsp;

Sélection "étendue" de modalités/détails

[Liste des calculs standards ](<Calculsstandards1.md>)

[Utilitaires \& divers](<TOOLS\_MISC1.md>)

[Présenter les variables dans les tableaux](<Presenterlesvariablesdanslestab1.md>)
