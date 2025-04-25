# CONCAT

## Fonction CONCAT

La fonction **CONCAT** crée une variable littérale dont les valeurs sont la concaténation des textes de plusieurs variables littérales.

#### Syntaxe :&nbsp;

\_CONCAT(Variables)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Variables | Liste de variables | Liste des variables (logiques ou littérales) ou des chaînes à concaténer | Obligatoire |


#### Remarques :

Fonctionne comme le \& de Excel.

#### Exemples :

\_CONCAT(S1; S1)

Crée une variable littérale dont les textes sont la concaténation des valeurs de S1 avec S1 (donc répétés dans notre cas).

&nbsp;

\_CONCAT(S1; S1; " - ")

Crée une variable littérale dont les textes sont la concaténation des valeurs de S1 avec S1 (donc répétés dans notre cas) puis le caractère " - ".

&nbsp;

Voir aussi :&nbsp;

[Traiter les variables littérales](<Traiterlesvariableslitterales.md>)

[Combiner les variables](<Combinerlesvariables1.md>)
