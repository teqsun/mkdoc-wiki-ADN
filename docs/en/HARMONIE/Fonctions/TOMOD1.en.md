# Tomod

## Tomod Function

The ** Tomod ** Function is an instruction which allows a digital variable to be representing in the form of modality and control the calculation Displayed.

This Function is very useful for the Treatment of Ladders or Multi-Answers for Which We Want To Add An Average Number or A Standard Deviation (etc.).

& nbsp;

### please: do not use this fun we have variable dimensioned.

### Syntax: & nbsp;

Q01.Tomod (calculations; label; presertittitle)

Gold

\ _TOMOD (Q01; Calculations; label; Presertittitle)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Calculation | Character Chain | List of Calculations to apply Separated by ',' or ',,' | Different by Default |
| &#50; | label | Character chain | Label of the modality | Different by Default |
| &#51; | Presertittitle | Boolean | If True, Creates a subtitle which corresponds to the title of the variable treated | False by Default |

#### NOIKS:

Please note, tomod is an instruction: it is assessled dynamically when calculating tables (like recap).

To add the Display of meaning tests in the tables, Use the testq1 Calculation name (Statistical test Applied to the Quantities).

If the Control of the Displayed Calculation is not necessary, it is preferable to use the [juxvar] Function (<juxvar1.md>).

** The Q01.mod ($ M $ Q) METHOD IS MORE GENERALIZABLE IN PARTECLARD FOR DIMENSED VARIABLE.**

### EXAMPLES:

\ _JUXVAR (Q1; Q1Q.TOMOD ("Mean ,, TestQ1"; "Average and test")

& nbsp;

See also: & nbsp;

"Examination" Selection of Modalities/Details

[List of Standard calculations] (<calculationstandards1.md>)

[Utilities \ & Miscellaneous] (<tools _misc1.md>)

[Present the variables in the tables] (<PertERDERLESVARIABLE WHILESTAB1.MD>)