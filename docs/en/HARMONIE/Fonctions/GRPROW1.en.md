# Grprow

## GRPROW FUNCTION

The ** Grprow ** function allows you to group the columns of a variable. & Nbsp;

The arguments corresponds to the different desired groups.

### Syntax: & nbsp;

Q01.grprow (Keys)

Gold

\ _GRPROW (Q01; Keys)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|& nbsp;|Keys |List of values ​​|List of & nbsp;Elements to be treated |Compulsory |

#### NOIKS:

The grouping operator is: & nbsp;

* Now for variable logical,
* Sum for Digital Variables.

### EXAMPLES:

S1.GRPROW (1 2; 1; 2; -1)

CREATES A NEW VARIABLE WHOSE LINES ARE:

\- The grouping of lines 1 and 2 of S1

\- The First Line of S1

\- The second line of S1 & Nbsp;

\- The Last of S1.

& nbsp;

S1.GRPMOD (1 2; 1; 2; $ o)

Creates a new variable whose lines are:

\- The Grouping of Lines 1 and 2 of S1

\- The First Line of S1

\- The Second Line of S1 & Nbsp;

\- The non-cited modalities

& nbsp;

See also: [Management dimensions] (<GERERLESDIMENSESDESSEVARIAIA1.MD>)