# Loginfo

## Loginfo Function

The ** Loginfo ** Function Allows You To Display A Message in The Newspaper During A recodification.& Nbsp;

### Syntax: & nbsp;

\ _Loginfo (variable; text)

Gold

variable.loginfo (text)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| & nbsp; | Text | Character chain | Displayed message in the Newspaper.use of Possible annotations. | Compulsory |

### EXAMPLES:

Q1.Title ("New Title").Loginfo ("Update of the Title of Q1")

The message "Update of the Q1 Title" Appears in the Newspaper.

With the use of annotations \ [title \] and \ [name \], it is possible to write:

Q1.loginfo ("The Title of \ [Name \] is \ [Title \]")

This Displays in the Newspaper: "The Title of ** Q1 ** is ** Q1. Age of the question **"

& nbsp;

#### NOIKS:

The annotations available are:

\ [Name \]: name of the variable

\ [Title \]: Title variable

\ [Title: S \]: short title of the variable

\ [How \]: Commentary on the variable

\ [Universe \]: Universe of the variable

\ [Weight \]: Weight of the variable

\ [Definition \]: Definition of the variable & nbsp;

& nbsp;

See also: & nbsp;

[Treat the Logical Variables (Modalities)] (<trelligableslogicalsmoda1.md>)

[Present the variables in the tables] (<PertERDERLESVARIABLE WHILESTAB1.MD>)

[Criteria] (<Creerdescriteresoubannieres1.md>)

[Combination the variables] (<combination thevariables1.md>)