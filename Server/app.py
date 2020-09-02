from flask import Flask
app = Flask(__name__)
import RecipeDatabase

@app.route('/')
def hello_world():
    return 'Hello, World'


@app.route('/recipe/<id>')
def get_recipe_by_id(id):
    rd = RecipeDatabase.RecipeDatabase()
    return rd.get_recipe(id).to_json()

print("hello world")


