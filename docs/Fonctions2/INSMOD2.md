# INSMOD

## Fonction INSMOD

La fonction **INSMOD** ajoute une modalité vide avant la position indiqué et lui attribue un libellé.

#### Syntaxe :&nbsp;

Q01.INSMOD(InsertionPoint; Text)

ou

\_INSMOD(Q01; InsertionPoint; Text)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | InsertionPoint | Nombre | Position d'insertion : La nouvelle modalité sera insérée avant la position indiquée. | Obligatoire |
| &#50; | Text | Chaîne de caractères | Optionnel : libellé à utiliser&nbsp; (à éviter lors des traitements multilingues \!) | &nbsp; |


#### Exemples :

S3.INSMOD(2; "Mon libellé")

Retourne une variable logique dont la 2e modalité a pour texte "Mon libellé".

&nbsp;

Voir aussi :&nbsp;

[Traiter les variables logiques (modalités)](<Traiterlesvariableslogiquesmoda1.md>)

[Gestion des libellés](<Gererleslibelleslestextes1.md>)

