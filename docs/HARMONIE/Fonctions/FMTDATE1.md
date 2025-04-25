# FMTDATE

## Fonction FMTDATE

La fonction **FMTDATE** transforme une variable temporelle en variable littérale à l'aide d'un format numérique "à la Excel".

#### Syntaxe :&nbsp;

Q01.FMTDATE(Format; NoAnswersValue)

ou

\_FMTDATE(Q01; Format; NoAnswersValue)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Format | Chaîne de caractères | Format d'affichage | "g" par défaut |
| &#50; | NoAnswersValue | Chaîne de caractères | Valeurs des sans-réponse | vide par défaut |


#### Exemples :

DATE.FTMDATE("g")

Retourne une variable littérale dont les textes sont sous la forme "10/12/1815".

&nbsp;

DATE.FTMDATE("D")

Retourne une variable littérale dont les textes sont sous la forme "dimanche 10 décembre 1815".

&nbsp;

Voir aussi : [Manipuler les variables temporelles et de durées](<Manipulerlesvariablestemporelle1.md>)
