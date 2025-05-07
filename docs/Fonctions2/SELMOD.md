# SELMOD

## Fonction SELMOD ou MOD

La fonction **SELMOD** permet de sélectionner les modalités d'une variable. La base de la variable obtenue est celle des répondants aux modalités restantes.

Il est aussi possible d'utiliser SELMOD sur une variable continue, on procède par sélection des réponses (codes).

&nbsp;

Les arguments correspondent aux listes de modalités à supprimer. Chaque liste suit la syntaxe relative aux sélections d'items et/ou à la sélection étendue de modalités/détails.

&nbsp;

Les fonctions SELCOL et SELROW fonctionnent exactement sur le même mode, mais la première s'applique à la dimension "colonnes" et la seconde à la dimension "lignes" de la variable source.

#### Syntaxe :&nbsp;

Q01.SELMOD(Keys)

Q01.MOD(Keys)

ou

\_SELMOD(Q01; Keys)

\_MOD(Q01; Keys)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Keys | Liste de valeurs | Liste des positions sélectionnées | Obligatoire |


#### Remarques :

GRPMOD et SELMOD sont très proches \! En réalité, la seule différence vient du comportement par défaut lorsqu'un argument correspond à une liste d'items : GRPMOD crée un sous-total et SELMOD en liste le détail.

Dans le cas d"une variable logique, 0 crée une modalité vide alors que dans le cas d'une variable continue, 0 sélectionne bien le code 0.

&nbsp;

Il est possible d'utiliser les crochets pour extraire une modalité : Q1\[1\] est équivalent à Q1.MOD(1)

#### Exemples :

S1.SELMOD(1 TO 3 -1)

Crée une nouvelle variable dont les modalités sont :

\- la première modalité de S1

\- la deuxième modalité de S1&nbsp;

\- la troisième modalité de S1&nbsp;

\- la dernière de S1.

&nbsp;

S2.SELMOD(20 TO 25) crée une variable logique à 6 modalités constituées à partir des réponses 20 à 25.

S2.SELMOD(20 TO 25).RESP() crée un filtre considérant les individus ayant entre 20 et 25 ans.

&nbsp;

Utilisations habituelles :

&nbsp;

\- Créer un filtre : S6.SELMOD(1) les possesseurs de réfrigérateurs

\- Extraire des modalités : S6.SELMOD(2 3 4 5 6 12) les équipements multimédia - que l'on peut aussi écrire S6.SELMOD(2 TO 6 12)&nbsp;

\- Extraire et réordonner : S6.SELMOD( 6 5 4 3 2 12) que l'on peut aussi écrire S6.SELMOD(6 TO 2 12)

&nbsp;

Autres utilisations :

&nbsp;

\- Extraire en partant de la fin :

S6.SELMOD(-1) : extrait la dernière modalité, VTT

S6.SELMOD(-2 -1) : extrait les deux dernières modalités

&nbsp;

\- Extraire des modalités en se basant sur le libellé, les moyens de déplacement :

S6.SELMOD("VOITURE";"vtt")ou S6.SELMOD("VOITURE,vtt") insensible à la casse

On peut mixer les deux modes de sélection : S6.SELMOD(10;"vtt")

Pour sélectionner un libellé comprenant une virgule comme par exemple "Aucun, rien" : Q1.SELMOD("Aucun? rien")

S6.SELMOD("ST \*") sélectionne toutes les modalités dont le libellé commence par "ST "

\- Les utilisations moins fréquentes mais très pratiques :

Créer une nouvelle modalité vide : S6.SELMOD(1 2 0)

Dupliquer des modalités : S6.SELMOD(1 1 2 2)

&nbsp;

&nbsp;

La modalité "Aucun" est conservée si l'option de suppression des modalités vides est activée : S1.SELMOD("Aucun".FILTER(FALSE))&nbsp;

&nbsp;

\- Et les autres :

S6.SELMOD(1 $O) : 2 modalités, les Frigo et les autres

S6.SELMOD(1 $R) : 2 modalités, les Frigo et les répondants

S6.SELMOD(1 $N) : 2 modalités, les Frigo et les SR

S6.SELMOD(1 $I) : 2 modalités, les Frigo et les interrogés

S6.SELMOD(1;\!1) : 2 modalités, les Frigo et les Pas Frigo

S6.SELMOD($R $M) : 14 modalités, les répondants et toutes les modalités

S2.SELMOD($L;"Autres") déplace la modalité "Autres" en dernière position.

## S2.SELMOD(1; ~1) extrait la modalité 1 et son complément..&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

Voir aussi :&nbsp;

[Traiter les variables logiques (modalités)](<Traiterlesvariableslogiquesmoda1.md>)

Combinaisons

[Gestion des dimensions](<Gererlesdimensionsdesvariables1.md>)

Pour des combinaisons plus complexes de modalités : [Sélection "étendue" de modalités/détails](<Selectionetenduedemodalitesdetai.md>)
