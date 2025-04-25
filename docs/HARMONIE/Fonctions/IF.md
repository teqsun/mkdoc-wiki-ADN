# IF

## Fonction IF

La fonction **IF** permet de reconstruire en fonction d'une condition.&nbsp;

#### Syntaxe :&nbsp;

Q01.IF(Universe; ValueIfTrue; Value IfFalse)

ou

\_IF(Variable; Universe; ValueIfTrue; Value IfFalse)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Variable | Variable | Tous types | Obligatoire |
| &#50; | Universe | Variable | Univers d'application (une variable ou une construction) | Obligatoire |
| &#51; | ValueIfTrue | Valeur ou variable | Réponse à affecter (numéro de modalité ou valeur numérique en fonction de la nature de la variable d'origine ou une variable)&nbsp; | Obligatoire |
| &#52; | ValueIfFalse | Valeur ou variable | Réponse à affecter (numéro de modalité ou valeur numérique en fonction de la nature de la variable d'origine ou une variable)&nbsp; | Obligatoire |


&nbsp;

#### Exemples :

S1.IF(S2 \> 80; 1; 2)

Les répondants à S2 \> 80 se voient&nbsp; attribués la réponse 1 et les autres la réponse 2.

&nbsp;

S6.FIX(F1; Q1; Q2)

Les répondants à F1 se voient attribués la valeur de Q1 et les autres la valeurs de Q2

&nbsp;

&nbsp;

Voir aussi :&nbsp;

[Combiner les variables](<Combinerlesvariables1.md>)

[Variables temporaires](<VariablestemporairesTHIS1.md>)

[Réparer une variable](<FIX1.md>)
