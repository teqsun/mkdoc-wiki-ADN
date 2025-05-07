# MIMAX

## Fonction MIMAX

La fonction **MIMAX** circonscrit une variable numérique en lui appliquant une borne inférieure et/ou supérieure.

&nbsp;

Argument 1 : la valeur minimale (plancher)

Argument 2 : la valeur maximale (plafond)

Argument 3 optionnel : TRUE (par défaut) pour autoriser la valeur minimale, FALSE pour l'exclure

Argument 4 optionnel : TRUE (par défaut) pour autoriser la valeur maximale, FALSE pour l'exclure

Argument 5 optionnel : TRUE pour ramener les valeurs hors zone à la borne, FALSE (par défaut) pour les mettre à Sans-Réponse

#### Syntaxe :&nbsp;

Q01.MIMAX(MinValue; MaxValue; IncludeMini; IncludeMaxi; ForceInsideRangeMode)

ou

\_MIMAX(Q01; MinValue; MaxValue; IncludeMini; IncludeMaxi; ForceInsideRangeMode)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | MinValue | Nombre | Valeur mini | &#49; par défaut |
| &#50; | MaxValue | Nombre | Valeur maxi | Nombre maximal par défaut |
| &#51; | IncludeMini | Booléen | Par défaut mini inclus | TRUE par défaut |
| &#52; | IncludeMaxi | Booléen | par défaut, maxi inclus | TRUE par défaut |
| &#53; | ForceInsideRangeMode | Booléen | Par défaut, les hors intervalle sont en sans-réponse | FALSE par défaut |


#### Exemples :

AGE.MIMAX(18; 99; TRUE; TRUE; TRUE)

La variable produite représente l'âge entre 18 et 99 compris. Les valeurs initialement hors champ sont ramenées à la borne la plus proche.

&nbsp;

AGE.MIMAX(18; 99)

La variable produite représente l'âge entre 18 et 99 compris. Les valeurs initialement hors champ sont éliminées (sans-réponse).

&nbsp;

Voir aussi : [Manipuler les variables numériques](<Manipulerlesvariablesnumeriques1.md>)