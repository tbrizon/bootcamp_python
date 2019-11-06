# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 15:26:23 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/05 16:52:09 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import time
import random


def generator(text, sep='',option=None):
    
    txt = text.split(sep)
    dic = {
        'shuffle' : random.shuffle(txt),
        'unique'  :  list(set(txt)),
        'ordered' : list(dict.fromkeys(txt)),
    }
    for value in dic.items():
        if value == option:
            txt = value[1]
            print(txt)
    for l in txt:
        time.sleep(0.1)
        yield l

if  __name__ == "__main__":
    f = "le Lorem Ipsum est simplement du faux texte."
    for word in generator(f, sep=' ', option=""):
        print(word)