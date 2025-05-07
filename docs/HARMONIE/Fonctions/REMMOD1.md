# REMMOD

## Fonction REMMOD

La fonction **REMMOD** supprime les modalités d'une variable. La base de la variable obtenue est celle des répondants aux modalités restantes.

&nbsp;

Les arguments correspondent aux listes des modalités à retenir. Chaque liste suit la syntaxe relative aux sélections d'items.

#### Syntaxe :&nbsp;

Q01.REMMOD(Keys)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Keys | Liste de valeurs | Liste des positions affectées | Obligatoire |


#### Remarques :

Cette fonction modifie donc la base de travail. Pour ne pas modifier la base de la variable, il faut utiliser la fonction HIDEMOD qui se contente de 'cacher' les modalités dans les tris résultants.

#### Exemples :

S1.REMMOD(1 -1)

Crée une nouvelle variable dans laquelle ne figurent plus ni la première ni la dernière modalité de la variable d'origine (S1).

Les fonctions REMCOL et REMROW fonctionnent exactement sur le même mode, mais la première s'applique à la dimension "colonnes" et la seconde à la dimension "lignes" de la variable source.

&nbsp;

S1.REMMOD("ST \*")

Supprime toutes les modalités dont le libellé commence par "ST ".

&nbsp;

Voir aussi :&nbsp;

[Traiter les variables logiques (modalités)](<Traiterlesvariableslogiquesmoda1.md>)

[Gestion des dimensions](<Gererlesdimensionsdesvariables1.md>)