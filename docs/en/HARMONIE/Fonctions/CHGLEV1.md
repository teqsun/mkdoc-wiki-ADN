# CHGLEV

## CHGLEV Function

The **CHGLEV** Function Changes The Level of Response Variable (Home to individuals and vice versa).& Nbsp;

The variable obtained is therefore on the level specified in the first argument.The reduction operator applied during the level change can be indicated in the second argument: Consult the [Table of reduction operators.] (<Reductions1.md>)

### Syntax: & nbsp;

Q01.CHGLEV (Newlevel; AGGREGATOR)

Gold

\ _Chglev (Q01; Newlevel; aggregator)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Newlevel | Character Chain | Target Level Name | Compulsory |
| &#50; | Aggregator | Character Chain | by Default, Or for Logics, Sum for Quantities | Different by Default |


#### Examples:

S2.chglev ("units")

Creates has variable based on the "units" level.

& nbsp;

See also: & nbsp;

[Levels] (<Levels1.md>)

[Discount Operators] (<ractions1.md>)