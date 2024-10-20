import pandas as pd

#Loading a csv file.
data_csv = pd.read_csv("percent-bachelors-degrees-women-usa.csv")

# print(data_csv.head(50))
# print(data_csv.tail(50))
# print(data_csv.info())


data_csv.dropna # to drop missing values
data_csv.drop_duplicates # to drop duplicates

#example

# print(data_csv)
# print(data_csv.drop_duplicates)

# print(data_csv.loc["X"]) # X -> the specific row number can also be used to search for specific columns in the db




