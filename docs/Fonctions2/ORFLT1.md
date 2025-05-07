# ORFLT

## Fonction ORFLT

La fonction **ORFLT** créer un filtre à l'aide d'un "OU LOGIQUE" en considérant les répondants de chacun des arguments (qui correspondent donc aux différentes variables et/ou constructions).

#### Syntaxe&nbsp; :&nbsp;

\_ORFLT(Q01; Selection)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Selection | Sélection de variables | Expression de sélection de variables (ex: '$"S?"') ou liste de variables séparées par un ";" | Obligatoire |


#### Remarques :

'ORFLT' produit un FILTRE (une seule modalité) quelques soient les variables en arguments.

#### Exemples :

\_ORFLT(S1.SELMOD(1 2); S3)

Le résultat contient une modalité. Un répondant est à "VRAI" lorsque c'est un répondant à au moins l'un des arguments.

&nbsp;

Voir aussi :&nbsp;

[Univers de variables](<Universciblesetsous-populations.md>)

[Combiner les variables](<Combinerlesvariables1.md>)