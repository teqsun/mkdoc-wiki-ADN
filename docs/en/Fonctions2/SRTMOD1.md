# Srtmod

## SRTMOD Function

The Function **SRTMOD** Prioritize the Modalities of A Variable On The Basis of Their Workforce.& Nbsp;

The Order of the Methods of the Variable Obtained Therefore Depends On The Data.

### Syntax: & nbsp;

Q01.SRTMOD (ascendant; sortgroups; universe; weight)

Gold

\ _SRTMOD (Q01; ascendant; soutegroups; universe; weight)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Ascendant | Boolean | True for an Ascending Sorting, False (by Default) for a Downhill Sorting. | False by Default |
| &#50; | Sortigroups | Boolean | True for a hierarchical outing (by subtitles \ & subtotals), false for a global outing. | False by Default |
| &#51; | Universe | Variable | Optional Universe to Use | Different by Default |
| &#52; | Weight | Variable | Optional Weighting to Use | Different by Default |


#### Examples:

S1.SRTMOD ()

Returns a variable whose modalities are hierarchical in the decreasing order, in groups and according to raw workforce.

& nbsp;

S1.SRTMOD (True; False; S3 1; Weight)

Returns a variable whose modalities are hierarchical in the growing order, overall, and according to the weighted workforce ('weight'), on the population 's3 1'

& nbsp;

& nbsp;

See also: & nbsp;

[Treat the Logical Variables (Modalities)] (<trelligableslogicalsmoda1.md>)

[Present the variables in the tables] (<PertERDERLESVARIABLE WHILESTAB1.MD>)

[Management dimensions] (<reurlesdimensesdesdesdairaible1.md>)

& nbsp;

& nbsp;