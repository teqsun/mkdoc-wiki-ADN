# Fix

## Fix Function

The **Fix** Function "Repair" A Variable by Modifying the Responses of Its responding to a universe of Application.& Nbsp;

### Syntax: & nbsp;

Q01.fix (universe; newvalue; appendmode)

Gold

\ _Fix (variable; universe; newvalue; appendmode)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Variable | Variable | All Types | Compulsory |
| &#50; | Universe | Variable | Universe of Application (A variable or A Construction) | Compulsory |
| &#51; | NewValue | Value | Response to affect (Modality Number or Numerical Value Depending On the Nature of The Original Variable Or A Variable) & Nbsp; | Compulsory |
| &#52; | appendmode | Boolean | Default Replacements, If True Adds the New Value | False by Default |
| &#53; | Text insertion | Chain | Label of the new modality created previous


& nbsp;

#### Examples:

S1.Fix (S2 \> 80; 5)

The variable obtained is in all respects similar to the variable S1.But respondent to S2 \> 80 are automatically assigned responsibility (to S1).

& nbsp;

S1.Fix (S2 \> 80; 6; false; "@99 nc")

The Variable Obtained is in All Respects Similar To The Variable S1.But The respondent to S2 \> 80 Are Automatically Allocated the Answer 6 (To the S1) Which Will Be Worded "NC" and Whose Associated Code is 99.

& nbsp;

S6.fix (S2 \> 80; 5; True)

The variable obtained is in all respects similar to the variable s6.But respondent to S2 \> 80 are automatically increased by Response 5 (to the S6).

& nbsp;

S6.fix (S2 \> 80; 5; False)

The variable obtained is in all respects similar to the variable s6.But respondent to S2 \> 80 are automatically allocated (even if it means deleting the other ANSWERS CITED by these individuals) Answer 5 (at S6).

& nbsp;

& nbsp;

Variable nubility \!

& nbsp;

In Our Dummy Study,

Husband represents Marital Status (The First Modality is "Married")

Country represents The Country of Origin (The First Modality is "France")

Age Represents Age in Clear

Sex represents the Gender of the Interviewee (Man, Woman)

& nbsp;

The problem:

& nbsp;

In France, Women can get married from their 13 Years When Boys Must Wait Until Their 15 Years.

In our dummy investigation, it turns out that at 14 -Year -OLD Boy declares that he is married ... no doubt a youthful error.

How to solve this thorny problem and clean the Mari variable?

& nbsp;

One Solution:

& nbsp;

Husband (\ _ Univ (Country 1; Sex 1; Age \ <15); na)

Returns a "clean" Husband variable in which french boys whose age is strictly less than 15 are assigned to without respondent.

& nbsp;

See also: & nbsp;

[Combine the variables] (<combine thevariables1.md>)

[Variable temporary] (<variablestemporanesshis1.md>)

[Repair has variable under conditions] (<If.md>)