# MAXCOUNT

## Fonction MAXCOUNT

La fonction MAX**COUNT** crée un filtre depuis une variable multi-réponses et un nombre maximum de citations.&nbsp;

#### Syntaxe :&nbsp;

Q01.MAXCOUNT(Argument;Liste;Mode)

ou

\_MAXCOUNT(Q01; Argument;Liste;Mode)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Argument | Entier | Nombre maximum de citations | Obligatoire |
| &nbsp; | Liste | Liste | Liste des modalités considérées | &nbsp; |
| &nbsp; | Mode | Booléen | Exclusivement sur la base de la sélection si TRUE | &nbsp; |


#### Exemples :

Q2.MAXCOUNT(2)

Crée un filtre sélectionnant les individus ayant cité au maximum 2 réponses.

&nbsp;

Q2.MINCOUNT(2; 1 2 3;TRUE)

Crée un filtre sélectionnant les individus ayant cité au maximum 2 réponses parmi les modalités 1, 2 ou 3 exclusivement.

&nbsp;

Voir aussi :&nbsp;

COUNT()&nbsp;

MINCOUNT()

&nbsp;

[Gestion des libellés](<Gererleslibelleslestextes1.md>)

[Propriétés des variables](<Modifierlesproprietesdesvariable.md>)

[Combiner les variables](<Combinerlesvariables1.md>)