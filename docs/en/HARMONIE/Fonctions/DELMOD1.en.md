# Delmod

## Delmod Function

The ** Delmod ** Function Removes The Methods of A Variable On The Basis of A Threshold Expressed in Number of Individuals.TO Delete Specific Methods (by position or other), Go See Remmod and Hidemod.

### Syntax: & nbsp;

Q01.DELMOD (Value; Generateothers; Weighted)

Or

\ _Delmod (Q01; Value; Generateothers; Weighted)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|&#49;|Threshold |Number |By default 0, minimum staff conservation workforce |&#48;By default |
|&#50;|Generateothers |Boolean |By default no "other" methods, creates an "other" modalities if true |False by default |
|&#51;|Weighted |Variable |Hosting variable name |None default |
|&#52;|Includedthreshold |Boolean |If activated, the methods reaching the threshold are kept.Otherwise they are deleted & nbsp;|False by default |
|&#53;|Divisor (or base) |Name |If defined, the conservation threshold is the percentage of the terms on the basis indicated: & nbsp;"R" for respondents "A" for "i" answers for interviewed "n" for homelessness |None by default, then threshold in number |
|&#54;|Universe |Variable |Name of the universe variable to be used for the calculation of statistics.If empty not univers |None default |

#### NOIKS:

The "other" modality is automatically pinned out therefore excluded from hierarchical sorting (cf. [pinmod] (<pinmod.md>)). & Nbsp;

Delmod is very different from Delcol and Delrow.

& nbsp;

#### Examples:

S1.DELMOD ()

Deletes all empty methods.

& nbsp;

S1.DELMOD (30)

Remove all the methods whose workforce is less than or equal to thirty.

& nbsp;

S1.DELMOD (30; True)

Removes All The Methods Whose Workforce is Less Than or Equal to Thirty and Creates An "Other" subtotal which brings them Together (in Last Modality).

& nbsp;

S1.Delmod (30; True; True)

Removes All the Methods Whose Weight WorkForce is Less Than Thirty and Creates An "Other" Subtotal Which Brings Them Together (in Last Modality) Taking Into Account the Weighting of the Variable.

& nbsp;

S1.DELMOD (30; True; Weight)

Removes all the methods whose weighted workforce is less than thirty and creates an "other" subtotal which brings them together (in last modality) by applying Weight weighting.

& nbsp;

S1.delmod (10; false; none; "r"; none)

Removes all the methods whose gross percentage is less than 10% on the basis of respondents.

& nbsp;

& nbsp;

See also: & nbsp;

[Treat the logical variables (modalities)] (<TrelligableslogicalsModa1.md>)

[Dimensions management] (<GERERLESDIMENSESDESSEDAIRAIBLE1.MD>)