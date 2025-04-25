# INVERT

## Fonction INVERT

La fonction **INVERT** permet de sélectionner le complément des modalités choisies hors sans-réponses

#### Syntaxe :&nbsp;

Q01.INVERT(Selection)

ou

\_INSVERT(Q01; Selection)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Selection | Liste de valeurs | Liste des N° de modalités à traiter | Obligatoire |


#### Exemples :

S3.INVERT(1 3)

Retourne une variable logique dont les deux modalités sont les compléments des modalités 1 et 3 hors sans-réponses. La base répondants initiale est conservée.

&nbsp;

## Il est aussi possible d'écrire S3.MOD(~1 ~3)

&nbsp;

Voir aussi :&nbsp;

[Traiter les variables logiques (modalités)](<Traiterlesvariableslogiquesmoda1.md>)

[Gestion des libellés](<Gererleslibelleslestextes1.md>)

