#ADD each even numbers pair and print by Numpy package
import numpy as np
#Get even numbers array from lists.txt by numpy
fileData = np.loadtxt('./lists.txt', dtype=int)
#iterate through list and add each pair
count  = 0
for each in fileData:
    count+=1
    pairSum = each[0]+each[1]
    print("Sum of pair no",count ,"is =", pairSum)