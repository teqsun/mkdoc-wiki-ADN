# Loginfo

## Loginfo function

The ** Loginfo ** Function Allows You To Display A Message in The Newspaper During A recodification.& Nbsp;

### Syntax: & nbsp;

\ _Loginfo (variable; text)

Or

variable.loginfo (text)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| & nbsp; | Text | Character chain | Displayed message in the Newspaper.use of Possible annotations. | Compulsory |


#### Examples:

Q1.Title ("New Title").Loginfo ("Update of the Title of Q1")

The message "Update of the Q1 title" appears in the newspaper.

With the use of annotations \ [title \] and \ [name \], it is possible to write:

Q1.loginfo ("The Title of \ [Name \] is \ [Title \]")

This displays in the newspaper: "The title of ** Q1 ** is ** Q1. Age of the question **"

& nbsp;

#### Remarks :

The annotations available are:

\ [Name \]: name of the variable

\ [Title \]: Title variable

\ [Title: s \]: short title of the variable

\ [How \]: Commentary on the variable

\ [Universe \]: Universe of the variable

\ [Weight \]: Weight of the variable

\ [Definition \]: Definition of the variable & nbsp;

& nbsp;

See also: & nbsp;

[Treat the Logical Variables (Modalities)] (<trelligableslogicalsmoda1.md>)

[Present the variables in the tables] (<pretenderlesvariableables whilestAb1.md>)

[Criteria] (<Creerdescriteresoubannieres1.md>)

[Combine the variables] (<combine thevariables1.md>)