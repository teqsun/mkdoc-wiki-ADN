# ANDFLT

## Fonction ANDFLT

La fonction ANDFLT crée un univers (un filtre) à l'aide d'un "ET LOGIQUE" en considérant les répondants de chacun des arguments (qui correspondent donc aux différentes variables et/ou constructions).

#### Syntaxe n°1 :&nbsp;

\_ANDFLT(Selection)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Selection | Sélection de variables | Expression de sélection de variables (ex: '$"S?"') ou liste de variables séparées par un ";" | Obligatoire |


#### Remarques :

Un 'ANDFLT' produit un FILTRE (une seule modalité) quelques soient les variables en arguments.

#### Exemples :

\_ANDFLT(S1.SELMOD(1 2); S3.SELMOD(2);S2)

Donne un univers constitué de l'intersection (ET logique) entre les répondants à S1 modalités 1 ou 2, les répondants à S3 modalité 2 et les répondants à S2.

&nbsp;

Voir aussi :&nbsp;

[Univers, cibles et sous-populations](<Universciblesetsous-populations.md>)

[Combiner les variables](<Combinerlesvariables1.md>)