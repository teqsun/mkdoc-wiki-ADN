# Stat

## Stat Function

The ** Stat ** Function Returns A Digital Variable, Each Individual Receives The % of its quotes.

### Syntax: & nbsp;

Q01.stat (universe; weight; base; factor)

Gold

\ _Stat (Q01; Universe; Weight; Base; Factor)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| & nbsp; | Universe | Variable | Applied Universe | Default |
| & nbsp; | Weight | Variable | Weighting to be Applied (Optional) | Default |
| & nbsp; | Base | Character | Base of % R: Sensors and I: Interview | Exposive if good |
| & nbsp; | factor | Whole |%& nbsp multiply coefficient; &#49;Default |

### EXAMPLES:

Sex.stat () Returns a continuous with the % (ex: 40) of men for men and the % (ex: 60) of women for women

Sex.stat (Univ; Weight) Returns The % Filtered by Univ and Weightd by Weight

Sex.stat (none; none; none) Returns The Raw Workforce.

#### NOIKS:

The dimensioned variables are supported.