# SUMUP

## Fonction SUMUP

La fonction **SUMUP** permet de créer facilement un tableau récapitulatif basé sur une batterie d'items.

#### Syntaxe :&nbsp;

Q01.SUMUP(Selection)

ou

\_SUMUP(Q01; Selection)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Selection | Modalité traitée | Numéro de la modalité sur laquelle construire le récap' | Obligatoire |


#### Remarques :

La fonction SUMUP conserve l'univers de la variable source et modifie à la fois le titre long et le titre court.

ATTENTION, si les bases des détails sont variables, il faut passer par la consigne RECAP.

Les portions de texte entre parenthèses ou crochets sont détectés.

#### Exemples :

Q14 est une échelle d'accord posée sur 23 items.

Q14.SUMUP(1) donne une variable multi-réponses à 23 modalités constituée de la concaténation des 23 modalités code 1 de la variable Q14, complétée par une modalité "Autres" avec la valeur 1 pour l'ordonnateur asssocié.

&nbsp;

Voir aussi : [Traiter les variables logiques (modalités)](<Traiterlesvariableslogiquesmoda1.md>)
