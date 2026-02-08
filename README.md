# IPFpy
Iterative proportionial fitting that can work with larger than memory tables.

inputs tables can be either pandas dataframes, .csv file or .parquet file

```
  input: table
      Thif table lists all the cells or units in a table whose value will be adjusted by Iterative proportional fitting along with boundaries whose adjusted value is meant to stay within.
      unit_id    : identifier for the decision variables
      weight     : decision variables. >=0
      lb	     : weight >= lb
      ub	     : weight <= up

  constraints : table
      This table maps for each constaint identifier, which unit_id to aggregate
      unit_id   : identifier for the decision variables
      cons_id   : identifiant des contraintes

  targets : table
      This table lists all the target values that the margins should add up to once adjusted
      cons_id   : identifiant des contraintes
      cons_type	: constraint must be greater or equal (ge) the target, lesser or equal (le), or equal (eq)
      target    : value for the constaint
  
  unit_id : name of the column that identifies each value to be adjusted (default "unit_id")
  var     : name of the column that contains the value to be adjusted    (default "weight")
  cons_id : name of the column that identifies each constraints          (default "cons_id")
                        
  db_file (optional ): name of the database file on disc that will hold the temporary tables. Default is in memory

  out_parquet (optional): name path of the parquet output file
  out_csv (optional)    : name path of the csv output file

  silent (optinal default false): Whether or not to print progress to screen
  
  output : table
      Output table lists all the initials cells/units along with their adjusted values.
      untiId    : identifier for the decision variables
      weight    : adjusted weight. Will fit in the interval lb <=	weight <= ub

```
  
## Example

```python
from ipfpy import *
import numpy as np


# test IPF
#step1 - create a table and generate the margins as well as the file that maps the cells of the inner table to the margins
raw_table = generate_random_table(4,8,scale=2)
input_table, margins, constraints = aggregate_table(raw_table, by=[0,1,2,3], var="value")
margins = margins.rename(columns={"value":"target"}) #rename margin column

# step2 - modify the margins by adding noise to the inner cells
new_table = input_table.copy().drop("unit_id",axis=1)
new_table["value"] =  input_table["value"] + np.random.uniform(-1, 1, input_table.shape[0])
modified_table, modified_margins, constraints = aggregate_table(new_table, by=[0,1,2,3], var="value")
modified_margins = modified_margins.rename(columns={"value":"target"})

# write table as csv
input_table.to_csv('input_table.csv', index=False)
constraints.to_csv('constraints.csv', index=False)
modified_margins.to_csv('modified_margins.csv', index=False)


df.to_parquet('my_data.parquet', engine='pyarrow')

# adjust the table in step1 to the margin obtained in step2
adjusted_table = ipf(   input=input_table,
                        constraints=constraints,
                        targets=modified_margins,
                        unit_id="unit_id",
                        var="value",
                        cons_id="cons_id",
                        db_file=None,
                        tol=0.1,
                        maxIter=1000)

# output to a file
ipf(input       =input_table,
    constraints =constraints,
    targets     =modified_margins,
    unit_id     ="unit_id",
    var         ="value",
    cons_id     ="cons_id",
    tol         =0.1,
    maxIter     =1000,
    out_csv     ="adjusted_table.csv",
    silent=True)

# input directly from files
ipf(input       ="/home/deck/Desktop/Programming/IPF/IPF/input_table.csv",
    constraints ="/home/deck/Desktop/Programming/IPF/IPF/constraints.csv",
    targets     ="/home/deck/Desktop/Programming/IPF/IPF/modified_margins.csv",
    unit_id     ="unit_id",
    var         ="value",
    cons_id     ="cons_id",
    tol         =0.1,
    maxIter     =1000,
    out_csv     ="adjusted_table.csv",
    silent=True)

```
