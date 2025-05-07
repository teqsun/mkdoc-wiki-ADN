# FLT

## Fonction FLT

La fonction **FLT** filtre (met à "sans-réponse") les répondants de la variable en lui appliquant des conditions de validité. L'univers appliqué à la variable est celui de ceux qui ont répondu à toutes les variables et/ou constructions en arguments.

#### Syntaxe :&nbsp;

Q01.FLT(Filters)

ou

\_FLT(Q01; Filters)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Filters | Liste de variables | Univers d'application | Obligatoire |


#### Exemples :

S1.FLT(S2 \> 10; S3 1)

La variable obtenue est en tous points similaire à la variable S1. Mais ses données sont filtrées selon les répondants à S2 \> 10 ET à S3 1.

&nbsp;

Voir aussi :&nbsp;

[Univers de variables](<Universciblesetsous-populations.md>)

[Combiner les variables](<Combinerlesvariables1.md>)
