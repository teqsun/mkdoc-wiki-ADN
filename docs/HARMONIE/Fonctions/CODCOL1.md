# CODCOL

## Fonction CODCOL

La fonction **CODCOL** permet à l'appelant de modifier les codes associés aux colonnes de la variable.

&nbsp;

L'argument est le vecteur des codes (exemple : 4 5 99) à inscrire dans les codes de la variable.

#### Syntaxe :&nbsp;

Q01.CODCOL(Values; sélection)

ou

\_CODCOL(Q01; Values;sélection )

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Values | Liste de nombres | Valeurs des codes | Obligatoire |
| &#50; | sélection | Liste de valeurs | Liste des positions affectées | NUL par défaut |


#### Remarques :

La fonction CODCOL conserve toutes les autres propriétés de la variable d'origine

#### Exemples :

S1.CODCOL(97 99; 11 12) affecte les codes 97 et 99 aux colonnes 11 et 12.&nbsp;

&nbsp;

Voir aussi : [Propriétés des variables](<Modifierlesproprietesdesvariable.md>)