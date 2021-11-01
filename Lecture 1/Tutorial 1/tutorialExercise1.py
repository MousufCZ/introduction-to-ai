# Read a CSV, manual stats
import codecs
import os
import csv
import math

path = "."

encoding = 'utf-8'
filename_read = os.path.join(path, "auto-mpg.csv")
filename_write = os.path.join(path, "auto-mpg-norm.csv")


"""
# === Pandas statistics implementation ===


c = 0

with codecs.open(filename_read, "r", encoding) as fh:
    reader = csv.reader(fh)
    
    # Generate header index using comprehension.
    # Comprehension is cool, but not necessarily a beginners feature of Python.
    header_idx = {key: value for (value, key) in enumerate(next(reader))}
    headers = header_idx.keys()

    fields = {key: value for (key, value) in [(key, {'count':0, 'sum':0, 'variance':0}) for key in headers]}

    # Pass 1, means
    row_count = 0
    for row in reader:
        row_count += 1
        for name in headers:
            try:
                value = float(row[header_idx[name]])
                field = fields[name]
                field['count'] += 1
                field['sum'] += value
            except ValueError:
                pass
            
            
    # Calculate means, toss sums (part of pass 1)
    for field in fields.values():
        # If 90% are not missing (or non-numeric) calculate a mean
        if (field['count'] / row_count) > 0.9:
            field['mean'] = field['sum'] / field['count']
        else:
            del field['sum']  # Why is this here?
            
            
    # Pass 2, standard deviation & variance
    fh.seek(0)
    for row in reader:
        for name in headers:
            try:
                value = float(row[header_idx[name]])
                field = fields[name]
                # If we failed to calculate a mean, no variance.
                if 'mean' in field:
                    field['variance'] += (value - field['mean'])**2
            except ValueError:
                pass
            
            
       
    # Calculate standard deviation, keep variance (part of pass 2)
    for field in fields.values():
        # If no variance, then no standard deviation
        if 'mean' in field:
            field['variance'] /= field['count']
            field['sdev'] = math.sqrt(field['variance'])
        else:
            del field['variance']
            
            
    # Print summary stats
    for key in sorted(fields.keys()):
        print(f"{key}:{fields[key]}")

"""

"""
# === Key with enumeration ===

# Read a CSV, symbolic headers
import codecs
import os
import csv

path = "."

encoding = 'utf-8'
filename = os.path.join(path, "auto-mpg.csv")

c = 0

with codecs.open(filename, "r", encoding) as fh:
    reader = csv.reader(fh)

    # Generate header index using comprehension.
    # Comprehension is cool, but not necessarily a beginners feature of Python.
    header_idx = {key: value for (value, key) in enumerate(next(reader))}

    for row in reader:
        c += 1
        if c > 5:
            break
        print(f"Car Name: {row[header_idx['name']]}")

"""



"""
# === Accessing Files directly ===
# Read a CSV, symbolic headers
import codecs
import os
import csv

path = "."

# Always specify your encoding! There is no such thing as "its just a text file".
# See... z
# Also see... http://www.utf8everywhere.org/
encoding = 'utf-8'
filename = os.path.join(path, "auto-mpg.csv")

c = 0

with codecs.open(filename, "r", encoding) as fh:
    # Iterate over this line by line...
    for line in fh:
        c += 1 # Only the first 5 lines
        if c > 5:
            break
        print(line.strip())

with codecs.open(filename, "r", encoding) as fh:
    reader = csv.reader(fh)
    for row in reader:
        c += 1
        if c > 5: 
            break
        print(row)


"""




"""
# === Concatenating Rows and Columns ===

col_horsepower = df['horsepower']
col_name = df['name']
col_cylinders = df['cylinders']
result = pd.concat([col_name, col_horsepower, col_cylinders], axis=1)
print(result)


"""

"""
# === Missing Values ===

med = df['horsepower'].median()
df['horsepower'] = df['horsepower'].fillna(med)
# df = df.dropna() # you can also simply drop NA values
print(f"horsepower has na? {pd.isnull(df['horsepower']).values.any()}")


"""

"""
# === Field Transformation & Preprocessing ===

import os
import pandas as pd
import numpy as np
from scipy.stats import zscore

path = "."


filename_read = os.path.join(path, "auto-mpg.csv")
df = pd.read_csv(filename_read, na_values=['NA','?'])
df ['mpg'] = zscore(df['mpg'])
df
print(df[0:50])


"""


"""
# === Calculated Fields ===

df.insert(1, 'weight_kg', (df['weight'] * 0.45359237).astype(int))

print(f"After drop: {df.columns}")
print(df[0:5])


"""

"""
# === Dropping fields ===

print(f"Before drop: {df.columns}")
df.drop('name', 1, inplace=True)
print(f"After drop: {df.columns}")

"""



"""
# === Saving a dataframe ===

filename_write = os.path.join(path, "auto-mpg-shuffle.csv")
df = df.reindex(np.random.permutation(df.index))
df.to_csv(filename_write, index=False)
print("Done copy to new .csv file")
"""


"""
# === Sorting and shuffling ===
df.sort_values(by='name', ascending = True)

print(f"The first car is: {df['name'].iloc[0]}")
print(df[0:5])


np.random.seed(41)
df = df.reindex(np.random.permutation(df.index))
df.reset_index(inplace=True, drop = True)

print(df)
"""


"""
# === Pandas ===
# Strip non-numerics
df = df.select_dtypes(include=['int', 'float'])

headers = list(df.columns.values)
fields = []

for field in headers:
    fields.append({
        # name of the columns
        'name' : field,
        # mean for the whole column
        'mean' : df[field].mean(),
        # the variance
        'var' : df[field].var(),
        # the standard deviation
        'sdev' : df[field].std()
        })


for field in fields:
    print(field)

"""
