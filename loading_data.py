import pandas as pd

#Loading a csv file.
data_csv = pd.read_csv("percent-bachelors-degrees-women-usa.csv")
# print(data_csv)

#Loading a txt file.
data_txt = pd.read_csv("students.txt",header=0,sep=",")
# print(data_txt)

#Loading an excel file
data_excel = pd.read_excel("file_name.xslx",sheet_name="sheet_name")
# print(data_excel)

#Loading a json file
data_json = pd.read_json("file.json")
# print(data_json)

#Loading data from a database
import sqlite3
connection_db = sqlite3.connect("database_name.db")

query_1 = 'SELECT col_name FROM table_name'
query_2 = 'SELECT * FROM table_name'

data_sql = pd.read_sql(query_1/query_2,connection_db)



