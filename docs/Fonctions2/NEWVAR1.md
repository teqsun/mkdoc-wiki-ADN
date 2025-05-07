# NEWVAR

## Fonction NEWVAR

La fonction **NEWVAR** génère une variable logique ou numérique.

#### Syntaxe :&nbsp;

\_NEWVAR(NbMod; Level; Dim; Value)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | NbMod | Entier positif ou nul | Si 0 création d'une variable numérique sinon nombre de modalités à créer | Obligatoire |
| &#50; | Level | Chaîne de caractères | Nom du niveau cible (la variable créée sera sur ce niveau) | Optionnel : Niveau courant par défaut |
| &#51; | Dim | Scalaire ou vecteur | Si scalaire, nombre de colonnes. Si vecteur (2 valeurs) nombre de lignes puis nombre de colonnes.&nbsp; | Optionnel |
| &#52; | Value | Valeur | valeur de la réponse ou de la modalité. Peut être une valeur à décimales si création d'une variable continue | Optionnel |


&nbsp;

#### Exemples :

\_NEWVAR(0)

Crée une variable numérique où tous les individus sont en sans-réponse.

&nbsp;

\_NEWVAR(5)

Crée une variable logique à 5 modalités où tous les individus sont en sans-réponse.

&nbsp;

\_NEWVAR(5;"MAIN\_US";NULL;2)

Crée une variable logique à 5 modalités dans le niveau MAIN\_US où tous les individus sont en modalité 2.

&nbsp;

\_NEWVAR(0;NULL;3 5;100)

Crée une variable numérique à 3 lignes et 5 colonnes dans le niveau courant où tous les individus ont la valeur 100.

&nbsp;

\_NEWVAR(1;"MAIN\_US";NULL;1).TXTMOD(1;"Ensemble")

Crée une variable logique à une seule modalité regroupant tous les individus et ayant le libellé "Ensemble". C'est donc un filtre qui sélectionne l'ensemble des individus du niveau MAIN\_US.

&nbsp;

\_NEWVAR(0;NULL;10;1).CUMCOL()

Crée une variable numérique à 10 colonnes respectivelment remplies des valeurs 1 à 10

&nbsp;

&nbsp;

Voir aussi :&nbsp;

[Manipuler les variables numériques](<Manipulerlesvariablesnumeriques1.md>)

[Création de variables (Système, aléatoire...)](<CreerdesvariablesdetoutepieceSys.md>)