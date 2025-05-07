# Todate

## Todate Function

The **Todate** Function Builds A Variable Tempral (Date/Hour) from a textual or continuous variable (Number of Days since 1/1/1900).

If the variable is textual, a list of reading masks must be indicated.

& nbsp;

** Be Careful, a Date variable date Should not be used directly in a table, it must be converted to the prequaler by apply for example the dtot function ().**

& nbsp;

& nbsp;

Arguments & nbsp;

The list of arguments corresponds to the different possible reading masks.

A MASK DESCRIBES The Date/Time to Read in the Form of A Character String Composed of the Following Characters:

& nbsp;

| Y | Year |
| --- | --- |
| M | MONTH |
| D | Days |
| H | hours |
| M | minutes |
| S | Seconds |
| F | Second fractions |

& nbsp;

Please note \! In the expression of the format, the breakage is important: respect the capital letters and the tiny \!

& nbsp;

Return Value

A temporal variable whose dates correspond to the deconing of the literal variable according to the different formats listed.

The values ​​that do not correspond to a format will be in place.

### Syntax: & nbsp;

Q01.Todate (Formats; Formatdeplimer; Defaultvalue)

Gold

\ _Todate (Q01; Formats; FormatDepLimer; Defaultvalue)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Formats | Character Chain | Reading Format | Different by Default |
| &#50; | Formatdeplimer | Character Chain | Separator | Different by Default |
| &#51; | DEFAULTVALUE | Character chain | Value of free reprieve | Different by Default |

### EXAMPLES:

Dates.Todate ("D/M/Yyyy")

Decodes The Literal Variable Dates and Reads the Days, Months and Years for Seizures Such As 12/1/2016 and 12/11/2016.

& nbsp;

Datec.todate ()

Decodes the continuous variable Datec & nbsp;

& nbsp;

Times.Todate ("Yyyy-MM-DD HH: MM: SS, FFF")

Decods the Times Literal Variable and Reads the Years, The Months, The Days, The Hours, The minutes, the Seconds and the Fraction of Seconds as encourage in "2016-11-29 16: 49: 52.531".

& nbsp;

See also: [Manipulate the temporal and duration variables] (<manipulativevariablestemporelle1.md>)