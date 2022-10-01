# Creating Table from PDF

### Importing the libraries
```python
import camelot as cm
import seaborn as sns
from matplotlib import pyplot as plt
```

### Reading PDF Files
```python
tables = cm.read_pdf("india_factsheet_economic_n_hdi.pdf", flavor='lattice', pages='1,2')
```

### Slicing a table
```python
df = tables[2].df.loc[11:14]
```

### Reseting table indices
```python
df = df.reset_index(drop = True)
```

### Naming the columns
```python
df.columns = ["KPI", "2001", "2011"]
```

### Saving table as CSV file
```python
df.to_csv("table_output.csv")
```

### Saving table as Excel file
```python
df.to_excel("table_output.xlsx")
```

### Unpivot dataframe from wide to long format
```python
df_melted = df.melt('KPI', var_name='year', value_name='percentage')
```

### Creating a bar chart
```python
plt.figure(figsize=(10,6))
sns.barplot(x = "KPI", y = "percentage", hue = "year", data = df_melted);
```






