# FMTDURATION

## Fonction FMTDURATION

La fonction **FMTDURATION** transforme une variable de durée en variable littérale à l'aide d'un format numérique "à la Excel".

#### Syntaxe :&nbsp;

Q01.FMTDURATION(Format; NoAnswersValue)

ou

\_FMTDURATION(Q01; Format; NoAnswersValue)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Format | Chaîne de caractères | Format d'affichage | "g" par défaut |
| &#50; | NoAnswersValue | Chaîne de caractères | Valeurs des sans-réponse | NUL par défaut |


#### Exemples :

DURATION.FTMDURATION("D")

Retourne une variable littérale dont les textes représentent les durées en clair.

&nbsp;

Voir aussi : [Manipuler les variables temporelles et de durées](<Manipulerlesvariablestemporelle1.md>)