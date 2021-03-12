### Pandas Series

- It is a way to represent a column of data as if you are looking at a table. There is one major concept associated with a series which is the called the index.

The index basically refers to a single element in the series. It is not that different from a list or a dictionary when it comes to an index, but it is a number and if you stack a bunch of these series together, you'd end up referring to a row of data using the index.

#### Useful Methods 

```python
.value_counts()
.describe()
.mean()
.sum()
```

Another useful feature related to Series objects is the ability to convert back into a normal Python object: list, dictionary.

An example would be if we want to store the value counts as a dictionary.

```python
names_as_series = pd.Series(names_list)

names_as_series.value_counts().to_dict()
```

#### File Handling

Series objects are also capable of being able to become files of various extensions. One example could be storing the names column into a .txt file.

One caveat is that .txt files can be generated using .to_csv() instead of .to_txt() since the real difference is the idea that .txt files can have any kind of separator between values whereas CSVs are only separated by commas.

```python
names_list = ['Binu' for i in range(50)] + ['Alex' for i in range(30)] + ['Rishov' for i in range(15)]

names_as_series = pd.Series(names_list)

names_as_series.value_counts().to_dict()

names_as_series.to_csv("data/our_names.txt")
```
