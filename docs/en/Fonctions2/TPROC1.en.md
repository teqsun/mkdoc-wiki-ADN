# Tproc

## TPROC Function

The ** TPROC ** Function Applied A Textual Treatment to A Literal Variable.The result is a literal variable display this treatment.the non -literal variable are automatically converted during the call.the treatments to be operared on is specific in the form of a trampAvailable in the Data Reading Engine (Preprocess' Field of Datamap 2.0).

### Syntax: & nbsp;

Q01.tproc (expression)

Gold

\ _Tproc (Q01; expression)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| & nbsp; | Expression | Character Chain | Treatment Instruction | Compulsory |

### EXAMPLES:

S1.TPROC ("Trim, Upper")

Returns a literal variable for which the textual values ​​are successively rid of whites at the start and end, then pass in capital letters.

& nbsp;

S1.TPROC ('Upper (Left (@value, 2)) \ & "\!"')

Returns a Literal Variable Which Takes The First 2 Characters of The Original Texts, Pass them in Capital Letters, then Adds an Exclamation Mark.

It is possible to extract sub-parts via the concept of "beaches" such as "1..4", ": 1 .."

& nbsp;etc.

l is also possible to specific a character chain treatment in dynamic masks, for examples \ [name: 3 .. \] to ignore the first 2 characteristics of the value of the annotation \ [name \]

Here are some examples:

& nbsp;

& nbsp;

| & nbsp; | ** Expression ** | ** Description ** | ** Value Example of \ [Name \] ** | ** Result ** |
| --- | --- | --- | --- | --- |
| & nbsp; | z \ _ \ [name \] | add "z \ _" before the value of name | Q1 | Z \ _Q1 |
| & nbsp; | \ [name \] \ _ r | add "\ _r" after walking it from name | Q1 | q1 \ _R |
| & nbsp; | \ [name: 3 .. \] | Extract the characters from the 3rd unil the end | Z \ _Q1 | Q1 |
| & nbsp; | \ [name: ..- 3 \] | Extract the characters from the start to 3carcters before the end | Q1 \ _R | Q1 |
| & nbsp; | Tprocmod ("Trim \ | -4 ..- 1 \ | Upper") | Utulize Trim to Delete Spaces, Extract the Last 4 Characters and Updates them | Data \ _exmp | Exmp |
| & nbsp; | q01ad.tproc ("Lower \ | 1..4") | Converted the Castle Into Tiny, then extracts the characters in positions 1 to 4 | Hello \ _Word | Ello |

### & nbsp;

See also: & nbsp;

[Treat the Literal Variables] (<Trellious Little Little.md>)

[Labels management] (<GERERLESLIBELLESLESTEXTES1.MD>)