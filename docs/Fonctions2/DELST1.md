# DELST

## Fonction DELST

La fonction **DELST** supprime les sous-titres rencontrés dans les modalités de la variable traitée.

Deux modes de travail sont possibles : soit ils sont purement et simplement supprimés, soit ils sont répétés au niveau des modalités à l'aide d'un séparateur, tout en respectant la hiérarchie originale.

#### Syntaxe :&nbsp;

Q01.DELST(Delimiter)

ou

\_DELST(Q01; Delimiter)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Delimiter | Chaîne de caractères | Séparateur optionnel | vide par défaut |


#### Remarques :

Les fonctions DELSTCOL et DELSTROW fonctionnent exactement sur le même mode, mais la première s'applique à la dimension "colonnes" et la seconde à la dimension "lignes" de la variable source.

#### Exemples :

BR1.DELST()

Retourne une variable dont les sous-titres sont supprimés de la liste des modalités.

&nbsp;

BR1.DELST(" - ")

Retourne une variable dont les sous-titres sont supprimés de la liste des modalités, mais indiqués dans chacune des modalités et séparés par la chaîne " - ".

&nbsp;

Voir aussi : [Gestion des libellés](<Gererleslibelleslestextes1.md>)
