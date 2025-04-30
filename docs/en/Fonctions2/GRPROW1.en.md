# Grprow

## GRPROW FUNCTION

The ** Grprow ** function allows you to group the columns of a variable. & Nbsp;

The arguments correspond to the different desired groups.The result variable has as many lines as there are groupings.To create a group, simply use the syntax relating to items selections and/or the extended selection of modalities/details.

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

* Or for logical variables,
* SUM for digital variables.

#### Examples:

S1.GRPROW (1 2; 1; 2; -1)

Creates a new variable whose lines are:

\- The grouping of lines 1 and 2 of S1

\- The first line of S1

\- The Second Line of S1 & Nbsp;

\- The last of S1.

& nbsp;

S1.GRPMOD (1 2; 1; 2; $ o)

CREATES A NEW VARIABLE WHOSE LINES ARE:

\- The Grouping of Lines 1 and 2 of S1

\- The first line of S1

\- The Second Line of S1 & Nbsp;

\- The non-cited modalities

& nbsp;

See also: [Dimensions management] (<GERERLESDIMENSESDESSEVARIABLE1.MD>)