# SELROW

## Fonction SELROW ou ROW

La fonction **SELROW** sélectionne (ou regroupe) des lignes de la variable traitée.

Voir [SELMOD](<SELMOD.md>).

#### Syntaxe :&nbsp;

Q01.SELROW(Part1; Part2; Part3; ...)

ou

Q01.ROW(Part1; Part2; Part3; ...)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Parts | Liste d'expressions | Expressions de sélection/regroupement séparés par des ';' | Obligatoire |


&nbsp;

Il est possible d'utiliser les accolades pour extraire un item : **Q1{2}** est équivalent à **Q1.COL(1).TRIMDIM()**

&nbsp;

Voir aussi : [Gestion des dimensions](<Gererlesdimensionsdesvariables1.md>)
