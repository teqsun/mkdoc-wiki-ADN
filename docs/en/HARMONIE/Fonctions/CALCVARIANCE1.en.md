# Calcvariance

## Calcvariance Function

The Function ** Calcvariance ** Creates A Constant Digital Variable corresponding to the Variance of the Digital Variable Indicated in Parameter, The Second Parameter Allows You To Choose Between The Standard Variance (False) or the Estimated Variance (True) .The default Setting Being False.

### Syntax: & nbsp;

Q01.Calcvariance (Useestimatedcalculation; Weight)

Or

\ _Calcvariance (Q01; Useestimatedcalculation; Weight)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Useestimatedcalculation | Boolean | by Default Calculates The Variance (Divideed by N) | False by Default |
| &#50; | Weight | Variable | Weighting to Apply | Default |

### EXAMPLES:

\ _Calcvariance (note)

Creates a new variable corresponding to the standard variance of the digital variable note.

& nbsp;

See also: [Manipulate the digital variables] (<manipulatingsnurablesnumerics1.md>)