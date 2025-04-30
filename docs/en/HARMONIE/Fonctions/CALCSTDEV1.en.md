# CalcstDev

## Calcstdev function

The function ** CALCSTDEV ** creates a constant digital variable corresponding to the standard deviation of the digital variable indicated in parameter, the second parameter allows you to choose between the standard standard deviation (FALSE) or the estimated standard deviation (TRUE).The default setting being FALSE.

& nbsp;

\ _CalcstDev (varq; false)

### Syntax: & nbsp;

Q01.CALCSTDEV (Useestimatedcalculation; Weight)

Or

\ _CalcstDev (Q01; Useestimatedcalculation; Weight)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Useestimatedcalculation | Boolean | By Default Calculates The Standard Deviation (Divideed by N) | False by Default |
| &#50; | Weight | Variable | Weighting to Apply | Default |


#### Examples:

\ _CalcstDev (note)

Creates a new variable corresponding to the standard standard deviation of the digital variable Note.

& nbsp;

See also: [Manipulate the digital variables] (<manipulatingsnurablesnumerics1.md>)