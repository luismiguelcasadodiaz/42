#!/usr/bin/python3
"""
The Recipe class.

It has some attributes:
    • name (str): name of the recipe,
    • cooking_lvl (int): range from 1 to 5,
    • cooking_time (int): in minutes (no negative numbers),
    • ingredients (list): list of all ingredients each represented by a string,
    • description (str): description of the recipe,
    • recipe_type (str): can be "starter", "lunch" or "dessert".

"""


class Recipe:
    def __ini__(self,
                name: str,     # name of the recipe,
                c_l: int,      # range from 1 to 5
                c_t: int,      # in minutes (no negative numbers)
                ingre: list,   # ingredients' list. One string per ingredient
                desc: str,     # description of the recipe,
                r_type: str    # can be "starter", "lunch" or "dessert"
                ):
