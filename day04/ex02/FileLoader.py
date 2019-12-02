# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    FileLoader.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/08 16:28:08 by tbrizon           #+#    #+#              #
#    Updated: 2019/12/02 11:16:18 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd

class FilerLoader():
    
    def __init__(self):
        pass


    def load(path):
        data = pd.read_csv(path)
        print("size : {}".format(data.size))
        return data
    
    def display(df, n):
        print(df.head(n))
        
if __name__ == "__main__":
    fl = FilerLoader
    a = fl.load('~/goinfre/athlete_events.csv')
    fl.display(a, -271114)
    fl.display(a, -1)
    