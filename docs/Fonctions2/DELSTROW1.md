# DELSTROW

## Fonction DELSTROW

La fonction **DELSTROW** supprime les sous-titres rencontrés dans les lignes de la variable traitée.

Deux modes de travail sont possibles : soit ils sont purement et simplement supprimés, soit ils sont répétés au niveau des lignes à l'aide d'un séparateur, tout en respectant la hiérarchie originale.

#### Syntaxe :&nbsp;

Q01.DELSTROW(Delimiter)

ou

\_DELSTROW(Q01; Delimiter)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Delimiter | Chaîne de caractères | Séparateur. | vide par défaut |


#### Exemples :

Q01.DELSTCOL()

Retourne une variable dont les sous-titres sont supprimés de la liste des colonnes.

&nbsp;

BR1.DELSTCOL(" - ")

Retourne une variable dont les sous-titres sont supprimés de la liste des colonnes, mais indiqués dans chacune des colonnes et séparés par la chaîne " - ".

&nbsp;

Voir aussi : [Gestion des libellés](<Gererleslibelleslestextes1.md>)
