# SRTMOD

## Fonction SRTMOD

La fonction **SRTMOD** hiérarchise les modalités d'une variable sur la base de leur effectif.&nbsp;

L'ordre des modalités de la variable obtenue dépend donc des données.

#### Syntaxe :&nbsp;

Q01.SRTMOD(Ascendant; SortGroups; Universe; Weight)

ou

\_SRTMOD(Q01; Ascendant; SortGroups; Universe; Weight)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Ascendant | Booléen | TRUE pour un tri ascendant, FALSE (par défaut) pour un tri descendant. | FALSE par défaut |
| &#50; | SortGroups | Booléen | TRUE pour un tri hiérarchique (par sous-titres \& sous-totaux), FALSE pour un tri global. | FALSE par défaut |
| &#51; | Universe | Variable | Univers optionnel à utiliser | NUL par défaut |
| &#52; | Weight | Variable | Pondération optionnelle à utiliser | NUL par défaut |


#### Exemples :

S1.SRTMOD()

Retourne une variable dont les modalités sont hiérarchisées dans l'ordre décroissant, par groupe et selon les effectifs bruts.

&nbsp;

S1.SRTMOD(TRUE; FALSE; S3 1; POIDS)

Retourne une variable dont les modalités sont hiérarchisées dans l'ordre croissant, globalement, et selon les effectifs pondérés ('POIDS'), sur la population 'S3 1'

&nbsp;

&nbsp;

Voir aussi :&nbsp;

[Traiter les variables logiques (modalités)](<Traiterlesvariableslogiquesmoda1.md>)

[Présenter les variables dans les tableaux](<Presenterlesvariablesdanslestab1.md>)

[Gestion des dimensions](<Gererlesdimensionsdesvariables1.md>)

&nbsp;

&nbsp;
