# XOR

## Fonction XOR

La fonction **XOR** applique un "OU LOGIQUE EXCLUSIF" de modalité à modalité en suivant le principe d'harmonisation des modalités. Les arguments correspondent aux différentes variables ou constructions à combiner.

#### Syntaxe :&nbsp;

\_XOR(Selection)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Selection | Sélection de variables | Expression de sélection de variables (ex: '$"S?"') ou liste de variables séparées par un ";" | Obligatoire |


#### Remarques :

Un 'XOR' entre deux variables ne produit donc pas un univers \! Pour créer un univers, utilisez XORFLT \!

#### Exemples :

\_XOR(S1; S3)

ou

S1 XOR S3

ou

S1 \^ S3

Le résultat contient autant de modalités que nécessaire pour que les modalités soient harmonisées. Pour chaque répondant, une modalité est citée lorsqu'elle est citée dans un et un seul argument.

&nbsp;

Voir aussi :&nbsp;

[Opérateurs](<Operateurs1.md>)

[Combiner les variables](<Combinerlesvariables1.md>)