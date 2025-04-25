# SETROW

## Fonction SETROW

La fonction **SETROW** permet de modifier partiellement une variable dimensionnée.&nbsp;

#### Syntaxe :&nbsp;

Q01.SETROW(Item; Value)

ou

\_SETROW(Variable; Item; Value)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Variable | Variable | Tous types | Obligatoire |
| &#51; | Item | Keys | liste des items à modifier | Obligatoire |
| &#52; | Value | Valeur ou variable | Réponse à affecter (numéro de modalité ou valeur numérique en fonction de la nature de la variable d'origine ou une variable)&nbsp; | Obligatoire |


&nbsp;

#### Exemples :

S1.SETROW(1 2; 10)

Les deux premiers items lignes de S1 récupèrent le valeur 10

&nbsp;

S1.SETROW(-1; Q1)

Le dernier item lignes de S1 récupère les valeurs de Q1

&nbsp;

S1.SETROW("France"; Q1)

L'item ligne "France" de S1 récupère les valeurs de Q1

&nbsp;

Voir aussi :&nbsp;

[Combiner les variables](<Combinerlesvariables1.md>)

[Variables temporaires](<VariablestemporairesTHIS1.md>)

[Réparer une variable](<FIX1.md>)
