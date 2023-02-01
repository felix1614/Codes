from collections import defaultdict
from itertools import groupby

import pandas as pd
import re
df = pd.read_csv("PokemonData.csv")
head = df.head(3)     # read top rows
tail = df.tail(3)     # read bottom rows
Indexing = df["Name"]     # takes name column and index
Indexing_1 = df[["Name", "HP"]]     # takes multiple columns with index
Indexing_2 = df[["Name", "HP"]][0:5]     # takes multiple columns and slicing also can be done
loc = df.iloc[1]    # read the specific row
loc_mul = df.iloc[1:4]  # to read the multiple rows using slicing
specific_loc = df.iloc[2, 1]    # to read a specific cell(loc) [Row, Col]
iterating_rows = [row["Name"] for ind, row in df.iterrows()]    # to iterate through rows
conditionalFilter = df.loc[df["Legendary"] == True]     # to filter the specific rows which satisfies the cond.
stat = df.describe()    # gives the stats like count, mean, percentage, std, min, max
sorting = df.sort_values("Name", ascending=True)    # sort the based on the col given
mUlSort = df.sort_values(["Type1", "HP"], ascending=[0, 1])    # to sort multiple cols here :-> 0 => descending, 1 => ascending
"""
Add a new column/row with a name as Total which would have values of the sum of given fields
[:, 4:10]    : ==> takes all the rows , 4:10 ==> index of col from 4:10
df.columns.get('HP')    :==> takes the index of a given vol
"""
df["Total"] = df.iloc[:, df.columns.get_loc("HP"):df.columns.get_loc("Generation")].sum(axis=1)
dropCol = df.drop(columns=["Total"])
cols = list(df.columns)   # returns the columns name
df = df[cols[0:4] + [cols[-1]] + cols[4:-1]]

"""
FILTER
& ==> and, | ==> or 
() ==> mandatory [for multiple conditions]
"""
filterDf = df.loc[(df["Type1"] == "Grass") & (df["Type2"] == "Poison")]
filterByName = df.loc[df['Type1'].str.contains('fire|grass', flags=re.I, regex=True)]   # filter by name using regex, | ==> or, re.I ==> IgnoreCase

"""
Replace Value
"""
df.loc[df["Type1"] == "Fire", "Type1"] = "Flamer"
df.loc[df["Type1"] == "Flamer", ["Type1", "Type2"]] = "Fire"    # to replace value for multiple columns
df.loc[df["Type1"] == "Fire", ["Type1", "Type2"]] = ["Fire", "Flamer"]    # to replace value for multiple columns with different val

df2 = df.groupby(['Type1']).mean().sort_values('Defense', ascending=False)   # groupBy type and taking the mean(avg)

"""
To filter the null values from df
"""
nan_indices = df.isnull().stack()
nan_indices = nan_indices[nan_indices].index.tolist()

dfd = {k: list(map(lambda x: x[0], g)) for k, g in groupby(sorted(nan_indices, key=lambda x: x[1]), key=lambda x: x[1])}
# dfd = {column: [index for index, col in nan_indices if col == column] for column in set([col for index, col in nan_indices])}
print(df)





