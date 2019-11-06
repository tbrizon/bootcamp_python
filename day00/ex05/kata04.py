# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 14:47:39 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/04 15:05:06 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == "__main__":
    t = ( 0, 4, 132.42222, 10000, 12345.67)
    day = str(t[0])
    ex = str(t[1])
    print("day_{}, ".format(day.rjust(2, '0')), end='')
    print("ex_{} : ".format(day.rjust(2,'0')), end='')
    nb = round(t[2], 2)
    print("{}, ".format(nb), end='')
    scientifique = t[3]
    print(" {:.2e}, ".format(scientifique), end='')
    print("{:.2e}".format(t[4]))