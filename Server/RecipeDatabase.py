import sqlite3
from sqlite3 import Error
from Recipe import recipe
import json

connection_string = 'Resources/RecipeDB.db'

class RecipeDatabase:
    def __init__(self):
        self.connection_string = connection_string

    def _to_recipe(self, query_result):
        recipes = []
        for row in query_result:
            id = row[0]
            name = row[1]
            author = row[2]
            cook_time = row[3]
            prep_time = row[4]
            cuisine = str(row[5]).split('\r\n')
            yeild = str(row[6]).split('\r\n')
            dish_type = str(row[7]).split('\r\n')
            ingredients = str(row[8]).split('\r\n')
            instructions = str(row[9]).split('\r\n')
            url = str(row[10])

            rec = recipe(id,name,author,cook_time,prep_time,cuisine,yeild,dish_type,ingredients,instructions,url)
            recipes.append(rec)
        return recipes

    def get_recipe(self, id):
        rec = None
        try:
            conn = sqlite3.connect(connection_string)
            cur = conn.cursor()
            cur.execute('Select * From Recipe Where id = {id}'.format(id=id))
            rec = self._to_recipe(cur.fetchall())
        except Error as e:
            print(e)

        finally:
            cur.close()
            conn.close()
            return rec[0]

        conn.close()


rdb = RecipeDatabase()
rdb.get_recipe(10)