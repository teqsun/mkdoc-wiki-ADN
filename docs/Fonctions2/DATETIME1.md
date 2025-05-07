# DATETIME

## Fonction DATETIME

La fonction **DATETIME** construit une nouvelle variable temporelle, depuis une date donnée sous forme de chaîne de caractères.

#### Syntaxe :&nbsp;

\_DATETIME(Level; Value; Format)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Level | Chaîne de caractères | Niveau cible | Obligatoire |
| &#50; | Value | Chaîne de caractères | La valeur de la date à décoder | Obligatoire |
| &#51; | Format | Chaîne de caractères | Format de décodage de la date | vide par défaut |


#### Remarques :

Attention \! dans l'expression du format, la casse est importante : respectez bien les majuscules et les minuscules \!

| y | Année |
| --- | --- |
| M | Mois |
| d | Jours |
| H | Heures |
| m | Minutes |
| s | Secondes |
| f | Fractions de seconde |


#### Exemples :

\_DATETIME("UNITS"; "4/10/1957"; "d/M/yyyy")

Crée la variable du 4 octobre 1957.

&nbsp;

(Consultez les fonctions \_NOW ou SYS pour créer une variable qui correspond à la date actuelle)

&nbsp;

Voir aussi : [Manipuler les variables temporelles et de durées](<Manipulerlesvariablestemporelle1.md>)