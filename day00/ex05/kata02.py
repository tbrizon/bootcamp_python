# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata02.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 14:12:33 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/04 14:39:27 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == "__main__":
    t = (3, 30, 2019, 9,25)
    u = (t[3], t[4], t[2]) 
    k = (t[1], t[2])
    i = 0
    while i <= 2:
        if u[i] < 10:
            print("0{}".format(u[i]), end='')
        else:
            print("{}".format(u[i]), end='')
        if (i < 2):
            print("/", end='')
        else:
            print(" ", end='')
        i += 1
    i = 0
    while i <= 1:
        if k[i] < 10:
            print("0{}".format(k[i]), end='')
        else:
            print("{}".format(k[i]), end='')
        if (i < 1):
            print(":", end='')
        i+=1