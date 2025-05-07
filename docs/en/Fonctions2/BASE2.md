# BASE

## Function base

The Function **Base** Filter (Puts to "Without Response") respondent of the Variable by Applying Validity Conditions and Adds a Modality Made Up of Individuals Remaining in No Response Application of the Filter.thus Making It Possible to make the Difference Between the individuals not concerned.

### Syntax: & nbsp;

Q01.Base (Filter; Text)

Gold

\ _Base (Q01; Filter; Text)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Filter | Universe | Universe Application | Compulsory |
| &#50; | Text | Character Chain | Optional: label to use & nbsp; preceded by @Code if we want to impose code on the new modality (to be oating during multilingual treatments \!) | & Nbsp; |


#### Examples:

S4.base (s3.selmod (1); "@99 the real SR")

The variable obtained is in all respects similar to the variable S4.But its data is filtered according to the respondents to S3.Selmod (1) and the remaining Modality of the remaining response is added with the "Real SR" label and is affected by code 99.

#### Remarks :

It is the equivalent of the definition & nbsp;::

S4.Noresp (99; "Les Ré Reir Sr"). FLT (S3.Selmod (1))

& nbsp;

The Basic Function () Applied to Variables of the Logical, continuous or literal type.& Nbsp;

& nbsp;

& nbsp;

See also: & nbsp;

[Universe of Variables] (<UniverscibleSetSous-Populations.md>)

[Combination the variables] (<combination thevariables1.md>)