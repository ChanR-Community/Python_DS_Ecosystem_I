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

names_as_series.to_csv("data/our_names.txt")

# Getting the numbers above 70 in the num_as_series
num_as_series[num_as_series >= 70].shape

num_as_series > 70

# Data Frames
data_dict = {'names': ['Binu', 'Alex', 'Rishov'], 'workshops_attended': [6, 8, 10]}

data_dict['random_nums'] = my_col

data_dict.keys()

df = pd.DataFrame(data_dict)

df

type(df['names'])
type(df['workshops_attended'])

type(df.iloc[0])


df.iloc[1:]

df.iloc[:-1]

my_col = [30, 40, 50]

df['random_nums'] = my_col

df

df.columns.tolist()

df['names'].tolist()

df[['workshops_attended', 'random_nums']]

df[df.columns.tolist()[1:]]

df[df['names'] == 'Binu']

# AND
new_df = df[(df['workshops_attended'] > 6) & (df['random_nums'] <= 40)]
new_df

# OR
df[(df['workshops_attended'] > 6) | (df['random_nums'] <= 40)]
