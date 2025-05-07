# CMBVAR

## Fonction CMBVAR

La fonction **CMBVAR** combine (croise) les modalités des variables en arguments.&nbsp;

Il suffit de lister les différentes variables (ou constructions) à croiser en guise d'arguments pour produire une variable avec des modalités combinées.

#### Syntaxe :&nbsp;

Q01.CMBVAR(Variables)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Variables | Liste de variables | Liste de variables à combiner ou une expression de sélection de variables (ex: '$"S?"') | Obligatoire |


#### Remarques :

La fonction CMBDEL, très proche de la variable CMBVAR, supprime les cas non rencontrés (les modalités vides) du résultat. De fait, elle est idéale pour par exemple croiser la variable REGION par la variable DEPARTEMENT : seuls les départements des régions apparaîtront (alors que CMBVAR listerait tous les départements pour chacune des régions \!).

#### Exemples :

\_CMBVAR(S1; S3; S4)

ou&nbsp;

S1.CMBVAR( S3; S4)

La variable résultante dispose en modalités le croisement des modalités des trois variables en arguments.

&nbsp;

Si la variable SEXE désigne les hommes et les femmes et la variable AGE désigne les tranches d'âge, alors le croisement de ces deux variables donnera le détail des tranches d'âge pour les hommes puis pour les femmes.

&nbsp;

Voir aussi :&nbsp;

[Combiner les modalités de plusieurs variables](<Combinerlesmodalitesdeplusieurs1.md>)

[Combinaisons](<Combinerlesvariables1.md>)