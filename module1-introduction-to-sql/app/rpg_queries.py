

import sqlite3
import os

#DB_FILEPATH = "data/chinook.db"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")
conn = sqlite3.connect(DB_FILEPATH)
conn.row_factory = sqlite3.Row
print(type(conn)) #> <class 'sqlite3.Connection'>
curs = conn.cursor()
print(type(curs)) #> <class 'sqlite3.Cursor'>



query = """SELECT 
count(DISTINCT character_id) as character_count
FROM charactercreator_character"""

query1 = """SELECT 
count(DISTINCT character_ptr_id) as character_ptr_count
FROM charactercreator_cleric"""

query2 = """SELECT 
count(DISTINCT character_ptr_id) as character_ptr_count
FROM charactercreator_fighter"""

query3 = """SELECT 
count(DISTINCT character_ptr_id) as character_ptr_count
FROM charactercreator_mage"""

query4 = """SELECT 
count(DISTINCT character_ptr_id) as character_ptr_count
FROM charactercreator_thief"""

query5 = """SELECT count(DISTINCT item_id) as total_item
from armory_item"""


query6 = """SELECT count(DISTINCT item_ptr_id) as number_of_weapons 
FROM armory_weapon"""

query7 = """SELECT
count(DISTINCT item_id)  -  count(DISTINCT item_ptr_id) as total_non_weapons
FROM armory_item, armory_weapon
"""


query8 ="""SELECT character_id,count(DISTINCT item_id) as item FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20
"""

query9 = """SELECT a.character_id,count(DISTINCT c.item_ptr_id) as number_of_weapons
FROM charactercreator_character_inventory as a
LEFT JOIN armory_item as b ON a.item_id = b.item_id
LEFT JOIN armory_weapon as c ON b.item_id = c.item_ptr_id
GROUP BY a.character_id
LIMIT 20 """

# -- On average, how many Items does each Character have?
# -- return a single number
# -- intermediate step:
# --     row per character (302)
# --     columns: character_id, name, item_count


query10 = """select avg(item_count) as avg_items
from (
    select
      c.character_id
      ,c."name" as character_name
      ,count(distinct inv.item_id) as item_count
    from charactercreator_character c
    left join charactercreator_character_inventory inv ON c.character_id = inv.character_id
    group by 1, 2
) subq
 """



#  on average , how many weapons does each character have


query11 = """SELECT avg(weapon_count) as avg_weapon
FROM (
    SELECT
     cci.character_id
     ,count(DISTINCT aw.item_ptr_id) as weapon_count
    FROM charactercreator_character_inventory cci
    LEFT JOIN armory_item ai ON cci.item_id = ai.item_id
    LEFT JOIN armory_weapon aw ON ai.item_id = aw.item_ptr_id
    GROUP BY 1
) subz"""



# results2 = curs.execute(query).fetchall()
# print("--------")
# print("RESULTS 2", results2)
print("----------")
result = curs.execute(query).fetchone()
print("RESULTS FOR CHARACTERCREATOR_CHARACTER", result)
print(result["character_count"])
print("-------------")
result1 = curs.execute(query1).fetchone()
print("Results for charactercreator_cleric", result1)
print(result1["character_ptr_count"])
print("---------")
result2 = curs.execute(query2).fetchone()
print("Results for charactercreator_fighter", result2)
print(result2["character_ptr_count"])
print("---------")
result3 = curs.execute(query3).fetchone()
print("Results for charactercreator_mage", result3)
print(result3["character_ptr_count"])
print('--------')
result4 = curs.execute(query4).fetchone()
print("Results for charactercreator_thief", result4)
print(result4["character_ptr_count"])
print("-------------")
result5 = curs.execute(query5).fetchone()
print("Results for total Items", result5)
print(result5["total_item"])
print("-------------")
result6 = curs.execute(query6).fetchone()
print("Results for total Items", result6)
print(result6["number_of_weapons"])
print("---------------------------")
result7 = curs.execute(query7).fetchone()
print("Results for total non weapon", result7)
print(result7["total_non_weapons"])
print("-------------------------")
result8 = curs.execute(query8).fetchall()

print("Total items for each character", result8)


print("----------------------------")
result9 = curs.execute(query9).fetchall()

print("Total weapons for each character", result9)
print("----------------------------")
result10 = curs.execute(query10).fetchone()
print("avg_items for each character", result10)
print(result10["avg_items"])
print("----------------------------")
result11 = curs.execute(query11).fetchone()
print("avg_weapon for each character", result11)
print(result11["avg_weapon"])



