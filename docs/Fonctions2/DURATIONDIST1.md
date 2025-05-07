# DURATIONDIST

## Fonction DURATIONDIST

La fonction **DURATIONDIST** calcule une variable logique qui correspond à la distribution des durées selon des tranches imposées.

#### Syntaxe :&nbsp;

Q01.DURATIONDIST(unité; Step; Format)

ou

\_DURATIONDIST(Q01; unité; Step; Format)

&nbsp;

| &nbsp; | Nom&nbsp; | Type&nbsp; | Description | Remarque |
| --- | --- | --- | --- | --- |
| &#49; | unité | Chaîne de caractères | résolution&nbsp; | vide par défaut |
| &#50; | Step | Entier | pas | &#48; par défaut |
| &#51; | Format | Chaîne de caractères | Format d'affichage dans les libellés de modalités | vide par défaut |


#### Remarques :

L'unité est une valeur de la table :

&nbsp;

| MILLISECONDS | En millisecondes |
| --- | --- |
| SECONDS | En secondes |
| MINUTES | En minutes |
| HOURS | En heures |
| DAYS | En jours |


Pour plus d'informations sur le format :

https://docs.microsoft.com/en-us/dotnet/standard/base-types/standard-timespan-format-strings

#### Exemples :

DURATIONS.DURATIONDIST("MINUTES"; 5)

Crée une variable logique dont les modalités sont les tranches de durée de 5 minutes, de la plus petite à la plus grande (5 min, 10 min, etc.).

&nbsp;

Voir aussi :&nbsp; [Manipuler les variables temporelles et de durées](<Manipulerlesvariablestemporelle1.md>)
