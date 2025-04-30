# Srtmod

## SRTMOD Function

The Function ** SRTMOD ** Prioritize the Modalities of A Variable On The Basis of Their Workforce.& Nbsp;

The Order of the Methods of the Variable Obtained Therefore Depends On The Data.

### Syntax: & nbsp;

Q01.SRTMOD (ascendant; sortgroups; universe; weight)

Or

\ _SRTMOD (Q01; ascendant; soutegroups; universe; weight)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|&#49;|Ascendant |Boolean |True for an ascending sorting, false (by default) for a downhill sorting.|False by default |
|&#50;|Sortgroups |Boolean |True for a hierarchical sorting (by subtitles \ & subtotals), false for a global sorting.|False by default |
|&#51;|Universe |Variable |Optional universe to use |Different by default |
|&#52;|Weight |Variable |Optional weighting to use |Different by default |

### EXAMPLES:

S1.SRTMOD ()

Returns a variable whose modalities are hierarchical in the decreasing order, in groups and according to raw workforce.

& nbsp;

S1.SRTMOD (True; False; S3 1; Weight)

Returns a variable whose modalities are hierarchical in the growing order, overall, and according to the weighted workforce ('weight'), on the population 's3 1'

& nbsp;

& nbsp;

See also: & nbsp;

[Treat the Logical Variables (Modalities)] (<trelligableslogicalsmoda1.md>)

[Present the variables in the tables] (<pretenderlesvariableables whilestAb1.md>)

[Management dimensions] (<reurlesdimensesdesdesdairaible1.md>)

& nbsp;

& nbsp;