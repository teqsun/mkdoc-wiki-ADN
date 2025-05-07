# FLTCOL

## Fonction FLTCOL

La fonction **FLTCOL** filtre (met à "sans-réponse") les répondants de la variable puis crée un détail en colonne qui correspond au titre du filtre appliqué. L'univers appliqué à la variable est celui de ceux qui ont répondu à toutes les variables et/ou constructions en arguments.

#### Syntaxe :&nbsp;

Q01.FLTCOL(Filter; Title)

ou

\_FLTCOL(Q01; Filters; Title)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Filter | Définition | Définition du filtre à appliquer aux données de la variable | Obligatoire |
| &nbsp; | Title | Chaîne | Titre à intégrer en colonne de la variable résultat | Optionnel |


#### Exemples :

S1.FLTCOL(S2 \> 50; "Plus de 50 ans")

La variable obtenue est dimensionnée avec 1 colonne et similaire à la variable S1. Mais ses données sont filtrées selon les répondants à S2 \> 50.

&nbsp;
