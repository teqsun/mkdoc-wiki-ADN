# PINROW

## Fonction PINROW

La fonction **PINROW** modifie le comportement de certains items de la dimension ligne d'une variable lors des hiérarchisations.

Une modalité épinglée n'est pas concernée par les tris/hiérarchies : elle reste fixée à sa place.

C'est très souvent le cas par exemple des items "autres", "aucun", etc.

#### Syntaxe :&nbsp;

Q01.PINROW(Keys; PinMe)

ou

\_PINROW(Q01; Keys; PinMe)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Keys | Valeur | Liste des positions affectées | Obligatoire |
| &#50; | PinMe | Booléen | TRUE : épingle FALSE : libère | TRUE par défaut |


#### Exemples :

S6.PINROW(-1)

Épingle le dernier item de la dimension ligne de la variable S6.

&nbsp;

Voir aussi :&nbsp;

[Gestion des dimensions](<Gererlesdimensionsdesvariables1.md>)

[Présenter les variables dans les tableaux](<Presenterlesvariablesdanslestab1.md>)