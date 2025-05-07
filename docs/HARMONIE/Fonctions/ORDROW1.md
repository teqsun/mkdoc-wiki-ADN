# ORDROW

## Fonction ORDROW

La fonction **ORDROW** modifie l'ordonnateur de la dimension ligne de la variable traitée.

&nbsp;

L'argument est le vecteur des valeurs (exemple : 1 1 1 2 2 2) à inscrire dans les items lignes de la variable.

#### Syntaxe :&nbsp;

Q01.ORDROW(Values; Selection)

ou

\_ORDROW(Q01; Values; Selection)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Values | Liste d'entiers | Vecteur des valeurs à écrire (exemple : 1 1 1 2 2 2)&nbsp; | Obligatoire |
| &#50; | Selection | Liste de valeurs | Liste des positions affectées (tout si indéfini) | Indéfini par défaut |


#### Remarques :

Il n'est pas nécessaire d'indiquer autant de valeurs qu'il y a d'éléments affectés : la fonction répète automatiquement la liste des valeurs fournies.

Ainsi, une liste de valeurs "1 1 2" sera automatiquement répétée s'il y a 8 éléments à affecter : "1 1 2 1 1 2 1"

#### Exemples :

S1.ORDROW(1 1 1 2 2)

Modifie complètement l'ordonnateur de la variable S1 - indépendamment de sa taille.

&nbsp;

S1.ORDROW(1; -1)

Modifie la valeur de l'ordonnateur de la DERNIERE ligne de la variable S1.

&nbsp;

Voir aussi : [Propriétés des variables](<Modifierlesproprietesdesvariable.md>)