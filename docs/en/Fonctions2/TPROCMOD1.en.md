# TPROCMOD

## TPROCMOD FUNCTION

The ** TPROCMOD ** FUNCTION APPLIES A TEXTAL PRODESSING TO THE MODALITIES OF A LOGICAL VARIABLE.

The Treatments to be Operated On is specific in the Argument in the Form of A Character Chain and Follow the Processing Avairable In The Data Reading Engine (Pre -procus' Field of Datamap 2.0).

& nbsp;

The tprocol and tprow functions work exactly on the same fashion, but the first apps to the "columns" dimension and the second to the "line" dimension of the source variable.

### Syntax: & nbsp;

Q01.tprocmod (expression; selection)

Gold

\ _TPROCMOD (Q01; Expression; selection)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Expression | Character Chain | Treatment Instruction | Compulsory |
| &#50; | Selection | List of Character Strings | Selection of Positions | Different by Default |

### EXAMPLES:

S1.TPROCMOD ("Trim, Upper")

Returns a logical variable whose modalities are successively rid of white at the start and end, then pass in capital letters.

& nbsp;

S1.tprocmod ('Upper (Left (@value, 2)) \ & "\!"')

Returns a logical variable which takes as modalities the first 2 characters of the original methods, switches to the uppercase, then adds an exclamation point.

& nbsp;

See also: & nbsp;

[Labels Management] (<GERERLIBELSLIBALESTHESTEXTES1.MD>)

[Treat the Literal Variables] (<Trellious Little Little.md>)