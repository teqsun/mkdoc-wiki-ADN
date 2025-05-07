# Sys

## SYS FUNCTION

The **Sys** Function Builds A New Variable Whose Value Depends On The System Requested.

& nbsp;

The Function Awaits:

* Level: Name of the Level of Creation (and NB Statistical Units)
* Propertynam: System Property Name

& nbsp;

| Study | Study File Name (Without Extension) |
| --- | --- |
| Study \ _Path | Full Name for Study File |
| Study \ _File | Study File Name (With Extension) |
| Study \ _Folder | Study File Name |
| User | Current User Name (License) |
| User \ _Email | Current User Email (License) |
| NOW | Variable temporal which gives current time, during execution |

### Syntax: & nbsp;

\ _SYS (Level; Propertynama)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| & nbsp; | Propertyname | Character Chain | Recovered Property Name | Compulsory |

### EXAMPLES:

\ _SYS ("units"; "now")

Returns a variable temporal which the current date and time, on the 'units' level.

& nbsp;

See also: & nbsp;

[Creation of Variables (System, Random ...)] (<CreerdesvariablesdoutepiecesS.MD>)