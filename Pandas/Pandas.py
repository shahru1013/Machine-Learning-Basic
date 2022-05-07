import pandas as pd
#load csv data and print
data = pd.read_csv('../Files/addresses.csv')
#print files data info
print(data.info())
#Sort the data files by name ascending
sorted_by_name = data.sort_values(by=["first_name"], ascending=True,inplace=False)
#print datas
print("--------------Original List------------\n\n",data.to_string())
print("--------------Sorted List--------------\n\n",sorted_by_name)