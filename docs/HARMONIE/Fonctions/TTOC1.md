# TTOC

## Fonction TTOC

La fonction **TTOC** traduit une variable littérale en variable numérique. Il est possible d'indiquer une valeur par défaut pour les valeurs qui ne correspondent pas à un format numérique.

#### Syntaxe :&nbsp;

Q01.TTOC(DefaultValue)

ou

\_TTOC(Q01; DefaultValue)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | DefaultValue | Nombre | Valeur des sans-réponse | Obligatoire |


#### Exemples :

VALUES.TTOC(99)

Retourne une variable numérique dont les valeurs sont la traduction des textes rencontrés dans la variable VALUES. La valeur par défaut est 99.

&nbsp;

Voir aussi : [Traiter les variables littérales](<Traiterlesvariableslitterales.md>)

