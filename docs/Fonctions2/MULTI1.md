# MULTI

## Fonction MULTI

La fonction **MULTI** crée une variable multi-réponses depuis une liste de variables.

Chaque variable en argument correspond à une forme de OUI/NON pour une modalité de réponse possible à la variable finale.

On ne retiendra qu'une valeur de réponse particulière pour chacune de ces variables.

#### Syntaxe :&nbsp;

\_MULTI(Key; Sources)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Key | Valeur | Modalité de réponse à retenir dans les variables en argument | Obligatoire |
| &#50; | Sources | Liste de variables | Liste des variables à traiter | Obligatoire |


&nbsp;

#### Exemples :

\_MULTI(2; Q01\_1; Q01\_2; Q01\_3; Q01\_4; Q01\_5; Q01\_6;)

Le résultat est une variable multi-réponses à 6 modalités en considérant la réponse 2

&nbsp;

Voir aussi :&nbsp;

[Traiter les variables multi-réponses](<Traiterlesvariablesmulti-repons1.md>)

[Combiner les variables](<Combinerlesvariables1.md>)
