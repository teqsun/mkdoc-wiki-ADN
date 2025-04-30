# Catmod

## Catmod Function

The ** Catmod ** Function Applied An External Grouping Table To A Variable.

& nbsp;

The Name of the Table is indicated by a Character Chain, According to the Principle of [Identifying External Tables.] (<USedablesexternes1.md>)

& nbsp;

This Function Plays a Particular Role Becuse It Allows The Hierarchical Grouping Operations To Be Carried Out On the Methods, Lines or Columns by Analysis of the Content of the External Table, in Excel format.the Definition is Thus Independent of Studies and can be used in successive waves, with updates thatInto Account Automatically in the absence of variable storage.& Nbsp;

The result is always a logical, multi-answer or discreet variable.

& nbsp;

The variable treated is logical.

& nbsp;

### Syntax: & nbsp;

Q01.catmod (Expression table; Field1; Field2)

Gold

\ _Catmod (Q01; Expression table ;; Field1; Field2)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|&#49;|Table Expression |Character chain |Descriptive codes table (Tamod) |Compulsory |
|&#50;|Field1 |Character chain |Name of the column as a starter |Compulsory |
|&#51;|Field2 |Character chain |Output column name |Compulsory |


#### Examples:

Let q1, a logical variable with the modalities that take up Cities of the World (ex: Paris, Lyon, Beijing ...).

The Columns of the Table (Geo.xlsx, Country Tab) Read Follow A Structure of the Type:

& nbsp;

| ** City ** | ** Country ** | ** Region ** |
| --- | --- | --- |
| Paris | France | Europe |
| Lyon | France | Europe |
| Rome | Italy | Europe |
| Alexandria | Egypt | Africa |
| Beijing | China | Asia |


& nbsp;

Q1.Catmod ("Geo.xlsx \! Country"; "City"; "Country")

The result is a logical variable with 4 China, Egypt, France, Italy modalities which are the grouping of Paris + Lyon methods for France, Rome for Italy, Egypt for Alexandria and China for Beijing.

On the SEEX EXAMPLE THE Q1.CATMOD DEFINITION ("GEO.XLSX \! Country"; "City"; "Region") GIVES A VARIABLE With the Africa, Asia and Europe Methods.