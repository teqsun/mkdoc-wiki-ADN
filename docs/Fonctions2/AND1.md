# AND

## Fonction AND

A ne pas confondre avec l'opérateur AND qui calcule une condition basée sur le ET LOGIQUE entre les répondants des arguments.

La fonction **AND** applique un "ET LOGIQUE" de modalité à modalité en ne suivant pas le principe d'harmonisation des modalités. Les arguments correspondent aux différentes variables ou constructions logiques à combiner.

#### Syntaxe :&nbsp;

\_AND(Selection)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Selection | Sélection de variables | Expression de sélection de variables (ex: '$"S?"') ou liste de variables séparées par un ";" | Obligatoire |


#### Remarques :

Le nombre de modalités des variables en argument doit être compatible.

La première variable sélectionnée et celle avec le nombre de modalité le plus grand.

#### Exemples :

\_AND(S1A;S1B)

Le résultat est une variable logique avec les mêmes modalités (en nombre et en libellés) que la première variable sélectionnée.

Les variables présentant moins de modalités que la première sont complétées avec des modalités vides.

Pour chaque répondant, une modalité est citée lorsqu'elle est citée dans tous les arguments.

IMPORTANT : un 'AND' entre deux variables ne produit donc pas un univers \! Pour créer un univers, utilisez UNIV ou ANDFLT \!

&nbsp;

&nbsp;

Voir aussi :&nbsp;

[Opérateurs](<Operateurs1.md>)

[Combiner les variables](<Combinerlesvariables1.md>)