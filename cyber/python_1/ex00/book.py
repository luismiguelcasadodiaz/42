#!/usr/bin/python3
"""
The Book class.

The Book class also has some attributes:
• name (str): name of the book,
• last_update (datetime): the date of the last update,
• creation_date (datetime): the creation date,
• recipes_list (dict): a dictionnary with 3 keys: "starter", "lunch", "dessert".

"""
from datetime import datetime

class Book:
    __empty_recipes_list = {"starter": [],
                            "lunch": [],
                            "dessert" : []}
    __now = datetime.today()

    def __init__(self, name: str):
        self.name = name
        self.recipes = self.__empty_recipes_list
        self.last_update = None  # at creation time there is not update
        self.creation_date = self.set_creation_date()

    def set_creation_date(self):
        return datetime.today()



    def set_last_update(self):
        self.last_update = self.set_creation_date()
        return 


    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance""" 
        #... Your code here ...
        for key in self.recipes.keys():
            key_list = get_recipes_by_types(key)
            for arecipe in key_list:
                if name == arecipe.name:
                    print(arecipe)

        
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """ 
        return self.recipes[recipe_type]
        
        

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update""" 
        self.recipes[recipe.recipe_type].append(recipe)
        

    def print_all(self):
        for k in self.recipes.keys():
            self.get_recipes_by_types(k)
