# RECAP

## Fonction RECAP

La consigne **RECAP** permet de créer facilement un tableau récapitulatif basé sur une batterie d'items (ou grille d'items).

A la différence de SUMUP, cette fonction ne modifie pas la variable, mais se contente d'indiquer au moteur de ventilation quelles sont les modalités à cacher.

&nbsp;

Inconvénient : il n'est pas possible d'exploiter la variable résultat dans une autre recodification

Avantage : la méthode marche aussi lorsque les bases des détails varient

#### Syntaxe :&nbsp;

Q01.RECAP(sélection)

ou

\_RECAP(Q01; sélection)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | sélection | Liste de valeurs | Modalités sélectionnées | Obligatoire |


#### Remarques :

La fonction RECAP conserve l'univers de la variable source.

La fonction RECAP ne modifie pas la base de la variable utilisée.

##### Exemples :

Q14 est une échelle d'accord posée sur 23 items.

Q14.RECAP(1) n'affichera que les scores de la première modalité pour chacun des détails de la Q14.

&nbsp;

Voir aussi :&nbsp;

[Traiter les variables logiques (modalités)](<Traiterlesvariableslogiquesmoda1.md>)

[Présenter les variables dans les tableaux](<Presenterlesvariablesdanslestab1.md>)