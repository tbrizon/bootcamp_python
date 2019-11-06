# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 10:18:05 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/04 11:21:51 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def print_all(dict_arg, size_arg):
    while size_arg > 0:
        print(dict_arg[size_arg], end='')
        if size_arg > 1:
                print(' ', end='')
        size_arg -= 1
    

def reverse(arg):    
    return arg[::-1]

if __name__ == "__main__":
    
    size_arg = 0
    dict_arg = {}
    for arg in sys.argv:
        if size_arg > 0:
            dict_arg[size_arg] = reverse(arg)
        size_arg += 1
    print_all(dict_arg, size_arg - 1)