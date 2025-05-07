# UNIV

## Fonction UNIV

La fonction **UNIV** créer un filtre en appliquant un "ET LOGIQUE" aux répondants de chacun des arguments (qui correspondent donc aux différentes variables et/ou constructions).

#### Syntaxe :&nbsp;

\_UNIV(Selection)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Selection | Sélection de variables | Expression de sélection de variables (ex: '$"S?"') ou liste de variables séparées par un ";" | Obligatoire |


#### Remarques :

IMPORTANT : un 'UNIV' produit un FILTRE (une seule modalité) quelles que soient les variables en argument.

#### Exemples :

\_UNIV(S1; S3)

Le résultat contient une modalité. Un répondant est à "VRAI" lorsque c'est un répondant à tous les arguments.

&nbsp;

Voir aussi : [Univers de variables](<Universciblesetsous-populations.md>)