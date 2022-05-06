import numpy as np
fileData = np.loadtxt('./lists.txt', dtype=int)
for each in fileData:
    print(each[0], each[1])