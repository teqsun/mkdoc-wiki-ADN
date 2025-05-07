# Banner

## Banner Function

The **Banner** function allows you to bring together several criteria to build a banner (group of several variables).It is a more advanced version of Juxvar.

### Syntax: & nbsp;

\ _Banner (Source; PropertyMask)

& nbsp;

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Source | Selection of Variables | List of Variables Separated by A ";" | Compulsory |
| &#50; | Propertymask | Character Chain | One or more characters (The Options can be combined) | A: ADD the Total Base to Each Source N: Add The Base Without Response To Each Source B: Adds A [Autobase] (<Autobase1.md>) Overall (Useless If a is specific) o: Add a [ordmod(1)] (<ordmod1.md>) on each source q: deletes the digital part of each source & nbsp; |

& nbsp;

### EXAMPLES:

\ _Banner (S1; S3)

The Resulting Variable is, and for each variable the deletion of digital methods, the Ordering of the Authorizing Officer to 1 and Adding the base respondent in the 1st modalities, the Concatenation of S1 and S3.

& nbsp;

\ _Banner (S1; S3; "O")

The Resulting Variable is the Concatenation of S1 and S3 After Passing the Authorizing Officers to 1.

& nbsp;

#### NOIKS:

The Definition \ _Banner (S1; S3) is equivalent to \ _banner (S1; S3; "aoq")

& nbsp;

& nbsp;

See also: & nbsp;

[Juxvar] (<juxvar1.md>)