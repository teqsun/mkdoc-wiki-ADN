# TXTMOD

## Fonction TXTMOD

La fonction **TXTMOD** modifie le texte d'une ou plusieurs modalités de la variable.&nbsp;

Cette méthode est utile pour modifier un texte particulier tout en laissant le moteur gérer les autres textes de manière utile.

La fonction TXTCOL modifie un item colonne et la fonction TXTROW modifie un item ligne.

#### Syntaxe :&nbsp;

Q01.TXTMOD(Key; Value; Delimiter)

ou

\_TXTMOD(Q01; Key; Value; Delimiter)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Key | Chaîne de caractères | Positions affectées | Obligatoire |
| &#50; | Value | Chaîne de caractères | Chaîne associée1;Chaîne associée2 | chaine;chaine2 par défaut |
| &#51; | Delimiter | Chaîne de caractères | séparateur de libellés | NUL par défaut |


#### Exemples :

S1.TXTMOD(1; "Répondants")

Retourne une variable logique dont la 1ère modalité a pour texte "Répondants".

&nbsp;

TAILLE.CTOD(3).TXTMOD(1; "Petit/Moyen/Grand"; "/")

Retourne une variable logique à 3 modalités avec les libellés respectivement Petit, Moyen et Grand.

&nbsp;

Q1.TXTMOD("\*"; "\[CODE\]")

Remplace les libellés de toutes les modalités par leur code respectif.

&nbsp;

On peut aussi utiliser \[NAME\], \[TITLE\], \[TITLE:S\], \[FILTER\], \[COMMENT\]...

&nbsp;

Voir aussi :&nbsp;

[Traiter les variables logiques (modalités)](<Traiterlesvariableslogiquesmoda1.md>)

[Gestion des libellés](<Gererleslibelleslestextes1.md>)

