# JUXVAR

## Fonction JUXVAR

La fonction **JUXVAR** juxtapose les modalités des variables en argument.&nbsp;

Si la première variable a 3 modalités et la seconde en a 2, alors la variables résultante possède 5 modalités.&nbsp;

La base de la variable obtenue est celle des répondants à au moins une des variables en argument.

&nbsp;

La fonction JUXVAR est équivalente à l'opérateur de juxtaposition "," (la virgule).

#### Syntaxe :&nbsp;

\_JUXVAR(Selection)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Selection | Sélection de variables | Expression de sélection de variables (ex: '$"S?"') ou liste de variables séparées par un ";" | Obligatoire |


#### Exemples :

\_JUXVAR(S1; S3)

\[ou S1, S3\]

La variable résultante liste les modalités de S1 puis les modalités de S3.

Base : répondants à S1 ou S3.

&nbsp;

\_JUXVAR(S1; S3; S4)

\[ou S1, S3, S4\]

La variable résultante liste les modalités de S1 puis celles de S3 puis celles de S4.

Base : répondants à S1, S3 ou S4.

#### Remarques :

Il est possible de juxtaposer des variables logiques avec des variables numériques :&nbsp;

\_JUXVAR(S1; S1Q.TITLE("Nombre de réponses citées"))

En cas de contrôle du calcul affiché, la fonction TOMOD est plus adaptée.

L'utilisation de cette fonction avec des variables continues est équivalente à JUXCOL() et crée donc des détails (lignes et/ou colonnes)

&nbsp;

Voir aussi :&nbsp;

[Traiter les variables logiques (modalités)](<Traiterlesvariableslogiquesmoda1.md>)

[Présenter les variables dans les tableaux](<Presenterlesvariablesdanslestab1.md>)

[Critères](<Creerdescriteresoubannieres1.md>)

[Combiner les variables](<Combinerlesvariables1.md>)
