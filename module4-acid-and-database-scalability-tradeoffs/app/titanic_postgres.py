
# imports
import os
from dotenv import load_dotenv
import psycopg2

#> loads contents of the .env file into the script's environment
load_dotenv() 


# getting env variables
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")



### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname= DB_NAME, user= DB_USER, password= DB_PASSWORD, host= DB_HOST)
print(type(conn))
### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()
print(type(cur))
# ### An example query
# query = """
# SELECT * from passengers;
# """
# cur.execute(query)
# ### Note - nothing happened yet! We need to actually *fetch* from the cursor
# results = cur.fetchall()
# print("-------------------------")
# print ("id survived pclass name gender age")
# for col in results:
#   print(col[0],col[1],col[2],col[3],col[4],col[5],col[6],col[7])


# How many passengers survived, and 
query1 = """
select count(*) as survived_count
from passengers
where survived = 1
"""
cur.execute(query1)
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result1 = cur.fetchall()
print("-------------------------")
print("RESULTS FOR How many passengers survived")
print(result1)


# how many passengers died?
query1 = """
SELECT count(*)
from passengers
where survived = 0
"""
cur.execute(query1)
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result1 = cur.fetchall()
print("-------------------------")
print("RESULTS FOR How many passengers died")
print(result1)

# How many passengers were in each class?
query1 = """
SELECT pclass,sum(sib_spouse_count + parent_child_count+1) as total_count
FROM passengers
GROUP BY pclass
ORDER BY pclass
"""

cur.execute(query1)
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result1 = cur.fetchall()
print("-------------------------")
print("RESULTS FOR count of passengers in each class")
print(result1)

# How many passengers survived within each class?
query1 = """
SELECT pclass, count(id) as num_of_sur
FROM passengers
WHERE survived = 1
GROUP BY pclass
ORDER BY pclass;
"""

cur.execute(query1)
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result1 = cur.fetchall()
print("-------------------------")
print("RESULTS FOR count of passengers survived in each class")
print(result1)

# How many passengers died within each class?
query1 = """
SELECT pclass,count(id) as num_of_died
FROM passengers
WHERE survived = 0
GROUP BY pclass
ORDER BY pclass
"""

cur.execute(query1)
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result1 = cur.fetchall()
print("-------------------------")
print("RESULTS FOR count of passengers died in each class")
print(result1)

# What was the average age of survivors vs nonsurvivors?
query1 = """
select  ROUND(avg(age)) as avg_age_of_survivors, 
		(SELECT ROUND(avg(age)) as avg_age_of_non_survivors FROM passengers where survived = 0)
from passengers
where survived = 1 
"""

cur.execute(query1)
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result1 = cur.fetchall()
print("-------------------------")
print("RESULTS FOR average age of survivors vs nonsurvivors")
print(result1)


# What was the average age of each passenger class?
query1 = """
SELECT pclass,count(id) as num, ROUND(avg(age)) as avg_age
FROM passengers
GROUP BY pclass
ORDER BY pclass
"""

cur.execute(query1)
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result1 = cur.fetchall()
print("-------------------------")
print("RESULTS FOR average age of each passenger class")
print(result1)


# What was the average fare by passenger class? By survival?


query1 = """
SELECT pclass,survived,avg(fare) as avg_fare
FROM passengers
GROUP BY pclass, survived
ORDER BY pclass,survived ;
"""

cur.execute(query1)
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result1 = cur.fetchall()
print("-------------------------")
print("RESULTS FOR average fare by passenger class & By survival")
print(result1)


# How many siblings/spouses aboard on average, by passenger class? By survival?

query1 = """

SELECT pclass,survived, sum(sib_spouse_count) as sum_sib_spouse
FROM passengers
GROUP BY pclass,survived
ORDER BY pclass,survived;
"""

cur.execute(query1)
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result1 = cur.fetchall()
print("-------------------------")
print("RESULTS FOR siblings/spouses aboard on average, by passenger class? By survival")
print(result1)

# How many parents/children aboard on average, by passenger class? By survival?
query1 = """
SELECT pclass,survived, SUM(parent_child_count) as sum_par_child
FROM passengers
GROUP BY pclass,survived
ORDER BY pclass,survived

"""

cur.execute(query1)
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result1 = cur.fetchall()
print("-------------------------")
print("RESULTS FOR parents/children aboard on average, by passenger class? By survival?")
print(result1)

# Do any passengers have the same name?
query1 = """
SELECT distinct("name") as p_name
FROM passengers
GROUP BY "name"
HAVING count("name")>1


"""

cur.execute(query1)
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result1 = cur.fetchall()
print("-------------------------")
print("checking for any passengers have the same name")
print(result1)

# (Bonus! Hard, may require pulling and processing with Python) 
# How many married couples were aboard the Titanic? 
# Assume that two people (one Mr. and one Mrs.) 
# with the same last name and with at least 1 sibling/spouse aboard are a married couple.

# print(type(results))
# print(results)