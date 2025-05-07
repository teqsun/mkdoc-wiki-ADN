# REDMOD

## Fonction REDMOD

La fonction **REDMOD** permet à l'appelant de modifier le réducteur (valeur numérique utilisée pour quantifier une modalité) de la variable.

&nbsp;

L'argument est le vecteur des valeurs (exemple : 4.5 5.2 7.5) à inscrire dans les modalités de la variable.

#### Syntaxe :&nbsp;

Q01.REDMOD(Values; sélection)

ou

\_REDMOD(Q01; Values;sélection )

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Values | Liste de nombres | Valeurs du réducteur | Obligatoire |
| &#50; | sélection | Liste de valeurs | Liste des positions affectées | NUL par défaut |


#### Remarques :

La fonction REDMOD conserve toutes les autres propriétés de la variable d'origine

#### Exemples :

S1.REDMOD(1 2 3 4 5)

&nbsp;

Voir aussi : [Propriétés des variables](<Modifierlesproprietesdesvariable.md>)