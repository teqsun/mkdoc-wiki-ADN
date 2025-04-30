# Selmod

## Selmod or mod Function

The ** Selmod ** Function Allows You To Select The Methods of A Variable.the Basis of the Variable Obtained is that of respondent to the remaining methods.

It is also possible to use selmod on has continued variable, we proceeded by selecting Resorts (codes).

& nbsp;

The arguments corresponds to the lists of methods to be deleted.each list follows the Syntax Relating to items selections and/or the extended selection of modalities/details.

& nbsp;

The Selcol and Selrow Functions Operate Exactly on the Same Mode, but the first apps to the "columns" dimension and the second to the "Line" dimension of the Source Variable.

### Syntax: & nbsp;

Q01.Selmod (Keys)

Q01.Mod (Keys)

Gold

\ _Selmod (Q01; Keys)

\ _Mod (Q01; Keys)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| & nbsp; | Keys | List of Values ​​| List of Selected Positions | Compulsory |

#### NOIKS:

Grpmod and Selmod are very close to \! In reality, the only different comes from the default behavior when an argument corresponds to a list of items: grpmod creates a subtotal and selmod in list the detail.

In the Case of A Logical Variable, 0 Creates an Empty Modality While in the Case of A continuous variable, 0 selects code 0 well.

& nbsp;

It is possible to use the hooks to extract a modality: q1 \ [1 \] is equivalent to q1.mod (1)

### EXAMPLES:

S1.Selmod (1 to 3 -1)

CREATES A NEW VARIABLE WHOSE MODALITIES ARE:

\- The First Modality of S1

\- The second modality of S1 & nbsp;

\- The Third Modality of S1 & Nbsp;

\- The Last of S1.

& nbsp;

S2.Selmod (20 to 25) creates a logical variable to 6 modalities made up of answers 20 to 25.

S2.Selmod (20 to 25) .resp () CREATES A FILTER CONSIDERING Individuals Between 20 and 25 years old.

& nbsp;

Usual uses:

& nbsp;

\- Filter Create: S6.Selmod (1) Owners refrigerators

\ - Extract Modalities: S6.Selmod (2 3 4 5 6 12) Multimedia Equipment - Which can also be written s6.selmod (2 to 6 12) & nbsp;

\- Extract and reordinate: S6.Selmod (6 5 4 3 2 12) that can also be written s6.selmod (6 to 2 12)

& nbsp;

Other Uses:

& nbsp;

\- Extract starting from the end:

S6.Selmod (-1): Extract the Last Modality, Mountain Bike

S6.Selmod (-2 -1): Extract the Last Two Modalities

& nbsp;

\- Extract Terms Based on the Wording, The Means of Travel:

S6.Selmod ("Car"; "Mountain Bike") or S6.Selmod ("Car, Mountain Bike") insensitive to scratch

The Two Selection modes can be mixed: s6.selmod (10; "mountain bike")

To select a wording include a order like for examples "nun, Nothing": Q1.Selmod ("None? Nothing")

S6.Selmod ("St \*") selects all the method Whose Label Begins with "St"

\- LESS FREQUENT but very PRACTICAL USES:

CREATE A NEW EMPTY MODALITY: S6.SELMOD (1 2 0)

Duplicate Modalities: S6.Selmod (1 1 2 2)

& nbsp;

& nbsp;

The "none" modality is kept if the option to remove empty methods is activated: s1.selmod ("none" .Filter (false)) & nbsp;

& nbsp;

\- And the Others:

S6.Selmod (1 $ o): 2 Terms, Fridge and Others

S6.Selmod ($ 1 r): 2 Modalities, Fridge and respondent

S6.Selmod ($ 1 n): 2 Modalities, Fridge and SR

S6.Selmod (1 $ I): 2 Modalities, Fridge and Interviewed

S6.Selmod (1; \! 1): 2 Modalities, Fridge and Fridge Steps

S6.Selmod ($ r $ m): 14 terms, respondent and all terms

S2.Selmod ($ L; "Others") Moves The "Other" Modality in Last position.

## S2.Selmod (1; ~ 1) Extracts modality 1 and its complement .. & nbsp;

& nbsp;

& nbsp;

& nbsp;

& nbsp;

See also: & nbsp;

[Treat the Logical Variables (Modalities)] (<trelligableslogicalsmoda1.md>)

Combinations

[Management dimensions] (<reurlesdimensesdesdesdairaible1.md>)

For more Complex Combinations of Modalities: ["Extended" selection of Modalities/Details] (<selection andmodalitesdetai.md>)