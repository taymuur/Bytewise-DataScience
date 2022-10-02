# Creating Table from PDF

```python
# Importing the libraries
import camelot as cm
import seaborn as sns
from matplotlib import pyplot as plt

# Reading PDF files
tables = cm.read_pdf("india_factsheet_economic_n_hdi.pdf", flavor='lattice', pages='1,2')

# Slicing a table
df = tables[2].df.loc[11:14]

# Reseting table indices
df = df.reset_index(drop = True)

# Naming the columns
df.columns = ["KPI", "2001", "2011"]

# Saving table as csv file
df.to_csv("table_output.csv")

# Saving table as excel file
df.to_excel("table_output.xlsx")

# Unpivot dataframe from wide to long format
df_melted = df.melt('KPI', var_name='year', value_name='percentage')
```

### Visualizing the data
```python
# Creating a bar plot
plt.figure(figsize=(10,6))
sns.barplot(x = "KPI", y = "percentage", hue = "year", data = df_melted);
```






