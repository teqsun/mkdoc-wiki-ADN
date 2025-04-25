# AS

## Fonction AS

La fonction **AS** crée une variable temporaire utilisable dans la définition courante.

&nbsp;

#### Syntaxe :&nbsp;

Q01.AS("Name")

ou

\_AS(Q01;"Name")

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Name | Chaîne de caractères | Nom de la variable temporaire | Obligatoire |


#### Remarques :

L'appel à une variable temporaire est préfixé par le caractère "@"

#### Exemples :

S2.AS("T1").FIX(@T1.NORESP() AND S1.MOD(1);99).AS("T2").FIX(@T2.NORESP() AND S1.NOT(1);-1)

Dans cet exemple, on souhaite appliquer 2 règles de nettoyage à la variable S2 sans passer par la création de variables intermédiaires.

T1 est une première copie de S2 sur laquelle une première règle de nettoyage est appliquée.

Puis T2 qui est une copie de la variable issue de ce premier nettoyage est utilisée pour l'application d'une deuxième règle de nettoyage.

&nbsp;

Voir aussi :