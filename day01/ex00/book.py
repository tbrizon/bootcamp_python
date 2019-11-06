# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 09:08:26 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/05 10:36:09 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime

class Book:

    def __init__(self, name, last_update, date, recipes):
        self.name = name
        self.last_update = last_update
        self.date = date
        self.recipes = recipes

    def get_recipe_by_name(self, name):
        for value in self.recipes.items():
            if value[1].name == name:
                print(value[1])
                