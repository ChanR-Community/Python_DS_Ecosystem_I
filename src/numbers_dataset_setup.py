import numpy as np
import pandas as pd

X = np.random.randint(0, 1000, (5000, 10))

df = pd.DataFrame(X, columns=[f'column_{i+1}' for i in range(X.shape[1])])

df_2 = pd.DataFrame(3*X, columns=[f'column_{i+1}' for i in range(X.shape[1])])

df_3 = pd.DataFrame(X**2, columns=[f'column_{i+1}' for i in range(X.shape[1])])

merged_df = pd.concat([df, df_2, df_3], axis=0)

merged_df.shape

merged_df.describe()

merged_df.info()

my_df = pd.read_csv("data/our_names.txt", sep=",")

my_df

my_df.drop(my_df.columns.tolist()[0], axis=1, inplace=True)

my_df

merged_df.to_csv("data/random_numbers.csv", index=False)

merged_v2 = pd.read_csv("data/random_numbers.csv")

merged_v2.drop(merged_v2.columns.tolist()[3:8], axis=1)
