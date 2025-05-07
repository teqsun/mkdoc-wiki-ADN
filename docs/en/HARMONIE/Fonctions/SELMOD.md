# Selmod

## Selmod or mod Function

The **Selmod** function allows you to select the methods of a variable.The basis of the variable obtained is that of respondents to the remaining methods.

It is also possible to use Selmod on a continuous variable, we proceed by selecting responses (codes).

& nbsp;

The arguments corresponds to the lists of methods to be deleted.each list follows the Syntax Relating to items selections and/or the extended selection of modalities/details.

& nbsp;

The Selcol and Selrow functions operate exactly on the same mode, but the first applies to the "columns" dimension and the second to the "line" dimension of the source variable.

### Syntax: & nbsp;

Q01.Selmod (Keys)

Q01.Mod (Keys)

Gold

\ _Selmod (Q01; Keys)

\ _Mod (Q01; Keys)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|& nbsp;|Keys |List of values ​​|List of selected positions |Compulsory |


#### Remarks :

Grpmod and Selmod are very close to \! In reality, the only different comes from the default behavior when an argument corresponds to a list of items: grpmod creates a subtotal and selmod in list the detail.

In the Case of A Logical Variable, 0 Creates an Empty Modality While in the Case of A continuous variable, 0 selects code 0 well.

& nbsp;

It is possible to use the hooks to extract a modality: q1 \ [1 \] is equivalent to q1.mod (1)

### EXAMPLES:

S1.Selmod (1 to 3 -1)

CREATES A NEW VARIABLE WHOSE MODALITIES ARE:

\- The First Modality of S1

\- The second modality of S1 & Nbsp;

\- The Third Modality of S1 & Nbsp;

\- The last of S1.

& nbsp;

S2.Selmod (20 to 25) Creates a Logical Variable To 6 Modalities Made Up of Answers 20 to 25.

S2.Selmod (20 to 25) .resp () CREATES A FILTER CONSIDERING Individuals Between 20 and 25 years old.

& nbsp;

Usual uses:

& nbsp;

\- Filter Create: S6.Selmod (1) Owners refrigerators

\ - Extract modalities: S6.Selmod (2 3 4 5 6 12) Multimedia equipment - which can also be written s6.selmod (2 to 6 12) & nbsp;

\- Extract and reordinate: S6.Selmod (6 5 4 3 2 12) that can also be written s6.selmod (6 to 2 12)

& nbsp;

Other Uses:

& nbsp;

\- Extract starting from the end:

S6.Selmod (-1): extract the last modality, mountain bike

S6.Selmod (-2 -1): Extract the Last Two Modalities

& nbsp;

\- Extract terms based on the wording, the means of travel:

S6.Selmod ("car"; "mountain bike") or s6.selmod ("car, mountain bike") insensitive to scratch

The two selection modes can be mixed: S6.Selmod (10; "VTT")

To select a wording including a comma like for example "none, nothing": Q1.Selmod ("None? Nothing")

S6.Selmod ("St \*") selects all the methods whose label begins with "St"

\- Less frequent but very practical uses:

Create a new empty modality: S6.Selmod (1 2 0)

Duplicate modalities: S6.Selmod (1 1 2 2)

& nbsp;

& nbsp;

The "none" modality is kept if the option to remove empty methods is activated: S1.Selmod ("None" .Filter (False)) & nbsp;

& nbsp;

\- and the others:

S6.Selmod (1 $ o): 2 Terms, Fridge and Others

S6.Selmod ($ 1 r): 2 Modalities, Fridge and respondent

S6.Selmod ($ 1 n): 2 Modalities, Fridge and SR

S6.Selmod (1 $ I): 2 Modalities, Fridge and Interviewed

S6.Selmod (1; \! 1): 2 modalities, fridge and fridge steps

S6.Selmod ($ r $ m): 14 terms, respondent and all terms

S2.Selmod ($ L; "Others") Moves The "Other" Modality in Last position.

## S2.SelMod (1; ~ 1) Modality extracts 1 and its Complement .. & nbsp;

& nbsp;

& nbsp;

& nbsp;

& nbsp;

See also: & nbsp;

[Treat the logical variables (modalities)] (<TrelligableslogicalsModa1.md>)

Combinations

[Dimensions management] (<GERERLESDIMENSESDESSEDAIRAIBLE1.MD>)

For more complex combinations of modalities: ["Extended" selection of modalities/details] (<selection andModalitesDetai.md>)