# SYS

## Fonction SYS

La fonction **SYS** construit une nouvelle variable dont la valeur dépend de la propriété système demandée.

&nbsp;

La fonction attend :

* niveau : nom du niveau de création (et nb unités statistiques)
* propertyName : nom de la propriété système

&nbsp;

| STUDY | Nom du fichier de l'étude (sans extension) |
| --- | --- |
| STUDY\_PATH | Nom complet du fichier de l'étude |
| STUDY\_FILE | Nom du fichier de l'étude (avec extension) |
| STUDY\_FOLDER | Nom du dossier de l'étude |
| USER | Nom de l'utilisateur actuel (licence) |
| USER\_EMAIL | Email de l'utilisateur actuel (licence) |
| NOW | Variable temporelle qui donne l'heure actuelle, lors de l'exécution |


#### Syntaxe :&nbsp;

\_SYS(Level; PropertyName)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | PropertyName | Chaîne de caractères | Nom de la propriété récupérée | Obligatoire |


#### Exemples :

\_SYS("UNITS"; "NOW")

Retourne une variable temporelle qui donne la date et l'heure actuelles, sur le niveau 'UNITS'.

&nbsp;

Voir aussi :&nbsp;

[Création de variables (Système, aléatoire...)](<CreerdesvariablesdetoutepieceSys.md>)
