# Srtcol

## SRTCOL FUNCTION

The **SRTCOL** function prioritizes the columns of a logical variable on the basis of the workforce of a reference modality.

The Order of the Columns of the Variable Obtained Therefore Dependes On the Data.

### Syntax: & nbsp;

Q01.SRTCOL (Criteria; Ascendant; Universe; Weight)

Gold

\ _SRTCOL (Q01; CRITERIA; Ascendant; Universe; Weight)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Criteria | Value | Reference Modality Number or Operator on continues | &#49; by Default |
| &#50; | Ascendant | Boolean | True for an Ascending Sorting, False (by Default) for a Downhill Sorting. | False by Default |
| &#51; | Universe | Variable | Optional Universe to Use | Different by Default |
| &#52; | Weight | Variable | Optional Weighting to Use | Different by Default |

### EXAMPLES:

S1.SRTCOL (1; True; S3 1; Weight)

Returns a variable whose columns are hierarchical in the growing order according to the weighted workforce ('weight') on the population 's3 1' of the 1st modality.

& nbsp;

#### NOIKS:

The SRTCOL Function Supports Continuous Variables, in this case the Criterion is [The Reduction Operator] (<rades1.md>) Associated:

Q1.SRTCOL ("Mean"; True) [discounts] (<Reductions1.md>)

& nbsp;

See also: [Management dimensions] (<GERERLESDIMENSESDESSEVARIAIA1.MD>)