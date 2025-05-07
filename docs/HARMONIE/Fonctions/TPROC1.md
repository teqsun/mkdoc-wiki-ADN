# TPROC

## Fonction TPROC

La fonction **TPROC** applique un traitement textuel à une variable littérale. Le résultat est une variable littérale après application de ce traitement. Les variables non littérales sont automatiquement converties lors de l'appel. Les traitements à opérer sont spécifier dans l'argument sous la forme d'une chaîne de caractère et suivent les traitements disponibles dans le moteur de lecture de données (champ 'PREPROCESS' des DATAMAP 2.0).

#### Syntaxe :&nbsp;

Q01.TPROC(Expression)

ou

\_TPROC(Q01; Expression)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &nbsp; | Expression | Chaîne de caractères | Instruction de traitement | Obligatoire |


#### Exemples :

S1.TPROC("TRIM, UPPER")

Retourne une variable littérale pour laquelle les valeurs textuelles sont successivement débarrassées des blancs en début et en fin, puis passées en majuscules.

&nbsp;

S1.TPROC('UPPER(LEFT(@VALUE, 2)) \& " \!"')

Retourne une variable littérale qui prend les 2 premiers caractères des textes d'origine, les passe en majuscules, puis y ajoute un point d'exclamation.

Il est possible d'extraire des sous-parties via la notion de "plages" telles que "1..4", ":1.."

&nbsp;etc.

l est également possible de spécifier un traitement de chaîne de caractères dans les masques dynamiques, par exemple \[NAME:3..\] pour ignorer les 2 premiers caractèes de la valeur de l'annotation \[NAME\]

Voici quelques exemples :

&nbsp;

&nbsp;

| &nbsp; | **Expression** |**Description**|**Valeur exemple de \[NAME\]**|**Résultat** |
| --- | --- | --- | --- | --- |
| &nbsp; | Z\_\[NAME\] | Ajoute "Z\_" avant la valeur de NAME | Q1 | Z\_Q1 |
| &nbsp; | \[NAME\]\_R | Ajoute "\_R" après la valuer de NAME | Q1 | Q1\_R |
| &nbsp; | \[NAME:3..\] | Extrait les caractères à partir du 3e jusqu'à la fin | Z\_Q1 | Q1 |
| &nbsp; | \[NAME:..-3\] | Extrait les caractères du début jusqu'à 3caractères avant la fin | Q1\_R | Q1 |
| &nbsp; | TPROCMOD("TRIM\|-4..-1\|UPPER") | Utulise TRIM pour supprimer les espaces, extrait les 4 derniers caractères et les met en majuscules | DATA\_EXMP | EXMP |
| &nbsp; | Q01AD.TPROC("LOWER\|1..4") | Convertit la châine en minuscule, puis extrait les caractères en positions 1 à 4 | HELLO\_WORD | ello |


#### &nbsp;

Voir aussi :&nbsp;

[Traiter les variables littérales](<Traiterlesvariableslitterales.md>)

[Gestion des libellés](<Gererleslibelleslestextes1.md>)