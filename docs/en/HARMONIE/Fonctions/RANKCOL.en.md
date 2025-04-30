# Rankcol

## Rankcol function

The ** RANKCOL ** function determines, for each indivdu, the rank of each detail (column) of its responses to a cotinue variable dimensioned.

### Syntax: & nbsp;

Q01.RANKCOL (descendant; rankingmode)

Or

\ _RANKCOL (Q01; descendant; rankingmode)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|&#49;|Descendant |Boolean |False (by default) for an ascending sorting, false for a descending sorting.|Compulsory |
|&#50;|Rankingmode |Character chain |Management of ex aequo & nbsp;** Standard ** (defect): The ex EAQUO receive the minimum rank possible among their possible ranks.For \ [10, 10, 5, 7, 15, 15 \], we get \ [3, 3, 1, 2, 5, 5 \] ** dense ** & nbsp;: The ex EAQUO receive the same rank, May there are "holes" in the seacnce of the rows.For \ [10, 10, 5, 7, 15, 15 \], we get \ [3, 3, 1, 2, 4, 4 \] ** Maximum **: The ex EAQUO receive the maximum possible rank.It is the opposite of the standard mode.For \ [10, 10, 5, 7, 15, 15 \], we get \ [4, 4, 1, 2, 6, 6 \] |& nbsp;|


#### Examples:

Q01.RANKCOL ()

Returns a continuous variable dimensioned containing the ranks of the responses in the descending order of Q01 for each individual.

& nbsp;

#### NOIKS:

Equivalent to the IDXCOL function of Daisie.