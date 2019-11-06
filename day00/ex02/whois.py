# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 11:23:28 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/04 11:53:55 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def who(x):
    if x == 0:
        print ("I'm Zero.")
        sys.exit(0)
    if (x % 2) == 0:
        print ("I'm Even.")
    else:
        print("I'm Odd.")

def check(arg):
    try:
        x = int(arg)
        return x
    except ValueError:
        print("ValueERROR")
        sys.exit(0)

if __name__ == "__main__":
    
    if  len(sys.argv) > 2:
            print("ERROR")
    else:
        if len(sys.argv) > 1:
            x = check(sys.argv[1])
            who(x)
