# DEPTH

## Fonction DEPTH

La fonction **DEPTH** permet de sélectionner des modalités depuis un niveau hiérarchique. Par exemple, si une variable VAGUE est présentée selon 3 niveaux : Années, Trimestres, Mois (avec des sous-totaux), alors ilo est facile d'en déduire une variable qui ne porte que sur les années ou les trimestres.

#### Syntaxe :&nbsp;

Q01.DEPTH(Value)

ou

\_DELSTROW(Q01; Delimiter)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Value | Entier | Niveau hiérarchique de référence pour l'extraction des modalités | Obligatoire |


#### Exemples :

S1.DEPTH(2)

Elimine les modalité dont la profondeur est supérieure à 2.
