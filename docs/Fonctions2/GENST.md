# GENST

## Fonction GENST

La fonction **GENST** crée des sous-titres en fonction d'un délimiteur choisi. c'est l'inverse de DELST.

#### Syntaxe :&nbsp;

Q01.GENST(Delimiter; rightAlign)

ou

\_GENST(Q01; Delimiter; rightAlign)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Delimiter | Chaîne de caractères | Séparateur oblogatoire | &nbsp; |
| &nbsp; | rightAlign | Booléen | TRUE : commence le décodage par la droite | &nbsp; |


#### &nbsp;

#### Exemples :

BR1.GENST(",")

Retourne une variable dont les sous-titres sont créés à partir des libellés des modalités.

&nbsp;

France, Homme

France, Femme

Espagne, Homme

Espagne, Femme

&nbsp;

devient

&nbsp;

France

&nbsp; &nbsp; Homme

&nbsp; &nbsp; Femme

Espagne

&nbsp; &nbsp; Homme

&nbsp; &nbsp; Femme
