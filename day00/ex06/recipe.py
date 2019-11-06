# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 15:05:51 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/04 19:21:16 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from pprint import pprint

def print_recipe(recipe):
    print("recette : {}".format(cookbook[recipe]))

def del_recipe(recipe):
    cookbook[recipe].clear()

def add_recipe(recipe_name, ingredient, meal, prep_time):
    new = ingredient.split()
    ingredient_new = {
        'ingredient' : new,
        'meal' : meal,
        'prep_time' : prep_time
    }
    cookbook[recipe_name] = ingredient_new

def print_all_recipename():
    for key in cookbook:
        print("recipe : {}".format(key))
    
if __name__ == "__main__":

    ingredient_sandwich = ['ham', 'bread', 'cheese', 'tomatoes']
    ingredient_cake = ['flour', 'sugar', 'eggs']
    ingredient_salad = ['avocado', 'arugula', 'tomatoes', 'spinach']
    
    cookbook = {
        "sandwich" : { 'ingredient' : ingredient_sandwich, 'meal' : 'lunch', 'prep_time' : 10},
        "cake" : { 'ingredient' : ingredient_cake, 'meal' : 'dessert', 'prep_time' : 60},
        "salad" : { 'ingredient' : ingredient_salad, 'meal' : 'lunch', 'prep_time' : 15},
    }
    """
    for key in cookbook:
        print("keys -->{}".format(key))
    for value in cookbook.items():
        print("only values -> {}".format(value[1]))
    for all_v in cookbook.items():
        print("All value > {}".format(all_v))
    """