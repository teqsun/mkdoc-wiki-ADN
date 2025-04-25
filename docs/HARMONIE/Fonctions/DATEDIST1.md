# DATEDIST

## Fonction DATEDIST

La fonction **DATEDIST** calcule une variable logique qui correspond à la distribution d'une variable temporelle, selon une résolution donnée.

&nbsp;

| YEAR | Année |
| --- | --- |
| MONTH | Mois |
| DAY | Jours |
| WEEK | Semaines |
| HOUR | Heures |
| MINUTE | Minutes |
| SECOND | Secondes |


#### Syntaxe :&nbsp;

Q01.DATEDIST(Resolution; Format)

ou

\_DATEDIST(Q01; Resolution; Format)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Resolution | Chaîne de caractères | résolution day/week/month/year | vide par défaut |
| &#50; | Format | Chaîne de caractères | Format utilisé pour libeller les modalités créées | vide par défaut |


#### Remarques :

Le format détermine la façon de nommer les tranches. Le plus simple consiste à laisser l'argument vide.

Pour plus d'information sur les formats possibles : https://docs.microsoft.com/en-us/dotnet/standard/base-types/standard-date-and-time-format-strings

#### Exemples :

DATES.DATEDIST("MONTH")

Crée une variable logique dont les modalités sont les tranches mensuelles de la plus petite date à la plus grande date rencontrée avec conservation des valeurs intermédiaires vides.

&nbsp;

Voir aussi : [Manipuler les variables temporelles et de durées](<Manipulerlesvariablestemporelle1.md>)
