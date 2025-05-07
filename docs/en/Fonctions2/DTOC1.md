# Dtoc

## DTOC function

The **DTOC** Function Builds A Digital Variable from a logical variable by Assiging Each Modality A Numerical Value.

Each Breathe Thus Receives The Numeric Value Associated With Their Responsible Modality.

This fun is useful for calculating, for examination, average scores on scales.

& nbsp;

The values ​​associated with the methods can be specified in the variable itself via are reducing, or directly in the function call, of your choice.

By default, the reducer is used as associated values

### Syntax: & nbsp;

Q01.DTOC (values)

Gold

\ _DTOC (Q01; values)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| & nbsp; | Values ​​| Nurse List or Code | Assigned to the methods **or** possible codes: "N" for the modality number "t" for the "r" modality text for the modality reducing "c" for the modality code | Compulsory |

#### NOIKS:

On a multi-response variable with a 1 reducer, the function returns as standard the number of responses cited.

The Particular Value Na (OR Nan) Indicates that the Associated Modality Will be Excluded in the Conversion Into Numeric Value.

This value is associated by default with subtotals from Grouping Methods.

Be careful, a 0 reducing do not excluded the associated modality of the variable created.

The Dtoc & Nbsp Function; Retains The Dimensions and the Universe of the Variable Source.

& nbsp;

#### Examples:

Q02C.DTOC (10 20 30 40 50)

This call Applies A Digital Conversion by Assiging the Values ​​10, 20, 30, 40 and 50 to Modalities 1 to 5 of the Q02c Variable.The Resulting Variable is a quantity whose average is Thus Between 10 and 50.

& nbsp;

Q02C.DTOC ()

This call is similar to the previous one with the different that the coefficient applied to the methods are reading in the q02c variable, directly (the "reducing").

& nbsp;

S3.DTOC ("T")

Creates a digital variable by associating with each modality a digital value deduced from the wording (text).

& nbsp;

S3.DTOC ("n")

Creates a digital variable by associating with each modality its modality number as a numerical value.

& nbsp;

S3.DTOC ("C")

CREATES A DIGITAL VARIABLE by Associating With Each Modality A Deducted Numeric Value of the Code.

& nbsp;

It is possible to operate the Properties of Retail Lines/Columns During the Digital Generation Based on Properties (Codes, Texts, etc.). To do this, Simply PREFIX by "C" to use the Properties of the Columns and by "R" for the Properties of the Lines.

Q12.DTOC ("CC")

This definition creates a continuous variable whose value is the code of columns.

& nbsp;

See also: [Treat Logical Variables (Modalities)] (<TrelligablelogiquesModa1.md>)