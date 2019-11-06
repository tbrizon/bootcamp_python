# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 18:14:02 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/04 19:07:42 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import time

def ft_progress(lst):
    for i in lst:
        if i % 2 == 0:
            yield i*i
        else:
            yield i

if __name__ == "__main__":
    lst = range(500)
    ret = 0
    for elem in ft_progress(lst): 
        ret += (elem + 3) % 5
        print(elem)
    
    print(ret)