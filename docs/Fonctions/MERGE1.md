# MERGE

## Fonction MERGE

La fonction **MERGE** colle les enregistrements des variables placées en argument et crée le niveau qui y correspond.

Ainsi, le nombre d'enregistrements de la variable résultat est la somme des nombres d'enregistrements des variables en argument.

#### Syntaxe :&nbsp;

\_MERGE(LevelName; Variables)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | LevelName | Chaîne de caractères | Nom du niveau cible (le niveau DOIT EXISTER) | Obligatoire |
| &#50; | Variables | Liste de variables | Liste des variables à fusionner, généralement sur des niveaux différents. Si le niveau d'arrivée existe déjà, alors les variables doivent être cohérentes avec les niveaux utilisés lors du 1er appel. | Obligatoire |


#### Remarques :

Cette fonction permet de réaliser une fusion d'études "manuelle" : vous importez les différentes études sous forme de niveaux à part entière (vous pouvez utiliser un masque de renommage pour bien isoler les variables). Puis vous créez les variables fusionnées à l'aide de MERGE. Il sera sans doute utile de recourir à FITMOD pour harmoniser les variables en question (au choix, sur les codes, les textes, etc.).

#### Exemples :

\_MERGE("PRODUITS";Q1A;Q1B)

&nbsp;

Voir aussi :&nbsp;

[Niveaux](<Niveaux1.md>)
