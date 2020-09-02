import json

class recipe:
    id = 0
    recipe_name = ''
    author = ''
    cook_time = 0
    prep_time = 0
    cuisine = []
    yeild = []
    dish_type = []
    ingredients = []
    instructions = []
    url = []

    def __init__(self, id, recipe_name, author,cook_time,prep_time,cuisine,yeild,dish_type,ingredients,instructions,url):
        self.id = id
        self.recipe_name = recipe_name
        self.author = author
        self.cook_time = cook_time
        self.prep_time = prep_time
        self.cuisine = cuisine
        self.yeild = yeild
        self.dish_type = dish_type
        self.ingredients = ingredients
        self.instructions = instructions
        self.url = url

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=3)

