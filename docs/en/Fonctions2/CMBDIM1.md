# CMBDIM

## CMBDIM function

The function **CMBDIM** (which corresponds to the operator \*\*) implements the crossing on dimensions.

It has the effect of positioning the dimensions of the second variable in columns of the result.For everything else, the variable obtained is comparable to the first argument.

### Syntax: & nbsp;

Q01.cmbdim (variables)

Gold

\ _CMBDIM (Q01; Variables)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| & nbsp; | Variables | List of Variables | List of Logical Variables to Combine | Compulsory |

#### NOIKS:

This Function Allows You To Add A Crossing Dimension In The Tables (Becaus the Bases Are Preserved for Each Detail of the Variable Obtained).& Nbsp;

### EXAMPLES:

S1 \*\*S3

Gold

S1.CMBDIM (S3)

Gold

\ _Cmbdim (S1; S3)

These Three Writings Lead to the Same Result: The Variable S1 is "Repeated" for Each Methods of the S3 Variable.the Modalities of the S3 Variable Become the "Details" of the Result.

& nbsp;

See also: & nbsp;

[Combine the methods of several variables] (<combine themodalites of the days1.md>)

[Combinations] (<combine thevariables1.md>)