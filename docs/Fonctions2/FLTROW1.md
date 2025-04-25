# FLTROW

## Fonction FLTROW

La fonction **FLTROW** filtre (met à "sans-réponse") les répondants de la variable puis crée un détail en ligne qui correspond au titre du filtre appliqué. L'univers appliqué à la variable est celui de ceux qui ont répondu à toutes les variables et/ou constructions en arguments.

#### Syntaxe :&nbsp;

Q01.FLTROW(Filter; Title)

ou

\_FLTROW(Q01; Filters; Title)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Filter | Définition | Définition du filtre à appliquer aux données de la variable | Obligatoire |
| &nbsp; | Title | Chaîne | Titre à intégrer en ligne de la variable résultat | Optionnel |


#### Exemples :

S1.FLTROW(S2 \> 50; "Plus de 50 ans")

#### Remarques :

Une variable ayant une dimension ligne a obligatoirement une dimension colonne.

Autrement dit, seule une variable doublement dimensionnée a des lignes et des colonnes. Une variable simplement dimensionnée n'a jamais de lignes.&nbsp;

