# DTOC

## Fonction DTOC

La fonction **DTOC** construit une variable numérique depuis une variable logique en assignant à chaque modalité une valeur numérique.

Chaque répondant reçoit ainsi la valeur numérique associée à sa modalité de réponse.

Cette fonction est utile pour calculer par exemple des scores moyens sur des échelles.

&nbsp;

Les valeurs associées aux modalités peuvent être spécifiées dans la variable elle-même via sont réducteur, ou directement dans l'appel de fonction, au choix.

Par défaut, le réducteur est utilisé en tant que valeurs associées

#### Syntaxe :&nbsp;

Q01.DTOC(Values)

ou

\_DTOC(Q01; Values)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Values | Liste de nombres ou un code | Valeurs affectées aux modalités **OU BIEN** Codes possibles : "N" pour le numéro de modalité "T" pour le texte de modalité "R" pour le réducteur de modalité "C" pour le code de modalité | Obligatoire |


#### Remarques :

Sur une variable multi-réponses avec un réducteur à 1, la fonction retourne en standard le nombre de réponses citées.

La valeur particulière Na (ou NAn) indique que la modalité associée sera exclue dans la conversion en valeur numérique.

Cette valeur est associée par défaut aux sous-totaux issus de regroupement de modalités.

Attention un réducteur à 0 n'exclut pas la modalité associée de la variable créée.

La fonction DTOC&nbsp; conserve les dimensions et l'univers de la variable source.

&nbsp;

#### Exemples :

Q02C.DTOC(10 20 30 40 50)

Cet appel applique une conversion numérique en assignant les valeurs 10, 20, 30, 40 et 50 aux modalités 1 à 5 de la variable Q02C. La variable résultante est une quantité dont la moyenne est ainsi comprise entre 10 et 50.

&nbsp;

Q02C.DTOC()

Cet appel est similaire au précédent à la différence que les coefficients appliqués aux modalités sont lus dans la variable Q02C, directement (le "réducteur").

&nbsp;

S3.DTOC("T")

Crée une variable numérique en associant à chaque modalité une valeur numérique déduite du libellé (du Texte).

&nbsp;

S3.DTOC("N")

Crée une variable numérique en associant à chaque modalité son numéro de modalité comme valeur numérique.

&nbsp;

S3.DTOC("C")

Crée une variable numérique en associant à chaque modalité une valeur numérique déduite du code.

&nbsp;

Il est possible d'exploiter les propriétés des détails Lignes/Colonnes lors de la génération numérique basée sur des propriétés (codes, textes, etc.). Pour ce faire, il suffit de préfixer par "C" pour utiliser les propriétes des Colonnes et par "R" pour les propriétés des Lignes.

Q12.DTOC("CC")

Cette définition crée une variable continue dont la valeur est le code des colonnes.

&nbsp;

Voir aussi : [Traiter les variables logiques (modalités)](<Traiterlesvariableslogiquesmoda1.md>)
