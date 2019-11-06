# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 09:17:58 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/06 11:11:02 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce
from functools import reduce

def plus_one(x):
    return x + 1

def afficher(a, b):
    print("Entrée :", a, b)
    print("Sortie :", a + b)
    return a + b
 

if __name__ == "__main__":
    a = range(40)
    b = [0, 52, 0]