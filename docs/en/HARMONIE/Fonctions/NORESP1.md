# Noresp

## Noresp Function

The **Noresp** function manipulates the homeless of a logical variable by adding them or combining them to an existing modality.Its syntax is equivalent to that of the RESP function.

#### Syntax n ° 1: & nbsp;

Q01.Noresp ()

Gold

\ _Noresp (Q01)

& nbsp;

This undead version simply returns to the uninponsidered with the variable (good method to create a filter / a universe \!).

#### Syntax n ° 2: & nbsp;

Q01.Noresp (insertionpoint; Margintext)

Gold

\ _Noresp (Q01; insertionpoint; Margintext)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|&#49;|INSERTIONPOINT |Number |Insertion position: if it is worth 0, the marginal is added at the top of the variable.If it is larger than the number of modalities, the marginal is added at the end. & Nbsp;If it is between 1 and 2 (1.5 for example), it is inserted between modality 1 and modality 2 (etc.).|Compulsory |
|&#50;|Margintext |Character chain |Optional: Label to use with @Code if you want to assign a code to the new modality (to be avoided during multilingual treatments \!).|Default indefinite |


#### Examples:

S2.Noresp ()

Returns a filter that conveys the homeless with the S2 variable.

& nbsp;

S1.noresp (99; "@99 sr")

Add the without answers to the S1 variable in last mode lelayed "SR" (insofar as the variable S1 at less than 99 modalities ...) and assigns code 99.

& nbsp;

S1.Noresp (0)

Add the homeless to the S1 variable in first modality.

& nbsp;

S1.Noresp (2.5)

Add the Homeless to the S1 Variable Between the 2nd and the 3rd Methods.

& nbsp;

See also: [Criteria] (<Creerdescriteresoubanieres1.md>)