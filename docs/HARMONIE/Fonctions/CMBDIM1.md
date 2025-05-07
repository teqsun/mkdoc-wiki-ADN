# CMBDIM

## Fonction CMBDIM

La fonction **CMBDIM** (qui correspond à l'opérateur \*\*) implémente le croisement sur dimensions.

Elle a pour effet de positionner les dimensions de la seconde variable en colonnes du résultat. Pour tout le reste, la variable obtenue est comparable au premier argument.

#### Syntaxe :&nbsp;

Q01.CMBDIM(Variables)

ou

\_CMBDIM(Q01; Variables)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Variables | Liste de variables | Liste des variables logiques à combiner | Obligatoire |


#### Remarques :

Cette fonction permet d'ajouter une dimension de croisement dans les tableaux (car les bases sont préservées pour chaque détail de la variable obtenue).&nbsp;

#### Exemples :

S1 \*\* S3

ou

S1.CMBDIM(S3)

ou

\_CMBDIM(S1; S3)

Ces trois écritures aboutissent au même résultat : la variable S1 est "répétée" pour chaque modalités de la variable S3. Les modalités de la variable S3 deviennent les "détails" du résultat.

&nbsp;

Voir aussi :&nbsp;

[Combiner les modalités de plusieurs variables](<Combinerlesmodalitesdeplusieurs1.md>)

[Combinaisons](<Combinerlesvariables1.md>)