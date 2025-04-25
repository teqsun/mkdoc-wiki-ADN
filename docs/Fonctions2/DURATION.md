# DURATION

## Fonction DURATION

La fonction **DURATION** calcule une variable numérique qui correspond à la durée entre les deux variables date sélectionnées.

#### Syntaxe :&nbsp;

\_DURATION(Start; Finish)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Start | Variable | Variable de type date | Obligatoire |
| &#50; | Finish | Variable | Variable de type date | Obligatoire |


#### Exemples :

\_DURATION(DATE\_ENTREE; DATE\_SORTIE)

La variable obtenue correspond à la durée entre les dates.

#### Remarques :

Cette durée devra être convertie en une unité de temps avec les fonctions [DURATIONDIST](<DURATIONDIST1.md>), [MILLISECONDS](<MILLISECONDS1.md>), [SECONDS](<SECONDS1.md>), [MINUTES](<MINUTES1.md>), [HOURS](<HOURS1.md>) ou [DAYS](<DAYS1.md>).

&nbsp;

Voir aussi : [Manipuler les variables temporelles et de durées](<Manipulerlesvariablestemporelle1.md>)
