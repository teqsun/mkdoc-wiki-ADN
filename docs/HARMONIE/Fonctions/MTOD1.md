# MTOD

## Fonction MTOD

La fonction **MTOD** transforme une variable multi-réponses en variable mono-réponse. Deux possibilités sont offertes : soit la "plus petite" des modalités citées est retenue, soit la fonction ne retient que ceux qui ont donné une seule et unique réponse.

&nbsp;

L'argument optionnel permet de déterminer le mode de travail :

FALSE (valeur par défaut) : la plus petite modalité citée est retenue

TRUE : seuls les répondants qui n'ont cité qu'une seule modalités sont retenus

#### Syntaxe :&nbsp;

Q01.MTOD(SingleAnswerOnly)

ou

\_MTOD(Q01; SingleAnswerOnly)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | SingleAnswerOnly | Booléen | Par défaut, considère toutes les réponses | FALSE par défaut |


#### Exemples :

S6.MTOD()

\[ou S6.MTOD(FALSE)\]

La variable résultante est une mono-réponse dont les réponses sont uniquement les plus petites modalités citées.

&nbsp;

S6.MTOD(TRUE)

La variable résultante est une mono-réponse dont les réponses sont celles de ceux qui n'ont cité qu'une seule réponse.

&nbsp;

Voir aussi : [Traiter les variables logiques (modalités)](<Traiterlesvariableslogiquesmoda1.md>)
