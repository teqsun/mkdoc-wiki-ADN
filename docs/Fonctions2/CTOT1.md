# CTOT

## Fonction CTOT

La fonction **CTOT** transforme une variable numérique en variable littérale à l'aide d'un format numérique "à la Excel".

#### Syntaxe :&nbsp;

Q01.CTOT(Format; NoAnswersValue)

ou

\_CTOT(Q01; Format; NoAnswersValue)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Format | Chaîne de caractères | Format numérique à utiliser | vide par défaut |
| &#50; | NoAnswersValue | Chaîne de caractères | Texte associé aux sans-réponse | vide par défaut |


#### Exemples :

S2.CTOT("000")

Retourne une variable littérale dont le texte est l'âge formaté sur 3 positions complétées par des 0.

&nbsp;

DELTA.CTOT('+00;-00;"="')

Retourne une variable littérale dont les textes sont le delta formaté sur 2 positions complétées par des 0, signées avec la valeur nulle remplacée par le signe "=".

&nbsp;

S2.CTOT('0" ans"'; "-")

Retourne une variable littérale dont les textes sont formés par l'âge formaté suivi de la chaîne de caractères " ans". Les sans-réponse reçoivent la chaîne "-"

&nbsp;

#### Remarque :

Il est toujours possible d'utiliser la fonction [NATOVAL](<NA2VAL1.md>) pour contôler le comportement des sans-réponses.

#### &nbsp;

&nbsp;

Voir aussi : [Manipuler les variables numériques](<Manipulerlesvariablesnumeriques1.md>)
