# COUNT

## Fonction COUNT

La fonction **COUNT** crée un filtre depuis une variable multi-réponses et un nombre de citations.&nbsp;

#### Syntaxe :&nbsp;

Q01.COUNT(Argument;Liste;Mode)

ou

\_COUNT(Q01; Argument;Liste;Mode)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Argument | Entier | Nombre de citations | Obligatoire |
| &nbsp; | Liste | Liste | Liste des modalités considérées | &nbsp; |
| &nbsp; | Mode | Booléen | Exclusivement sur la base de la sélection si TRUE | &nbsp; |


#### Exemples :

Q2.COUNT(2)

Crée un filtre sélectionnant les individus ayant cité au&nbsp; 2 réponses.

&nbsp;

Q2.COUNT(2; 1 2 3;TRUE)

Crée un filtre sélectionnant les individus ayant cité&nbsp; 2 réponses parmi les modalités 1, 2 ou 3 exclusivement.

&nbsp;

Voir aussi :&nbsp;

MINCOUNT()&nbsp;

MAXCOUNT()

&nbsp;

[Gestion des libellés](<Gererleslibelleslestextes1.md>)

[Propriétés des variables](<Modifierlesproprietesdesvariable.md>)

[Combiner les variables](<Combinerlesvariables1.md>)