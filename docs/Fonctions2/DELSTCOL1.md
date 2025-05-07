# DELSTCOL

## Fonction DELSTCOL

La fonction **DELSTCOL** supprime les sous-titres rencontrés dans les colonnes de la variable traitée.

Deux modes de travail sont possibles : soit ils sont purement et simplement supprimés, soit ils sont répétés au niveau des colonnes à l'aide d'un séparateur, tout en respectant la hiérarchie originale.

#### Syntaxe :&nbsp;

Q01.DELSTCOL(Delimiter)

ou

\_DELSTCOL(Q01; Delimiter)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Delimiter | Chaîne de caractères | Séparateur&nbsp; optionnel | vide par défaut |


#### Exemples :

Q01.DELSTCOL()

Retourne une variable dont les sous-titres sont supprimés de la liste des colonnes.

&nbsp;

BR1.DELSTCOL(" - ")

Retourne une variable dont les sous-titres sont supprimés de la liste des colonnes, mais indiqués dans chacune des colonnes et séparés par la chaîne " - ".

&nbsp;

Voir aussi : [Gestion des libellés](<Gererleslibelleslestextes1.md>)