# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 12:11:55 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/05 18:43:43 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

#Checcker comment sortir ma gestion d'erreur sur 

class Vector:
    
    def __init__(self, lst):
        self.values = lst
        try:
            if type(lst) is list:
                for i in lst:
                    if type(i) is not float:
                        raise TypeError
                self.values = np.asarray(lst)
            elif type(lst) is tuple:
                for p in lst:
                    if type(p) is not int:
                        raise TypeError
                self.values = np.arange(lst[0], lst[1], dtype=float)
            else:
                assert int(lst)
                print(lst)
                self.values = np.arange(lst, dtype=float)
        except TypeError:
            print("TypeERROR")
            exit(0)
        self.lenght = len(self.values)
    
    def __str__(self):
        txt = []
        txt.append("Vector {}".format(self.values))
        a = '\n'.join(txt)
        return a

    def __add__(self, other):
        x = self.values + other
        return (x)
    
    def __radd__(self, other):
        x = self.values + other
        return (x)
    
    def __sub__(self, other):
        if other == 0:
            print('ERROR')
            exit(0)
        x = self.values - other
        return (x)
    
    