# CRIT

## Fonction CRIT

La fonction **CRIT** concatène les répondants des variables en arguments en appliquant les univers associés.

Elle permet de créer un critère dont chaque modalité est une définition potentiellement complexe.

La variable qui en résulte possède une modalité par variable en argument.

#### Syntaxe :&nbsp;

Q01.CRIT(Variables)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Variables | Liste de variables | Liste de définitions à traiter | Obligatoire |


#### Exemples :

\_CRIT(S1.MOD(1 2); S3.MOD(2 3 4); S2 \> 30)

Crée une variable logique constituée de 3 modalités :

1. Les répondants à S1.MOD(1)
1. Les répondants à S3.MOD(2 3 4)
1. Les répondants à S2 \> 30

&nbsp;

#### Remarques :

La variable créée n'a pas d'univers.

&nbsp;

Voir aussi : [Critères](<Creerdescriteresoubannieres1.md>)