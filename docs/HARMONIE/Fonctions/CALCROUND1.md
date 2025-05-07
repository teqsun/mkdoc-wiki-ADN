# CALCROUND

## Fonction CALCROUND

La fonction **CALCROUND** crée une variable numérique correspondant à la valeur arrondie de la variable numérique placée en argument avec le nombre de décimales en paramètre.

#### Syntaxe :&nbsp;

Q01.CALCROUND(Decimals)

ou

\_CALCROUND(Q01; Decimals)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Decimals | Entier | Nombre de décimales conservées, 0 par défaut | &#48; par défaut |


#### Exemples :

IMC.CALCROUND()

Crée une nouvelle variable correspondant à la valeur arrondie à 0 décimale de la variable numérique IMC.

&nbsp;

IMC.CALCROUND(4)

Crée une nouvelle variable correspondant à la valeur arrondie à 4 décimales de la variable numérique IMC.

&nbsp;

#### Remarque :

La fonction CALCROUND() suit la logique d'Excel (AwayFromZero).

&nbsp;

Voir aussi : [Manipuler les variables numériques](<Manipulerlesvariablesnumeriques1.md>)