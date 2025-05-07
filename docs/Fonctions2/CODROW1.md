# CODROW

## Fonction CODROW

La fonction **CODROW** permet à l'appelant de modifier les codes associés aux lignes de la variable.

&nbsp;

L'argument est le vecteur des codes (exemple : 4 5 99) à inscrire dans les lignes de la variable.

#### Syntaxe :&nbsp;

Q01.CODROW(Values; sélection)

ou

\_CODROW(Q01; Values;sélection)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Values | Liste de nombres | Valeurs des codes | Obligatoire |
| &#50; | sélection | Liste de valeurs | Liste des positions affectées | NUL par défaut |


#### Remarques :

La fonction CODROW conserve toutes les autres propriétés de la variable d'origine

#### Exemples :

S1.CODROW(97 99; 11 12) affecte les codes 97 et 99 aux lignes 11 et 12.&nbsp;

&nbsp;

Voir aussi : [Propriétés des variables](<Modifierlesproprietesdesvariable.md>)