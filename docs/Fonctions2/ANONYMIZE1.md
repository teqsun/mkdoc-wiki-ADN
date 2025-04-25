# ANONYMIZE

## Fonction ANONYMIZE

La fonction **ANONYMIZE** nettoie une variable en supprimant les modalités non citées par rapport à un univers donné.&nbsp;

En option, une modalité "Autres" peut être créée.

#### Syntaxe :&nbsp;

Q01.ANONYMIZE(Universe; CreateOthers)

ou

\_ANONYMIZE(Q01; Universe; CreateOthers)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Universe | Univers | Univers d'application | Obligatoire |
| &#50; | CreateOthers | Booléen | Crée la modalité "Autres" si TRUE | TRUE par défaut |


#### Exemples :

DEPARTEMENTS.ANONYMIZE(REGION 1)

Retourne une variable DEPARTEMENTS qui ne comporte que les départements de la REGION 1. Les autres départements sont regroupés dans une modalités "Autres".

&nbsp;

DEPARTEMENTS.ANONYMIZE(REGION 1; FALSE)

Retourne une variable DEPARTEMENTS qui ne comporte que les départements de la REGION 1. Les autres départements sont simplement supprimés.

&nbsp;

Voir aussi :&nbsp;

[Univers, cibles et sous-populations](<Universciblesetsous-populations.md>)

[Combiner les variables](<Combinerlesvariables1.md>)

