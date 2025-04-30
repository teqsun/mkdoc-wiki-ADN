# Srtcol

## SRTCOL FUNCTION

The ** SRTCOL ** function prioritizes the columns of a logical variable on the basis of the workforce of a reference modality.

The Order of the Columns of the Variable Obtained Therefore Dependes On the Data.

### Syntax: & nbsp;

Q01.SRTCOL (Criteria; Ascendant; Universe; Weight)

Gold

\ _SRTCOL (Q01; CRITERIA; Ascendant; Universe; Weight)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|&#49;|Criteria |Value |Reference modality number or operator on continuous |&#49;By default |
|&#50;|Ascendant |Boolean |True for an ascending sorting, false (by default) for a downhill sorting.|False by default |
|&#51;|Universe |Variable |Optional universe to use |Different by default |
|&#52;|Weight |Variable |Optional weighting to use |Different by default |


#### Examples:

S1.SRTCOL (1; True; S3 1; Weight)

Returns a variable whose columns are hierarchical in the growing order according to the weighted workforce ('weight') on the population 's3 1' of the 1st modality.

& nbsp;

#### Remarks :

The SRTCOL function supports continuous variables, in this case the criterion is [the reduction operator] (<drades1.md>) Associated:

Q1.SRTCOL ("Mean"; True) [discounts] (<Reductions1.md>)

& nbsp;

See also: [Dimensions management] (<GERERLESDIMENSESDESSEVARIABLE1.MD>)