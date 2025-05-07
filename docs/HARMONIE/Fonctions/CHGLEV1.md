# CHGLEV

## Fonction CHGLEV

La fonction **CHGLEV** change la variable de niveau de réponse (foyer vers individus et vice versa).&nbsp;

La variable obtenue est donc sur le niveau spécifié en premier argument. L'opérateur de réduction appliqué lors du changement de niveau peut être indiqué dans le deuxième argument : consultez la [table des opérateurs de réduction.](<Reductions1.md>)

#### Syntaxe :&nbsp;

Q01.CHGLEV(NewLevel; Aggregator)

ou

\_CHGLEV(Q01; NewLevel; Aggregator)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | NewLevel | Chaîne de caractères | Nom du niveau cible | Obligatoire |
| &#50; | Aggregator | Chaîne de caractères | Par défaut, OU pour les logiques, SUM pour les quantités | NUL par défaut |


#### Exemples :

S2.CHGLEV("UNITS")

Crée une variable basée sur le niveau "UNITS".

&nbsp;

Voir aussi :&nbsp;

[Niveaux](<Niveaux1.md>)

[Les opérateurs de réductions](<Reductions1.md>)