# TXTCOL

## Fonction TXTCOL

La fonction **TXTCOL** modifie le texte d'une ou plusieurs 'colonnes' (dimension 1) de la variable.

Cette méthode est utile pour modifier un texte particulier tout en laissant le moteur gérer les autres textes de manière utile.

#### Syntaxe :&nbsp;

Q01.TXTCOL(Key; Value; Delimiter)

ou

\_TXTCOL(Q01; Key; Value; Delimiter)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Key | Chaîne de caractères | Positions affectées | Obligatoire |
| &#50; | Value | Chaîne de caractères | Chaîne associée1;Chaîne associée2 | chaine;chaine2 par défaut |
| &#51; | Delimiter | Chaîne de caractères | ; | NUL par défaut |


#### Exemples :

Il est possible d'utiliser les annotations de variable pour modifier les textes des items, dans cet exemple, les libellés des items sont enrichis de l'annotation \[TITLE\] :

Q02C.TXTCOL("\*";"\[TITLE\] - #")

&nbsp;

Voir aussi :&nbsp;

[Gestion des dimensions](<Gererlesdimensionsdesvariables1.md>)

[Gestion des libellés](<Gererleslibelleslestextes1.md>)
