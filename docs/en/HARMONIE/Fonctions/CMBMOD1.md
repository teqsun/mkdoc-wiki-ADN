# CMBMOD

## CMBMOD Function

The Function **CMBMOD** Combines The Modalities of A Variable.& Nbsp;

### Syntax: & nbsp;

Q01.CMBMOD (Source; PermutationSize; Exactly; Removeempty; Soultresults; Insertsubitles; Insertsubto)

Gold

\ _Cmbmod (Q01; Source; PermutationSize; Exactly; Removeempty; Soultresults; Insertsubtles; Insertsubto)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Source | Variable | Multi-Answer Variable | Compulsory |
| &#50; | PermutationSize | Whole | by Default, All possible Sizes combination | \ -1 Default |
| &#51; | Exactly | Boolean | All Answers Exactly If True | False by Default |
| &#52; | Removeempty | Boolean | by Default, Keeps Empty Combinations | False by Default |
| &#53; | Spells | Boolean | Fault, Non -Sorted Results | False by Default |
| &#54; | Insertsubtitles | Boolean | by Default, no subtitles | False by Default |
| &#55; | Insertsubtotal | Boolean | Default no subtotals | False by Default |

#### NOIKS:

Please note, without argument, it produces all possible combinations ... and can therefore requires significant calm \!

### EXAMPLES:

S6.CMBMOD (2)

Returns a variable which contains all the existing combinations of 2 modalities among the modalities of the s6 variable.

& nbsp;

S6.CMBMOD (-1; True; True; True; True; False)

Returns a variable with all the exclusive combinations, sorted with subtitles.

& nbsp;

See also: [Combine the Modalities of Several Variables] (<Combine Themodalites of the Days1.md>)