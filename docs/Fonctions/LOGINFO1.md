# LOGINFO

## Fonction LOGINFO

La fonction **LOGINFO** permet d'afficher un message dans le journal à l'occasion d'une recodification.&nbsp;

#### Syntaxe :&nbsp;

\_LOGINFO(variable;texte)

ou

variable.LOGINFO(texte)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | texte | chaîne de caractères | Message affiché dans le journal. Usage des annotations possible. | Obligatoire |


#### Exemples :

Q1.TITLE("Nouveau titre").LOGINFO("Mise à jour du titre de Q1")

Le message "Mise à jour du titre de Q1" apparaît dans le journal.

Avec l'utilisation des annotations \[TITLE\] et \[NAME\], il est possible d'écrire :

Q1.LOGINFO("le titre de \[NAME\] est \[TITLE\]")

cela affiche dans le journal : "le titre de **Q1** est **Q1. Age de l'interrogé**"

&nbsp;

#### Remarques :

Les annotations disponibles sont :

\[NAME\] : nom de la variable

\[TITLE\] : titre de la variable

\[TITLE:S\] : titre court de la variable

\[COMMENT\] : commentaire de la variable

\[UNIVERSE\] : univers de la variable

\[WEIGHT\] : poids de la variable

\[DEFINITION\] : définition de la variable&nbsp;

&nbsp;

Voir aussi :&nbsp;

[Traiter les variables logiques (modalités)](<Traiterlesvariableslogiquesmoda1.md>)

[Présenter les variables dans les tableaux](<Presenterlesvariablesdanslestab1.md>)

[Critères](<Creerdescriteresoubannieres1.md>)

[Combiner les variables](<Combinerlesvariables1.md>)
