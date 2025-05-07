# SELCOL

## Fonction SELCOL ou COL

La fonction **SELCOL** sélectionne (ou regroupe) des colonnes de la variable traitée.

Voir [SELMOD](<SELMOD.md>).

#### Syntaxe :&nbsp;

Q01.SELCOL(Part1; Part2; Part3; ...;Reducer)

ou

Q01.COL(Part1; Part2; Part3; ...)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Parts | Liste d'expressions | Expressions de sélection/regroupement séparés par des ';' | Obligatoire |
| &nbsp; | Reducer | Operateur&nbsp; | [Opérateur de réduction](<Reductions1.md>) | Optionnel |


&nbsp;

#### Exemples :

Q1.COL(1 2 3;SUMNA(1 2 3))&nbsp;

Retourne une variable dimensionnée à 3 colonnes plus une dernière étant la somme des 3 autres sans tenir compte des sans-réponse (SUMNA).&nbsp;

&nbsp;

Il est possible d'utiliser les accolades pour extraire un item : **Q1{2}** est équivalent à**Q1.COL(1).TRIMDIM()**

&nbsp;

Voir aussi :

[Gestion des dimensions,](<Gererlesdimensionsdesvariables1.md>)

&nbsp;
