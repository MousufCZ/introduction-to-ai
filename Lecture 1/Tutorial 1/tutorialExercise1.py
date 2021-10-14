import os
import pandas as pd
import numpy as np

path = "."


filename_read = os.path.join(path, "auto-mpg.csv")
df = pd.read_csv(filename_read, na_values=['NA','?'])


"""
# === Dropping fields ===


"""

print(f"Before drop: {df.columns}")
df.drop('name', 1, inplace=True)
print(f"After drop: {df.columns}")


# === Saving a dataframe ===
"""

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
