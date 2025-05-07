# ORDMOD

## Fonction ORDMOD

La fonction **ORDMOD** modifie l'ordonnateur de la variable traitée.

&nbsp;

L'argument est le vecteur des valeurs (exemple : 1 1 1 2 2 2) à inscrire dans les modalités de la variable.

#### Syntaxe :&nbsp;

Q01.ORDMOD(Values; Selection)

ou

\_ORDMOD(Q01; Values; Selection)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Values | Liste d'entiers | Vecteur des valeurs à écrire (exemple : 1 1 1 2 2 2)&nbsp; | peut être vide |
| &#50; | Selection | Liste de valeurs | Liste des positions affectées (tout si indéfini) | Indéfini par défaut |


#### Remarques :

Il n'est pas nécessaire d'indiquer autant de valeurs qu'il y a d'éléments affectés : la fonction répète automatiquement la liste des valeurs fournies.

Ainsi, une liste de valeurs "1 1 2" sera automatiquement répétée s'il y a 8 éléments à affecter : "1 1 2 1 1 2 1"

Si le ORDMOD est utilisé sans paramètre, l'ordonnateur est déterminé automatiquement en fonction des sous-titres.&nbsp;

#### Exemples :

S1.ORDMOD(1 1 1 2 2)

Modifie complètement l'ordonnateur de la variable S1 - indépendamment de sa taille.

&nbsp;

S1.ORDMOD(1; -1)

Modifie la valeur de l'ordonnateur de la DERNIERE modalité de la variable S1.

&nbsp;

Q2.ORDMOD()

Si Q2 est une variable logique à 6 modalités sous la forme :

| Modalité de la variable Q2 | Ordonnateur produit par Q2.ORDMOD() |
| --- | --- |
| Sous-titre 1 | &nbsp; |
| &nbsp;Modalité 1 | &#49; |
| &nbsp;Modalité 2 | &#49; |
| Sous-titre 2 | &nbsp; |
| &nbsp;Modalité 3 | &#50; |
| &nbsp;Modalité 4 | &#50; |


&nbsp;

&nbsp;

Voir aussi : [Propriétés des variables](<Modifierlesproprietesdesvariable.md>)