# TIMESPAN

## Fonction TIMESPAN

La fonction **TIMESPAN** crée une variable de durée constante sur un niveau statistique donné.

#### Syntaxe :&nbsp;

Q01.TIMESPAN(Level; Days; Hours; Minutes; Seconds; Milliseconds)

ou

\_TIMESPAN(Q01; Level; Days; Hours; Minutes; Seconds; Milliseconds)

&nbsp;

| &nbsp; | Nom&nbsp; | Type&nbsp; | Description | Remarque |
| --- | --- | --- | --- | --- |
| &#49; | Level | Chaîne de caractères | Nom du niveau statistiques à utiliser | Obligatoire |
| &#50; | Days | Entier | Nombre de jours | &#48; par défaut |
| &#51; | Hours | Entier | Nombre d'heures | &#48; par défaut |
| &#52; | Minutes | Entier | Nombre de minutes | &#48; par défaut |
| &#53; | Seconds | Entier | Nombre de secondes | &#48; par défaut |
| &#54; | Milliseconds | Entier | Nombre de millisecondes | &#48; par défaut |


#### Remarques :

Le résultat est une durée qui représente la somme de ces composantes.

Cette durée pourra par exemple être ajoutée ou soustraite à une date (pour créer un intervalle de temps) ou à une autre durée.

&nbsp;

Voir aussi : [Manipuler les variables temporelles et de durées](<Manipulerlesvariablestemporelle1.md>)
