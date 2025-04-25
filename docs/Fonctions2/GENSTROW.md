# GENSTROW

## Fonction GENSTROW

La fonction **GENSTROW** crée des sous-titres en fonction d'un délimiteur choisi. c'est l'inverse de DELSTROW.

#### Syntaxe :&nbsp;

Q01.GENSTROW(Delimiter; rightAlign)

ou

\_GENSTROW(Q01; Delimiter; rightAlign)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Delimiter | Chaîne de caractères | Séparateur oblogatoire | &nbsp; |
| &nbsp; | rightAlign | Booléen | TRUE : commence le décodage par la droite | &nbsp; |


#### &nbsp;

#### Exemples :

BR1.GENSTROW(",")

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

