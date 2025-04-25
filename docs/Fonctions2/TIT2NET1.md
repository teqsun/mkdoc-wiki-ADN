# TIT2NET

## Fonction TIT2NET

La fonction **TIT2NET** convertit automatiquement les sous-titres en sous-totaux.

&nbsp;

Les sous-titres agissent comme des "têtes de chapitres" dans les dimensions des variables (modalités, détails, etc.). Après application, chaque sous-titre devient un regroupement de modalités, mais conserve le même niveau hiérarchique en termes de présentation.

#### Syntaxe :&nbsp;

Q01.TIT2NET(True;1;1)

ou

\_TIT2NET(Q01;True;1;1)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Divisor | Booléen | Si TRUE, modifie le diviseur pour que les bases soient les sous-totaux créés. | par défaut False, pas de diviseur |
| &nbsp; | LevelUsed | Numérique | Niveau de sous-titre à partir duquel commencer à créer les sous-totaux | &nbsp; |
| &nbsp; | StandardBase | Numérique | Si 0, alos la base standard est lla base de la variable. Si 1, les sous-totaux de niveau 1 sont des bases à part entière, etc. | &nbsp; |


#### Exemples :

S1.TIT2NET()

Dans la variable résultante, les sous-titres sont "remplacés" par des sous-totaux.

&nbsp;

Voir aussi : [Traiter les variables logiques (modalités)](<Traiterlesvariableslogiquesmoda1.md>)
