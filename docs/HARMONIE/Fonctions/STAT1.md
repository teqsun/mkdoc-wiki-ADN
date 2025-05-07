# STAT

## Fonction STAT

La fonction **STAT** retourne une variable numérique, chaque individus reçoit le % de ses citations.

#### Syntaxe :&nbsp;

Q01.STAT(Universe;Weight;Base;Factor)

ou

\_STAT(Q01;Universe;Weight;Base;Factor)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Universe | Variable | Univers appliqué | Vide par défaut |
| &nbsp; | Weight | Variable | Pondération à appliquer (optionnel) | Vide par défaut |
| &nbsp; | Base | Caractère | Base du % R : Répndants et I : Interrogés | Effectif si vide |
| &nbsp; | Factor | Entier | Coefficient multiplicateur de %&nbsp; | &#49;00 par défaut |


#### Exemples :

SEXE.STAT() retourne une continue avec le % (ex: 40) d'homme pour les hommes et le % (ex: 60) de femme pour les femmes

SEXE.STAT(UNIV;POIDS) retourne le % filtré par UNIV et pondéré par POIDS

SEXE.STAT(NONE;NONE;NONE) retourne les effectifs bruts.

#### Remarques :

Les variables dimensionnées sont supportées.