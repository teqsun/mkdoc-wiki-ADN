# NA2VAL

## Fonction NA2VAL ou NATOVAL

La fonction **NA2VAL** s'applique aux variables numériques, littérales et temporelles.&nbsp;

Elle a pour effet de créer une variable dans laquelle les sans-réponses à la variable d'origine sont réaffectés à une valeur particulière.

La variable obtenue n'a donc plus de sans-réponse.

#### Syntaxe :&nbsp;

Q01.NA2VAL(Value)

ou

\_NA2VAL(Q01; Value)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Value | Nombre | Valeur affectée aux sans-réponse | Obligatoire |


#### Remarques :

Pour une ré-affection de réponse plus avancée, utilisez la fonction FIX.

#### Exemples :

AGE.NA2VAL(45)

Crée une variable dans laquelle les sans-réponses ont récupéré la valeur 45. Il n'y a plus de sans-réponse.

&nbsp;

Voir aussi : [Manipuler les variables numériques](<Manipulerlesvariablesnumeriques1.md>)
