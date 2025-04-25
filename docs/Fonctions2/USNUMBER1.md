# USNUMBER

## Fonction USNUMBER

La fonction **USNUMBER** permet de calculer un identifiant numérique par incrémentation. \
Il est nécessaire de spécifier sur quel niveau de réponse on souhaite créer la variable.

#### Syntaxe :&nbsp;

\_USNUMBER(Level; FirstRecordValue)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Level | Chaîne de caractères | Nom du niveau à identifier | NUL par défaut |
| &#50; | FirstRecordValue | Entier | Première valeur | &#49; par défaut |


#### Exemples :

\_USNUMBER("UNITS"; 1001)

Crée une variable numérique qui commence à 1001 pour le 1er enregistrement puis qui incrémente de 1 à chaque nouvel enregistrement.

&nbsp;

Voir aussi :&nbsp;

[Utilitaires \& divers](<TOOLS\_MISC1.md>)

[Création de variables (Système, aléatoire...)](<CreerdesvariablesdetoutepieceSys.md>)
