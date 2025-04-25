# RADICAL

## Fonction RADICAL

La fonction **RADICAL** appliquée à une variable numérique permet de lui associer un radical qui sera utilisé comme "unité" lors de la créations de modalités automatiques par la fonction CTOD.

#### Syntaxe :&nbsp;

Q1.RADICAL(Label)

ou

\_RADICAL(Q1;Label)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Label | chaîne de caractères | texte du radical&nbsp; | Obligatoire |


#### Remarques :

Le radical n'est utilisé que par la fonction CTOD.

#### Exemples :

\_RADICAL(S2;" y/o").CTOD(4)

ou

S2.RADICAL(" y/o").CTOD(4)

&nbsp;

&nbsp;

Voir aussi : [Traiter les variables logiques (modalités)](<Traiterlesvariableslogiquesmoda1.md>)
