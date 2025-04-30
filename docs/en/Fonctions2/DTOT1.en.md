# Dtot

## DTOT Function

The function ** dtot ** builds a literal variable from a logical variable: each respondent receives as an answer the text of the modality he cited.The transformation into a literal variable makes it possible to apply text treatments.And it is well suitable for the use of textual identifiers (non-digital), formatting of multi-answer or digital variables.

### Syntax: & nbsp;

Q01.DTOT (Delimiter; Noanswersvalue; TextMode)

Or

\ _DTOT (Q01; Delimiter; Noanswersvalue)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Delimite | Character Chain | Separator to Use to Concatenate The Multiple Resorts of An Individual | Different by Default |
| &#50; | Noanswersvalue | Character chain | Chain for free respondent | Different by Default |
| &#51; | TextMode | Character | Reference used for the ANSWER | "T" by Default |

#### NOIKS:

In tables, literal variables act as "logical" variables: the distribution of texts is calculated automatically.The order of modalities thus created is alphabetical order.

& nbsp;

Argument 3 (textmode) & nbsp;maybe :

* "C": use the codes
* "N": use the modality number
* "T": use the text of the methods (in capital letters)

& nbsp;

### EXAMPLES:

S1.DTOT ()

The variable obtained no longer has any modality: it is a literal variable.The value of each respondent is a character string.

& nbsp;

S6.dtot (" -"; "\!"; "T")

To concatenate the different responses of an individual with " -" for separator.The homeless will be represented by "\!".

& nbsp;

See also: [Treat the Literal Variables] (<Trellious Little Little.md>)