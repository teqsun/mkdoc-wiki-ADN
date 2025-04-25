# SRTCOL

## Fonction SRTCOL

La fonction **SRTCOL** hiérarchise les colonnes d'une variable logique sur la base des effectifs d'une modalité de référence.

L'ordre des colonnes de la variable obtenue dépend donc des données.

#### Syntaxe :&nbsp;

Q01.SRTCOL(Criteria; Ascendant; Universe; Weight)

ou

\_SRTCOL(Q01; Criteria; Ascendant; Universe; Weight)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Criteria | Valeur | Numéro de la modalité de référence ou opérateur sur continue | &#49; par défaut |
| &#50; | Ascendant | Booléen | TRUE pour un tri ascendant, FALSE (par défaut) pour un tri descendant. | FALSE par défaut |
| &#51; | Universe | Variable | Univers optionnel à utiliser | NUL par défaut |
| &#52; | Weight | Variable | Pondération optionnelle à utiliser | NUL par défaut |


#### Exemples :

S1.SRTCOL(1; TRUE; S3 1; POIDS)

Retourne une variable dont les colonnes sont hiérarchisées dans l'ordre croissant selon les effectifs pondérés ('POIDS') sur la population 'S3 1' de la 1ère modalité.

&nbsp;

#### Remarques :

La fonction SRTCOL supporte les variables continues, dans ce cas le critère est [l'opérateur de réduction](<Reductions1.md>) associé :

Q1.SRTCOL("MEAN"; TRUE)[Réductions](<Reductions1.md>)

&nbsp;

Voir aussi : [Gestion des dimensions](<Gererlesdimensionsdesvariables1.md>)
