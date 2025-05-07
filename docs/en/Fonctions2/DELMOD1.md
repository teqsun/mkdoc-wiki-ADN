# Delmod

## Delmod Function

The **Delmod** function removes the methods of a variable on the basis of a threshold expressed in number of individuals.To delete specific methods (by position or other), go see Remmod and Hidemod.

### Syntax: & nbsp;

Q01.DELMOD (Value; Generateothers; Weighted)

Gold

\ _Delmod (Q01; Value; Generateothers; Weighted)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Threshold | Number | by Default 0, minimum staff conservation workforce | &#48; by Default |
| &#50; | Generateothers | Boolean | by Default No "Other" Methods, Creates an "Other" Modalities If True | False by Default |
| &#51; | Weighted | Variable | Variable Hosting Name | None Default |
| &#52; | Includedthreshold | Boolean | If Activated, The Methods Reaching the Threshold Are Kept.otherwise they are Deleted & Nbsp; | False by Default |
| &#53; | Divisor (OR Base) | Name | If Defined, The Conservation Threshold is the Percentage of the Terms On The Basis Indicated: & Nbsp; "R" for respondent "a" for "I" Answers for Interview "N" for Homelessness | None by Default, then Threshold in Number |
| &#54; | Universe | Variable | Name of the Universe Variable to be for the Calculation of Statistics.if Empty Not Universe | None Default |

#### NOIKS:

The "other" modality is automatically pinned out there excluded from hierarchical outing (cf. [pinmod] (<pinmod.md>)).& Nbsp;

Delmod is very different from Delcol and Delrow.

& nbsp;

### EXAMPLES:

S1.DELMOD ()

Deletes all empty methods.

& nbsp;

S1.DELMOD (30)

Remove All The Mosets Whose Workforce is less Than or Equal to Thirty.

& nbsp;

S1.DELMOD (30; True)

Removes All The Methods Whose Workforce is Less Than or Equal to Thirty and Creates An "Other" subtotal which brings them Together (in Last Modality).

& nbsp;

S1.Delmod (30; True; True)

Removes all the methods whose weighted workforce is less than thirty and creates an "other" subtotal which brings them together (in last modality) taking into account the weighting of the variable.

& nbsp;

S1.DELMOD (30; True; Weight)

Removes all the methods whose weighted workforce is less than thirty and creates an "other" subtotal which brings them together (in last modality) by applying Weight weighting.

& nbsp;

S1.delmod (10; false; none; "r"; none)

Removes All The Methods Whose Gross Percentage is less Than 10% on the basis of respondent.

& nbsp;

& nbsp;

See also: & nbsp;

[Treat the Logical Variables (Modalities)] (<trelligableslogicalsmoda1.md>)

[Management dimensions] (<reurlesdimensesdesdesdairaible1.md>)