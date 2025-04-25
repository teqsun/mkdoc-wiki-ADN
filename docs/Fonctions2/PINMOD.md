# PINMOD

## Fonction PINMOD

La fonction **PINMOD** épingle (ou libère) des modalités d'une variable.

Une modalité épinglée n'est pas concernée par les tris/hiérarchies : elle reste fixée à sa place.

C'est très souvent le cas par exemple des modalités "autres", "aucuns", etc.

#### Syntaxe :&nbsp;

Q01.PINMOD(Keys; PinMe)

ou

\_PINMOD(Q01; Keys; PinMe)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Keys | Valeur | Liste des positions affectées | Obligatoire |
| &#50; | PinMe | Booléen | TRUE : épingle FALSE : libère | TRUE par défaut |


#### Exemples :

S6.PINMOD(-1)

Épingle la dernière modalité de la variable S6.

&nbsp;

Voir aussi :&nbsp;

[Gestion des dimensions](<Gererlesdimensionsdesvariables1.md>)

[Présenter les variables dans les tableaux](<Presenterlesvariablesdanslestab1.md>)
