import sqlite3, csv
import pandas as pd 
from utils import check_file_exist

database = 'chad'
table = 'quest'
path_database = f'..\\data\\chadmaster\\{database}.sqlite'



path_csv = '..\\data\\chadmaster\\quest_032913.csv'
conn = sqlite3.connect(path_database)

# csv to sqlite 
# df = pd.read_csv(path_csv, header=0)
# df.to_sql(table, conn, index=False, if_exists='fail') # if exists: do nothing


# sql command 
c = conn.cursor()


## list all tables 
# sql = "SELECT name FROM sqlite_master WHERE type='table';"

### `totaldays` min = 1 (total 131) & max = 737
sql = f"SELECT max(totaldays) FROM {table} "
sql = f"SELECT count(*) FROM {table} WHERE totaldays = 1 "

## how many ```asthma``` = 5021
sql = f"SELECT count(*) FROM {table} WHERE asthma = 'Y' "

## how many ```heartlung``` = 4649 
sql = f"SELECT count(*) FROM {table} WHERE heartlung = 'Y' "

## both `asthma` and `heartlung` = 1298
sql = f"SELECT count(*) FROM {table} WHERE heartlung = 'Y' AND asthma = 'Y' "


c.execute(sql)

results = c.fetchall()
print(results)
     