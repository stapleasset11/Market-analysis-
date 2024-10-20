import pandas as pd

data_csv = pd.read_csv("percent-bachelors-degrees-women-usa.csv")

#Sort smallest to largest
print(data_csv.sort_values(by = "Agriculture"))

#sort largest to smallest
print(data_csv.sort_values(by="Agriculture",ascending=False))

#grouping

print('dataframe_name'.groupby("column_name").count())

