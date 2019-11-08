# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 10:21:22 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/07 10:11:20 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import time
"""
    print( args)
    for i in args:
        print(i)
"""
def log(function):
    def wrap(*args):
        print("avant")
        function()
        print("apres")
        return function()
    return wrap


def what_are_the_vars(*args, **kwargs):
    i = 0
    obj = ObjectC
    if not args and not kwargs:
        return 
    for lst_v in args:
        "s{}tr".format("cc")
        setattr(obj, "var_{}".format(i), lst_v)
        i+=1
    for k, value, in kwargs.items():
        setattr(obj, k, value)
    return (ObjectC)
    

class ObjectC(object):
    def __init__(self):
        pass
@log
def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
