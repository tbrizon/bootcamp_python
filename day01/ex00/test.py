# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 09:08:36 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/05 16:19:54 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime

from recipe import Recipe
from book import Book

if __name__ == "__main__":
    ingredient_tourte = ['Salut', 'Toi', 'Comment','ca','va']
    a = Recipe("tourte", 2, 50, ingredient_tourte, "Tourte pour manger","entree")
    b = Recipe("pizza", 4, 12, ingredient_tourte, "pizza","lunch")
    c = Recipe("flan", 5, 10, ingredient_tourte, "pizza","lunch")
    lst = {
        'start' : a,
        'lunch' : b,
        'dessert' : c,
    }
    book = Book("le beau livre", 0, 0, lst)
    book.get_recipe_by_name("flan")