# DATE

## Function date

The Function **Date** CREATES A Constant Temporal Variable Whose Components are defined one by one, by the arguments.

The Variable Will Be Created On The Level Specified in the First Argument.

### Syntax:

\ _Date (Levelname; Year; Month; Day; Hour; minute; second; millisecond)

& nbsp;

|& nbsp;|Name & nbsp;|Type & nbsp;|Description |Note |
|--- |--- |--- |--- |--- |
|&#49;|Levelname |Character chain |Target level name |Compulsory |
|&#50;|Year |Whole |Year |&#48;By default |
|&#51;|Month |Whole |Month (from 1 to 12) |&#48;By default |
|&#52;|Day |Whole |Day (from 1 to 31) |&#48;By default |
|&#53;|HOUR |Whole |Time (from 0 to 23) |&#48;By default |
|&#54;|Minute |Whole |Minute (from 0 to 59) |&#48;By default |
|&#55;|Second |Whole |Second (from 9 to 59) |&#48;By default |
|&#56;|Millisecond |Whole |Milliseconds |&#48;By default |


#### Examples:

\ _Date ("Units"; 2020; 3; 17)

& nbsp;

See also: [Manipulate the temporal and duration variables] (<manipulativevariablestemporelle1.md>)