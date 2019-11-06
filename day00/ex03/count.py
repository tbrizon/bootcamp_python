# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 11:54:32 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/04 13:22:27 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def text_analyzer(txt):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if not txt:
        txt = input("No text to analyse, please add a text : ") 
    dic = {
        'upper letters' : 0,
        'lower letters' : 0,
        'punctuation marks' : 0,
        'spaces' : 0,
    }
    for i in txt:
        if i.isupper():
           dic['upper letters'] += 1
        elif i.islower():
            dic['lower letters'] += 1
        elif i == ' ':
            dic['spaces'] += 1
        else:
            dic['punctuation marks'] += 1
    print("The text contains {} characters:".format(i))
    for key, value in dic.items():
        print("- {} {}".format(value,key))