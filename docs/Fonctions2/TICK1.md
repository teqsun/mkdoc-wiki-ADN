# TICK

## Fonction TICK

La fonction **TICK** construit une variable numérique retournant le nombre de TICKS écoulés depuis le 1er janvier 1 à 00:00:00 (calendrier grégorien) et la date de la variable temporelle placée en argument.

&#49; tick&nbsp; = 100 nanosecondes

#### Syntaxe :&nbsp;

Q01.TICK(NaValue)

ou

\_TICK(Q01; NaValue)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | NaValue | Nombre | Valeur des sans-réponse | Nombre invalide par défaut |


#### Exemples :

DATES.TICK()

Décode la variable temporelle DATES et retourne le nombre de ticks écoulés.

Il s'est écoulé 600077939360170000 ticks entre le 1er janvier 1 et le 29 juillet 1902 à 15:38:56

&nbsp;

Voir aussi : [Manipuler les variables temporelles et de durées](<Manipulerlesvariablestemporelle1.md>)
