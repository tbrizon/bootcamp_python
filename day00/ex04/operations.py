# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 13:22:47 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/04 13:55:03 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def calculate(x, y):
    dic = {
        'Sum' : 0,
        'Difference' : 0,
        'Product' : 0,
        'Quotient' : 0,
        'Remainder' : 0,
    }
    try:
        x = int(x)
        y = int(y)
        dic['Sum'] = x + y
        dic['Difference'] = x + y
        dic['Product'] = x * y
        dic['Quotient'] = x / y
        dic['Remainder'] = x % y
    except ValueError:
        print("Input Error: only numbers")
        exit(0)
    except ZeroDivisionError:
        dic['Quotient'] = "ERROR (div by zero)"
        dic['Remainder'] = "ERROR (modulo by zero)" 
    for key, value in dic.items():
        print("{}:         {}".format(key, value))


if __name__ == "__main__":
    if len(sys.argv) == 1:
            exit(0)
    if len(sys.argv) != 3:
        print("ERROR wrong number of arguments")
        exit (0)   
    calculate(sys.argv[1], sys.argv[2])