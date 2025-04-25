# NEWLEV

## Fonction NEWLEV

La fonction **NEWLEV** crée un nouveau niveau logique sur la base d'une variable existante.

#### Syntaxe :&nbsp;

QACHATS.NEWLEV("N\_ACHATS")

ou

\_NEWLEV(Q01; "N\_ACHATS")

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Nom du niveau | Nom | Le nom du niveau à créer mettre à jour | Obligatoire |
| &nbsp; | Titre du niveau | Chaîne | Le titre du niveau, optionnel | Optionnel |


#### Exemples :

QACHATS.NEWLEV("N\_ACHATS")

En estimant que la variable QACHATS est dimensionnée selon le nombre d'achats, la fonction NEWLEV crée le niveau "N\_ACHATS" qui comptabilisera (nb d'enregistrements) l'ensemble des achats réalisés sur l'ensemble des items en colonnes.&nbsp;

&nbsp;

Voir aussi :&nbsp;

[Niveaux](<Niveaux1.md>)

