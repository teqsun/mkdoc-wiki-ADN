# DELMOD

## Fonction DELMOD

La fonction **DELMOD** supprime les modalités d'une variable sur la base d'un seuil exprimé en nombre d'individus. Pour supprimer des modalités précises (par position ou autres), allez voir REMMOD et HIDEMOD.

#### Syntaxe :&nbsp;

Q01.DELMOD(Value; GenerateOthers; Weighted)

ou

\_DELMOD(Q01; Value; GenerateOthers; Weighted)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Threshold | Nombre | Par défaut 0, seuil d'effectif minimum de conservation des modalités | &#48; par défaut |
| &#50; | GenerateOthers | Booléen | Par défaut pas de modalités "Autres", Crée une modalités "Autres" si TRUE | FALSE par défaut |
| &#51; | Weighted | Variable | Nom de la variable de pondération | NONE par défaut |
| &#52; | IncludeThreshold | Booléen | Si activé, les modalités atteignant le seuil sont conservées. Sinon elles sont supprimées&nbsp; | FALSE par défaut |
| &#53; | Divisor (ou Base) | Nom | Si définie, le seuil de conservation est le pourcentage des modalités sur la base indiquée :&nbsp; "R" pour les répondants "A" pour les réponses "I" pour les interrogés "N" pour les sans-réponses | NONE par défaut, alors seuil en effectif |
| &#54; | Universe | Variable | Nom de la variable univers à utiliser pour le calcul des statistiques. Si vide pas d'univers | NONE par défaut |


#### Remarques :

La modalité "Autres" est automatiquement épinglée donc exclue des tris hiérarchiques (cf. [PINMOD](<PINMOD.md>)).&nbsp;

DELMOD est très différent de DELCOL et DELROW.

&nbsp;

#### Exemples :

S1.DELMOD()

Supprime toutes les modalités vides.

&nbsp;

S1.DELMOD(30)

Supprime toutes les modalités dont l'effectif est inférieur ou égal à trente.

&nbsp;

S1.DELMOD(30; TRUE)

Supprime toutes les modalités dont l'effectif est inférieur ou égal à trente et crée un sous-total "autres" qui les regroupe (en dernière modalité).

&nbsp;

S1.DELMOD(30; TRUE; TRUE)

Supprime toutes les modalités dont l'effectif pondéré est inférieur à trente et crée un sous-total "autres" qui les regroupe (en dernière modalité) en tenant compte de la pondération de la variable.

&nbsp;

S1.DELMOD(30; TRUE; WEIGHT)

Supprime toutes les modalités dont l'effectif pondéré est inférieur à trente et crée un sous-total "autres" qui les regroupe (en dernière modalité) en appliquant la pondération WEIGHT.

&nbsp;

S1.DELMOD(10; FALSE; NONE;FALSE;"R";NONE)

Supprime toutes les modalités dont le pourcentage brut est inférieur à 10% sur la base des répondants.

&nbsp;

&nbsp;

Voir aussi :&nbsp;

[Traiter les variables logiques (modalités)](<Traiterlesvariableslogiquesmoda1.md>)

[Gestion des dimensions](<Gererlesdimensionsdesvariables1.md>)
