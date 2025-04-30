# GRPMOD

## GRPMOD function

The ** GRPMOD ** function makes it possible to group the methods of a variable. & Nbsp;

The arguments corresponds to the different desired groups.the result variable has as many modalities as there are groups.to create a group, Simply use the syntax Relating to items selections and or the extended selection of modalities/details.

### Syntax: & nbsp;

Q01.grpmod (Keys)

Or

\ _Grpmod (Q01; Keys)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|& nbsp;|Keys |List of values ​​|List of & nbsp;Elements to be treated |Compulsory |


#### Remarks :

Grpmod and Selmod are very close to \!In reality, the only difference comes from the default behavior when an argument corresponds to a list of items: GRPMOD creates a subtotal and Selmod in list the detail.

The GRPCOL and GRPROW functions work exactly on the same mode, but the first applies to the "columns" dimension and the second to the "line" dimension of the source variable.

In the Case of A Logical Variable, 0 Creates an Empty Modality While in the Case of A continuous variable, 0 selects code 0 well.

### EXAMPLES:

S1.GRPMOD (1 2; 1; 2; -1)

CREATES A NEW VARIABLE WHOSE MODALITIES ARE:

\- The Grouping of Terms 1 and 2 of S1

\- The first modality of S1

\- The second modality of S1 & Nbsp;

\- The Last of S1.

& nbsp;

S1.GRPMOD (1 2; 1; 2; $ o)

CREATES A NEW VARIABLE WHOSE MODALITIES ARE:

\- The grouping of terms 1 and 2 of S1

\- The First Modality of S1

\- The second modality of S1 & nbsp;

\- The non-cited modalities

& nbsp;

## S1.grpmod (1; ~ 1)

CREATES A NEW VARIABLE WHOSE MODALITIES ARE:

\- The Selection of Modality 1 of S1

\- The Selection of the Complement of Modality 1 of S1, on the basis of S1 respondent

& nbsp;

See also: & nbsp;

[Treat the Logical Variables (Modalities)] (<trelligableslogicalsmoda1.md>)

[Management dimensions] (<reurlesdimensesdesdesdairaible1.md>)

& nbsp;