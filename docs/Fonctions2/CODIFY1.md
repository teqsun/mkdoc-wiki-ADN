# CODIFY

## Fonction CODIFY

La fonction **CODIFY** affecte des codes aux modalités d'une variable.

Les codes identifient les modalités de façon plus "stable" que les numéros de modalités, et sont utilisés pour les exports de données.

&nbsp;

L'argument attendu (en plus de la variable à coder) est la liste des codes à affecter.

#### Syntaxe :&nbsp;

Q01.CODIFY(Codes)

ou

\_CODIFY(Q01; Codes)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Codes | Liste de chaînes de caractères | Liste des codes à affecter | NUL par défaut |


#### Remarques :

La conservation des codes après application d'autres recodifications n'est pas garantie.

Toutes les modalités doivent être décrites

#### Exemples :

\_CODIFY(S1; 1 2 3 4 99)

Retourne une variable dont les modalités sont respectivement identifiées par les codes 1 2 3 4 99

&nbsp;

Voir aussi :&nbsp;

[Traiter les variables logiques (modalités)](<Traiterlesvariableslogiquesmoda1.md>)

[Propriétés des variables](<Modifierlesproprietesdesvariable.md>)