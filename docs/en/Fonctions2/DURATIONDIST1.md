# Durationdist

## Durationdist function

The **Durationdist** function calculates a logical variable which corresponds to the distribution of durations according to imposed sections.

### Syntax: & nbsp;

Q01.Durationdist (unit; step; format)

Gold

\ _Durationdist (Q01; Unit; Step; Format)

& nbsp;

| & nbsp; | name & nbsp; | Type & nbsp; | Description | Note |
| --- | --- | --- | --- | --- |
| &#49; | unit | Character chain | Resolution & nbsp; | Default |
| &#50; | Step | Whole | Not | &#48; by Default |
| &#51; | Format | Character Chain | Display Format in Methods of Modalities | Default |

#### NOIKS:

Unit is a value of the table:

& nbsp;

| Milliseconds | in milliseconds |
| --- | --- |
| Seconds | in Seconds |
| Minutes | in minutes |
| Hours | In Hours |
| Days | In Days |

For more information on the format:

https://docs.microsoft.com/en-us/dotnet/standard/base-types/standard-timespan-format-strings

#### Examples:

Durations.Duddist ("minutes"; 5)

CREATES A LOGICAL VARIABLE WHOSE MODALITIES Are the 5 -Minute Duration Sections, from the Smallest to the Large (5 min, 10 min, etc.).

& nbsp;

See also: & nbsp; [Manipulate the temporal and duration variables] (<manipulatingsvariablestemporelle1.md>)