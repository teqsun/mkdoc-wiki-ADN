# DTOT

## Fonction DTOT

La fonction **DTOT** construit une variable littérale depuis une variable logique : chaque répondant reçoit en guise de réponse le texte de la modalité qu'il a citée. La transformation en variable littérale permet d'appliquer des traitements textuels. Et elle convient bien à l'utilisation des identifiants textuels (non numériques), au formatage des variables multi-réponses ou numériques.

#### Syntaxe :&nbsp;

Q01.DTOT(Delimiter; NoAnswersValue;TextMode)

ou

\_DTOT(Q01; Delimiter; NoAnswersValue)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Delimiter | Chaîne de caractères | Séparateur à utiliser pour concaténer les réponses multiples d'un individu | NUL par défaut |
| &#50; | NoAnswersValue | Chaîne de caractères | Chaîne pour les sans-réponse | NUL par défaut |
| &#51; | TextMode | Caractère | Référence utilisée pour la réponse | "T" par défaut |


#### Remarques :

Dans les tableaux, les variables littérales agissent comme les variables "logiques" : la distribution des textes est calculée automatiquement. L'ordre des modalités ainsi créées est l'ordre alphabétique.

&nbsp;

L'argument 3 (TextMode)&nbsp; peut être :

* "C" : utilise les codes
* "N" : utilise le n° de modalité
* "T" : utilise le texte des modalités (en majuscules)

&nbsp;

#### Exemples :

S1.DTOT()

La variable obtenue ne comporte plus de modalité : c'est une variable littérale. La valeur de chaque répondant est une chaîne de caractères.

&nbsp;

S6.DTOT(" - "; "\!";"T")

Pour concaténer les différentes réponses d'un individu avec " - " pour séparateur. Les sans-réponses seront représentés par des "\!".

&nbsp;

Voir aussi :[ Traiter les variables littérales](<Traiterlesvariableslitterales.md>)