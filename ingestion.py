import pandas as pd

# Write a function that reads a csv file and returns a pandas dataframe
def ingest_data(file_path):
    return pd.read_csv(file_path)

df = ingest_data('data.csv')

# Write a function that returns the first 5 rows of a dataframe
def get_head(df):
    return df.head()

# Write a function that returns the last 5 rows of a dataframe
def get_tail(df):
    return df.tail()

# Write a function that returns the shape of a dataframe
def get_shape(df):
    return df.shape

# Write a function that returns the number of rows and columns of a dataframe
def get_info(df):
    return df.info()
