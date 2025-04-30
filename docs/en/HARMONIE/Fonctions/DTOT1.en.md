# Dtot

## DTOT Function

The Function ** DTOT ** BUILDS A LITERAL VARIABLE FROM A LOGICAL VARIABLE: Each Breature Receives AS AN ANSWER The Text Of The Modality He Cited.the Transformation Into A Literal Variable Makes It Possible To Apply Text Treatments.and it is well followed for the use of identifiers (non-Digital),Digital variables.

### Syntax: & nbsp;

Q01.DTOT (Delimiter; Noanswersvalue; TextMode)

Gold

\ _DTOT (Q01; Delimiter; Noanswersvalue)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Delimite | Character Chain | Separator to Use to Concatenate The Multiple Resorts of An Individual | Different by Default |
| &#50; | Noanswersvalue | Character chain | Chain for free respondent | Different by Default |
| &#51; | TextMode | Character | Reference used for the ANSWER | "T" by Default |

#### NOIKS:

In Tables, Literal Variable Act as "Logical" Variables: The Distribution of Texts is calculated Automatically.the Order of Modalities Thus Created is Alphabetical Order.

& nbsp;

Argument 3 (TextMode) & Nbsp; Maybe:

* "C": use the codes
* "N": use the modality number
* "T": use the text of the methods (in capital letters)

& nbsp;

### EXAMPLES:

S1.DTOT ()

The variable obtained no long has any modality: it is a literal variable.the value of each breathing is a character thong.

& nbsp;

S6.dtot (" -"; "\!"; "T")

To Concatenate the Different Responses of an Individual With " -" For Separator.the Homeless Will Be Representation by "\!".

& nbsp;

See also: [Treat the Literal Variables] (<Trellious Little Little.md>)