# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 09:08:30 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/05 10:05:25 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Recipe:
    
    def __init__(self, name, lvl, time, ingr, descri, tip):
        self.name = name
        self.cooking_lvl = lvl
        self.cooking_time = time
        self.ingredient = ingr
        self.decription = descri
        self.recipe_type = tip
    
    def info(self):
        
        txt = []
        txt.append("name of the recipe : {}\nCooking_lvl : {}".format(self.name, self.cooking_lvl))
        txt.append("cooking time : {}".format(self.cooking_time))
        txt.append("Ingredient : {}".format(' | '.join(self.ingredient)))
        txt.append("Description : {}".format(self.decription))
        txt.append("Type of meal : {}".format(self.recipe_type))
        a = '\n'.join(txt)
        return a

    def __str__(self):
        prin = self.info()
        return prin