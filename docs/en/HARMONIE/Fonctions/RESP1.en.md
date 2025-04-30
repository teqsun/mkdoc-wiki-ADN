# Resp

## Resp Function

The ** Resp ** Function manipulates respondent of a variable by adding or combining them to an existing modality.its syntax is equivalent to that of the noresp function.

#### Syntax n ° 1: & nbsp;

Q01.resp ()

Gold

\ _RESP (Q01)

& nbsp;

This version within Argument Simply Returns The respondent to the variable (Good Method for Creating A Filter / A Universe \!).

#### Syntax n ° 2: & nbsp;

Q01.resp (insertionpoint; margintext)

Gold

\ _RESP (Q01; insertionpoint; Margintext)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | InsertionPoint | Number | Insertion position: If it is Worth 0, the marginal is added at the top of the variable.if it is width the number of modalities, the marginal is added at the end.& Nbsp; If it is between 1 and 2 (1.5 for exams), it is inserted between modality 1 and modality 2 (etc.). | Compulsory |
| &#50; | Margintext | Character chain | Optional: label to use with @code if you want to code to the new modality (to be had multilingual daring treatments \!). | Default indefinite |

### EXAMPLES:

S2.RESP ()

Returns a filter that conveys respondents to the S2 variable.

& nbsp;

S1.resp (99; "@99 Total")

Add the respondent of the S1 Variable S1 in the Last "Total" Worded Mode (Insofar as the Variable S1 at Less Than 99 Modalities ...) and affects the code 99.

& nbsp;

S1.RESP (0)

Add the respondent of the S1 variable in the first modality.

& nbsp;

S1.RESP (2.5)

Add the respondent of the S1 Variable Between the 2nd and the 3rd Methods.

& nbsp;

See also: [Universe of Variables] (<UniverscibleSets-Populations.md>)