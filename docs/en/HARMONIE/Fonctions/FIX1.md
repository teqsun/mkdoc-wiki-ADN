# Fix

## Fix function

The **Fix** Function "Repair" A Variable by Modifying the Responses of Its responding to a universe of Application.& Nbsp;

### Syntax: & nbsp;

Q01.fix (universe; newvalue; appendmode)

Or

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

### EXAMPLES:

S1.Fix (S2 \> 80; 5)

The variable obtained is in all respects similar to the variable S1.But respondents to S2 \> 80 are automatically assigned response 5 (to S1).

& nbsp;

S1.Fix (S2 \> 80; 6; false; "@99 nc")

The variable obtained is in all respects similar to the variable S1.But the respondents to S2 \> 80 are automatically allocated the answer 6 (to the S1) which will be worded "NC" and whose associated code is 99.

& nbsp;

S6.fix (S2 \> 80; 5; True)

The variable obtained is in all respects similar to the variable S6.But respondents to S2 \> 80 are automatically increased by response 5 (to the S6).

& nbsp;

S6.fix (S2 \> 80; 5; False)

The variable obtained is in all respects similar to the variable s6.But respondent to S2 \> 80 are automatically allocated (even if it means deleting the other ANSWERS CITED by these individuals) Answer 5 (at S6).

& nbsp;

& nbsp;

Variable nubility \!

& nbsp;

In our dummy study,

Husband represents marital status (the first modality is "married")

Country represents the country of origin (the first modality is "France")

Age Represents Age in Clear

Sex represents the Gender of the Interviewee (Man, Woman)

& nbsp;

The problem:

& nbsp;

In France, women can get married from their 13 years when boys must wait until their 15 years.

In our dummy investigation, it turns out that at 14 -Year -OLD Boy declares that he is married ... no doubt a youthful error.

How to solve this thorny problem and clean the Mari variable?

& nbsp;

One Solution:

& nbsp;

Husband (\ _ univ (country 1; sex 1; age \ <15); na)

Returns a "clean" Husband variable in which french boys whose age is strictly less than 15 are assigned to without respondent.

& nbsp;

See also: & nbsp;

[Combination the variables] (<combination thevariables1.md>)

[Temporary variables] (<variablestemporanesshis1.md>)

[Repair a variable under conditions] (<If.md>)