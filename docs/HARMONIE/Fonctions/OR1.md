# OR

## Fonction OR

(A ne pas confondre avec l'opérateur OR qui calcule une condition basée sur le OU LOGIQUE entre les répondants des arguments)

La fonction **OR** applique un "OU LOGIQUE" de modalité à modalité en suivant le principe d'harmonisation des modalités. Les arguments correspondent aux différentes variables ou constructions à combiner.

&nbsp;

IMPORTANT : un 'OR' entre deux variables ne produit donc pas un univers \! Pour créer un univers, utilisez UNIV ou ANDFLT \!

#### Syntaxe :

\_OR(Selection)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Selection | Sélection de variables | Expression de sélection de variables (ex: '$"S?"') ou liste de variables séparées par un ";" | Obligatoire |


#### Exemples :

\_OR(S1; S3)

ou

S1 OR S3

ou

S1 \| S3

&nbsp;

Le résultat contient autant de modalités que nécessaire pour que les modalités soient harmonisées. Pour chaque répondant, une modalité est citée lorsqu'elle est citée dans au moins un argument.

&nbsp;

Attention, à ne pas confondre avec l'opérateur ° (OU logique sans harmonisation des modalités)

&nbsp;

Ainsi, S1 ° S3 donne une variable avec les mêmes modalités que l'argument droit de °, ici S3.

Il est possible d'écrire : S1.SELMOD(1) ° S3, dans ce cas la modalité de l'argument gauche est appliqué aux modalités de l'argument droit.

Si l'opérateur ° est utilisé sur des variables dimensionnées, le principe d'harmonisation des modalités est toujours appliqué aux lignes/colonnes.

&nbsp;

Voir aussi :&nbsp;

[Traiter les variables logiques (modalités)](<Traiterlesvariableslogiquesmoda1.md>)

[Combiner les variables](<Combinerlesvariables1.md>)
