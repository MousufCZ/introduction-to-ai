# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 01:08:12 2021
Solutions to INM701/IN3062 Ex 1

@author: mousuf
"""

#imports for Q2
import os
import pandas as pd





#Q2

#read in the file, store in a DataFrame
path = "."
filename_read = os.path.join(path, "iris.csv")

df = pd.read_csv(filename_read)
#print(df)

#print rows where petal_w is less than 1.0 (hard coded that this is column 3)
for i in df.index:
    if(df.iloc[i,3]<1.0):
        print(df.iloc[i].values)
        
        
        
#sort the data, and print
sorted_df = df.sort_values(by='sepal_l', ascending=True)
print(sorted_df)



#write sorted data to .csv file
filename_write = os.path.join(path, "sorted_iris.csv")
sorted_df.to_csv(filename_write, index=False)
print("Written to file")



#calculate variance
#first mean
mean = df['sepal_l'].mean()
print(f"Mean: {[mean]}")


#then sum of square of difference to mean
sum=0
for val in df['sepal_l']:
    sum += (mean-val)**2

print(f"Sum: {[sum]}")



#divide by the number of values
variance = sum / len(df.index)
print("Variance: " + str(variance))

