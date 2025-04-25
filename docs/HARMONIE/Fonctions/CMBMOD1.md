# CMBMOD

## Fonction CMBMOD

La fonction **CMBMOD** combine entre elles les modalités d'une variable.&nbsp;

#### Syntaxe :&nbsp;

Q01.CMBMOD(Source; PermutationSize; Exactly; RemoveEmpty; SortResults; InsertSubTitles; InsertSubTotal)

ou

\_CMBMOD(Q01; Source; PermutationSize; Exactly; RemoveEmpty; SortResults; InsertSubTitles; InsertSubTotal)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Source | Variable | Variable multi-réponses | Obligatoire |
| &#50; | PermutationSize | Entier | Par défaut, toutes les tailles de combinaisons possibles | \-1 par défaut |
| &#51; | Exactly | Booléen | Toutes les réponses exactement si TRUE | FALSE par défaut |
| &#52; | RemoveEmpty | Booléen | Par défaut, conserve les combinaisons vides | FALSE par défaut |
| &#53; | SortResults | Booléen | Pat défaut, résultats non triés | FALSE par défaut |
| &#54; | InsertSubTitles | Booléen | Par défaut, pas de sous-titres | FALSE par défaut |
| &#55; | InsertSubTotal | Booléen | Par défaut pas de sous-totaux | FALSE par défaut |


#### Remarques :

Attention, sans argument, elle produit toutes les combinaisons possibles... Et peut donc nécessiter un temps de calcul important \!

#### Exemples :

S6.CMBMOD(2)

Retourne une variable qui contient toutes les combinaisons existantes de 2 modalités parmi les modalités de la variable S6.

&nbsp;

S6.CMBMOD(-1;TRUE;TRUE;TRUE;TRUE;FALSE)

Retourne une variable avec toutes les combinaisons exclusives, triées avec des sous-titres.

&nbsp;

Voir aussi : [Combiner les modalités de plusieurs variables](<Combinerlesmodalitesdeplusieurs1.md>)
