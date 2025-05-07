# Rankcol

## Rankcol Function

The **Rank Col** Function Determines, for Each Individual, The Rank of Each Detail (Column) of his Responses to a Dimensioned Cotinue Variable.

### Syntax: & nbsp;

Q01.RANKCOL (descendant; rankingmode)

Gold

\ _RANKCOL (Q01; descendant; rankingmode)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Descendant | Boolean | False (by Default) for an ascending outing, false for a descending outing. | Compulsory |
| &#50; | Rankingmode | Character Chain | Management of ex aequo & nbsp; **Standard** (Defect): The ex eaquo Receive the minimum rack possible among their racks.for \ [10, 10, 5, 7, 15, 15 \], we Get \ [3, 3, 1, 5, 5, 5, 5, 5, 5, 5, 5The ex eaquo receives the same rank, May there are "holes" in the seacnce of the rows.for \ [10, 10, 5, 7, 15, 15 \], we get \ [3, 3, 1, 2, 4, 4 \] **Maximum**: The ex eaquo receive the maximum possible rank.it is the opposite of the standard mode.for \ [1015, 15 \], we get \ [4, 4, 1, 2, 6, 6 \] | & nbsp; |

### EXAMPLES:

Q01.RANKCOL ()

Returns a continuous variable dimensioned containing the ranks of the responsibilities in the descending order of q01 for each individual.

& nbsp;

#### NOIKS:

Equivalent to the ID INPUT Collar Function.