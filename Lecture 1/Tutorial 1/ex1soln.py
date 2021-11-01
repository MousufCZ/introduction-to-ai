"""
Solutions to INM701/IN3062 Ex 1

@author: jacob
"""

#imports for Q2
import os
import pandas as pd


"""
#Q1

# ====== Multiplication Tables ======
#padded 5 x 5 multiplication square experiment
for i in range(1,6):
    for j in range(1,6):
        print(str(i*j).ljust(4), end="")
    print("Next line>>")

#padded 5 x 5 multiplication square
for i in range(1,6):
    for j in range(1,6):
        print(str(i*j).ljust(3), end="")
    print("")
print('\n')


# ====== Multiplication Table, replace even numbers with 0 ======
# Using mod feature
#as above, but with even numbers replaced by 0
for i in range(1,6):
    for j in range(1,6):
        r = i*j % 2
        if r==0:
            print(str(0).ljust(3), end="")
        else:
            print(str(i*j).ljust(3), end="")
    print("")    

"""


#Q2
#==== Read in the file, store in a DataFrame ====
path = "."
filename_read = os.path.join(path, "iris.csv")

df = pd.read_csv(filename_read)

"""
#print the data
print(df)
"""


"""
# ==== Print rows where petal_w is less than 1.0 (hard coded that this is column 3) ====
for i in df.index:
    if(df.iloc[i,3]<1.0):
        print(df.iloc[i].values)


"""

"""
#==== Sort the data, and print ====
sorted_df = df.sort_values(by='sepal_l', ascending=True)
print(sorted_df)

#==== Write sorted data to .csv file ====
filename_write = os.path.join(path, "sorted_iris.csv")
sorted_df.to_csv(filename_write, index=False)
print("Written to file")

"""

"""
#==== calculate variance ===
#first mean
mean = df['sepal_l'].mean()

#then sum of square of difference to mean
sum=0
for val in df['sepal_l']:
    sum += (mean-val)**2

#divide by the number of values
variance = sum / len(df.index)
print("variance: " + str(variance))

"""