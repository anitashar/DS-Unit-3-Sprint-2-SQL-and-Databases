
import sqlite3 as sq
import os
import pandas as pd


df = pd.read_csv('./data/buddymove_holidayiq.csv')

conn = sq.connect('buddymove_holidayiq.sqlite3')
df.to_sql('buddymov_holiday', conn, if_exists = 'replace')
#df.to_sql('buddymove_holiday', conn)

curs = conn.cursor()



 #how many rows do I have?
query = """
SELECT count(distinct "User Id") as user_count
FROM buddymove_holiday"""

result = curs.execute(query).fetchall()
print("I have this many rows -", result)

#How many users who reviewed at least 100 `Nature` in the category also
#reviewed at least 100 in the `Shopping` category?

query1 = """SELECT count(DISTINCT "User Id") as user_count
FROM buddymove_holiday as bh 
WHERE bh.Nature >=100 and bh.Shopping >=100"""

result1 = curs.execute(query1).fetchall()
print("this many users reviewed Nature and Shopping category -", result1)