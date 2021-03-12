import pandas as pd

# Series
nums = [i for i in range(1, 101)]
type(nums)

num_as_series = pd.Series(nums)
type(num_as_series)

# Adding all the numbers
num_as_series.sum()

# Getting the mean
num_as_series.mean()

num_as_series.describe()

# The Names List
names_list = ['Binu' for i in range(50)] + ['Alex' for i in range(30)] + ['Rishov' for i in range(15)]

names_as_series = pd.Series(names_list)

names_as_series.value_counts().to_dict()




# Data Frame
