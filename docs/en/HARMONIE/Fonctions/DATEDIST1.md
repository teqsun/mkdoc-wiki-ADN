# DateDist

## Datedist Function

The **Date Date** Calculates A Logical Variable which corresponds to the Distribution of A temporal variable, According to a given resolution.

& nbsp;

| Year | Year |
| --- | --- |
| MONTH | MONTH |
| Day | Days |
| Weeks | Weeks |
| HOUR | HOURS |
| Minute | minutes |
| Second | Seconds |

### Syntax: & nbsp;

Q01.DATEDIST (Resolution; Format)

Gold

\ _DATEDIST (Q01; Resolution; Format)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Resolution | Character Chain | Doy/Week/Month/Year Resolution | Default |
| &#50; | Format | Character Chain | Used to read the Modalities Created | Default |

#### NOIKS:

The Determines format How to name the Slices.the Simplest is to Leave the Argument Empty.

For more information we possible formats: https://docs.microsoft.com/en-us/dotnet/standard/base-types/standard-date-and-time-format-strings

#### Examples:

Dates.datedist ("month")

CREATES A LOGICAL VARIABLE WHOSE METHODS Are the Monthly Sections of the Smallest Date on the Large Date encouraged with Conservation of Empty Intermediate Values.

& nbsp;

See also: [Manipulate the temporal and duration variables] (<manipulativevariablestemporelle1.md>)