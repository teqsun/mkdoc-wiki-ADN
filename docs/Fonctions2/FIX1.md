# FIX

## Fonction FIX

La fonction **FIX** "répare" une variable en modifiant les réponses de ses répondants selon un univers d'application.&nbsp;

#### Syntaxe :&nbsp;

Q01.FIX(Universe; NewValue; AppendMode)

ou

\_FIX(Variable; Universe; NewValue; AppendMode)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Variable | Variable | Tous types | Obligatoire |
| &#50; | Universe | Variable | Univers d'application (une variable ou une construction) | Obligatoire |
| &#51; | NewValue | Valeur | réponse à affecter (numéro de modalité ou valeur numérique en fonction de la nature de la variable d'origine ou une variable)&nbsp; | Obligatoire |
| &#52; | AppendMode | Booléen | Par défaut remplace, si TRUE ajoute la nouvelle valeur | FALSE par défaut |
| &#53; | Insertion text | Chaîne | Libellé de la nouvelle modalité créée précédée de @code pour lui affecter un code | Optionnel |


&nbsp;

#### Exemples :

S1.FIX(S2 \> 80; 5)

La variable obtenue est en tous points similaire à la variable S1. Mais les répondants à S2 \> 80 se voient automatiquement attribués la réponse 5 (à la S1).

&nbsp;

S1.FIX(S2 \> 80; 6;FALSE;"@99 NC")

La variable obtenue est en tous points similaire à la variable S1. Mais les répondants à S2 \> 80 se voient automatiquement attribués la réponse 6 (à la S1) qui sera libellée "NC" et dont le code associé vaut 99.

&nbsp;

S6.FIX(S2 \> 80; 5; TRUE)

La variable obtenue est en tous points similaire à la variable S6. Mais les répondants à S2 \> 80 se voient automatiquement augmentés de la réponse 5 (à la S6).

&nbsp;

S6.FIX(S2 \> 80; 5; FALSE)

La variable obtenue est en tous points similaire à la variable S6. Mais les répondants à S2 \> 80 se voient automatiquement attribués (quitte à supprimer les autres réponses citées par ces individus) la réponse 5 (à la S6).

&nbsp;

&nbsp;

Une nubilité variable \!

&nbsp;

Dans notre étude factice,

MARI représente le statut marital (la première modalité est "marié")

PAYS représente le pays d'origine (la première modalité est "France")

AGE représente l'âge en clair

SEXE représente le sexe de l'interviewé (Homme, Femme)

&nbsp;

Le problème :

&nbsp;

En France, les femmes peuvent se marier dès leur 13 ans alors que les garçons doivent attendre leur 15 ans.

Dans notre enquête factice, il se trouve qu'un garçon de 14 ans déclare être marié... sans doute une erreur de jeunesse.

Comment résoudre cet épineux problème et nettoyer la variable MARI ?

&nbsp;

Une solution :

&nbsp;

MARI.FIX(\_UNIV(PAYS 1; SEXE 1; AGE \< 15); NA)

Retourne une variable MARI "propre" dans laquelle les garçons français dont l'âge est strictement inférieur à 15 sont assignés à sans-réponse.

&nbsp;

Voir aussi :&nbsp;

[Combiner les variables](<Combinerlesvariables1.md>)

[Variables temporaires](<VariablestemporairesTHIS1.md>)

[Réparer une variable sous conditions](<IF.md>)
