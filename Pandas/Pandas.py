import pandas as pd
#load csv data and print
data = pd.read_csv('../Files/addresses.csv')
print(data.to_string())