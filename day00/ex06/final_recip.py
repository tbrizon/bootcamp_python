# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    final_recip.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 16:12:52 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/04 16:24:36 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import recipe

def options(x, name):
    if x == 1:
        recipe.add_recipe(name, input("ingredient name pls"), input("Meal ?"), input("prep time ?"))
    if x == 2:
        recipe.del_recipe(name)
    if x == 3:
        recipe.print_recipe(name)
    if x == 4:
        recipe.print_all_recipename()
    
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
    x = input("Please, select an option \n1: Add recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n")
    options(x, input("Select a recipe"))
    