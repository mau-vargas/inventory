import pandas as pd

# Lee un archivo Excel
df = pd.read_excel('doc/inventory.xlsx')

# Muestra las primeras filas del DataFrame
print(df.head())
