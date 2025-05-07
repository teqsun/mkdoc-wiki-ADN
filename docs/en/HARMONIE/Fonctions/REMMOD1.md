# Remmod

## Remmod function

The **Remmod** function removes the methods of a variable.The basis of the variable obtained is that of respondents to the remaining methods.

& nbsp;

The arguments corresponds to the lists of the method to be remembered.each list follows the syntax relating to items selections.

### Syntax: & nbsp;

Q01.Remmod (Keys)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| & nbsp; | Keys | List of values ​​| List of Affuted Positions | Compulsory |

#### NOIKS:

This Function Therefore Modifies The Work Base.in Order Not To Modify the Basis of the Variable, You Must use the Hidemod Function which is content to 'hide' The Methods in the Resulting Sorts.

#### Examples:

S1.Remmod (1 -1)

Creates a new variable in which neither the first nor the last modality of the original variable (S1) is no longer included.

The Remcol and Remrow functions work exactly on the same mode, but the first applies to the "columns" dimension and the second to the "line" dimension of the source variable.

& nbsp;

S1.Remmod ("St \*")

Removes All The Methods Whose Label Begins with "St".

& nbsp;

See also: & nbsp;

[Treat the Logical Variables (Modalities)] (<trelligableslogicalsmoda1.md>)

[Management dimensions] (<reurlesdimensesdesdesdairaible1.md>)