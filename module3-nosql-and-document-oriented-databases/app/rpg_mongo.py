
"""
The difference between MongoDB and PostgreSQL
is in the way you read and write the data.
For example, when importing in PostgreSQL you look
at the entire row, while for Mongo you have to assign a value
to each column.
The advantage of Mongo is that you don’t need a schema.
However, having a well defined relational schema in postgres
helps us retreiving more information and relationships between tables.
I would say it’s easier to work with postgres when having structured data,
and to work with mongo when having unstructured data.
"""




import pymongo
import urllib
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

print(CLUSTER_NAME)

#Read the db file
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")
connection = sqlite3.connect(DB_FILEPATH)
print(type(connection)) #> <class 'sqlite3.Connection'>

cursor = connection.cursor()
print(type(cursor)) #> <class 'sqlite3.Cursor'>

character = cursor.execute("SELECT * FROM charactercreator_character").fetchall()



#Connect to a MOngo DB database 
connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

cursor = connection.cursor()
print(type(cursor)) #>


db = client.rpg_mongo # "rpg_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.character # "rpg_mongo" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)

# inserting data into table--here character is in line 40

for rw in character:
    collection.insert_one({
    "character_id": rw[0],
    "name":rw[1] ,
    "level":rw[2], 
    "exp":rw[3], 
    "hp":rw[4], 
    "strength":rw[5], 
    "intelligence":rw[6], 
    "dexterity":rw[7], 
    "wisdom":rw[8]
        
    })