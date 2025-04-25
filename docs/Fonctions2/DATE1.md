# DATE

## Fonction DATE

La fonction **DATE** crée une variable temporelle constante dont les composantes sont définies une à une, par les arguments.

La variable sera crée sur le niveau spécifié en premier argument.

#### Syntaxe :

\_DATE(LevelName; Year; Month; Day; Hour; Minute; Second; Millisecond)

&nbsp;

| &nbsp; | Nom&nbsp; | Type&nbsp; | Description | Remarque |
| --- | --- | --- | --- | --- |
| &#49; | LevelName | Chaîne de caractères | Nom du niveau cible | Obligatoire |
| &#50; | Year | Entier | Année | &#48; par défaut |
| &#51; | Month | Entier | Mois (de 1 à 12) | &#48; par défaut |
| &#52; | Day | Entier | Jour (de 1 à 31) | &#48; par défaut |
| &#53; | Hour | Entier | Heure (de 0 à 23) | &#48; par défaut |
| &#54; | Minute | Entier | Minute (de 0 à 59) | &#48; par défaut |
| &#55; | Second | Entier | Seconde (de 9 à 59) | &#48; par défaut |
| &#56; | Millisecond | Entier | Millisecondes | &#48; par défaut |


#### Exemples :

\_DATE("UNITS";2020;3;17)

&nbsp;

Voir aussi : [Manipuler les variables temporelles et de durées](<Manipulerlesvariablestemporelle1.md>)
