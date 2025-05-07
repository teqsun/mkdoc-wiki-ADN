# RANDOM

## Fonction RANDOM

La fonction **RANDOM** génère une variable numérique aléatoire dont les valeurs sont comprises entre un minimum et un maximum.

La racine (Seed) permet de contrôler l'aléatoire de façon à ce qu'il soit reproductible.

Il est possible d'intégrer un pourcentage de sans-réponses.

#### Syntaxe :&nbsp;

\_RANDOM(Level; MinValue; MaxValue; Seed; PercentNa; Dim)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Level | Chaîne de caractères | Nom du niveau cible (la variable créée sera sur ce niveau) | &nbsp; |
| &#49; | MinValue | Entier | Valeur mini | &#49; par défaut |
| &#50; | MaxValue | Entier | Valeur maxi | &#49;00 par défaut |
| &#51; | Seed | Entier | Germe aléatoire (-1 par défaut) | \-1 par défaut |
| &#52; | PercentNa | Entier | Valeur entre 0 et 100 : pourcentage de sans-réponses à intégrer | &#48; par défaut |
| &#53; | Dim | Scalaire ou vecteur | Si scalaire, nombre de colonnes. Si vecteur (2 valeurs) nombre de colonnes puis nombre de lignes.&nbsp; | Optionnel |


&nbsp;

Voir aussi :&nbsp;

[Manipuler les variables numériques](<Manipulerlesvariablesnumeriques1.md>)

[Création de variables (Système, aléatoire...)](<CreerdesvariablesdetoutepieceSys.md>)