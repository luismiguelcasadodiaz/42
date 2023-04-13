#!/usr/bin/python3
"""
Part 1 Nested Dictionaries
Create a dictionary called cookbook.
"""
cookbook = {}
"""
You will use this cookbook to store recipe.
A recipe is a dictionary that stores (at least) 3 couples key-value:
• ”ingredients": a list of string representing the list of ingredients
• "meal": a string representing the type of meal
• "prep_time": a non-negative integer representing a time in minutes
In the cookbook, the key to a recipe is the recipe name.

Initialize your cookbook with 3 recipes:
• The Sandwich’s ingredients are ham, bread, cheese and tomatoes.
  It is a lunch and it takes 10 minutes of preparation.
"""
recipe = {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
        }
cookbook["Sandwich"] = recipe
"""
• The Cake’s ingredients are flour, sugar and eggs.
  It is a dessert and it takes 60 minutes of preparation.
"""
recipe = {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
        }
cookbook["cake"] = recipe

"""
• The Salad’s ingredients are avocado, arugula, tomatoes and spinach.
  It is a lunch and it takes 15 minutes of preparation.
"""
recipe = {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15,
        }
cookbook["salad"] = recipe
