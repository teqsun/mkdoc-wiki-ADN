# BASE

## Fonction BASE

La fonction **BASE** filtre (met à "sans-réponse") les répondants de la variable en lui appliquant des conditions de validité et ajoute une modalité constituée par les individus restant en sans-réponse après application du filtre. Permettant ainsi de faire la différence entre les individus non concernées et les sans-réponse.

#### Syntaxe :&nbsp;

Q01.BASE(Filter; Text)

ou

\_BASE(Q01; Filter; Text)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | Filter | Univers | Univers d'application | Obligatoire |
| &#50; | Text | Chaîne de caractères | Optionnel : libellé à utiliser&nbsp; précédé de @code si on souhaite imposer un code à la nouvelle modalité (à éviter lors des traitements multilingues \!) | &nbsp; |


#### Exemples :

S4.BASE(S3.SELMOD(1); "@99 les vrais SR")

La variable obtenue est en tous points similaire à la variable S4. Mais ses données sont filtrées selon les répondants à S3.SELMOD(1) et la modalité des sans-réponse restant est ajoutée avec le libellé "les vrais SR" et se voit affecté le code 99.

#### Remarques :

Elle est l'équivalent de la définition&nbsp; :

S4.NORESP(99; "les vrais SR").FLT(S3.SELMOD(1))

&nbsp;

La fonction BASE() s'applique aux variables de type logique, continue ou littérale.&nbsp;

&nbsp;

&nbsp;

Voir aussi :&nbsp;

[Univers de variables](<Universciblesetsous-populations.md>)

[Combiner les variables](<Combinerlesvariables1.md>)