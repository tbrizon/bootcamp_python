# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    YoungestFellah.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/08 17:02:12 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/08 17:36:57 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FilerLoader as fl
import pandas as pd


class YoungestFellah():
    def __init__(self, df, year):
        df = df.loc[df['Year'] == 2010]
        df = df.sort_values('Age')
        
        print (df)
        pass



if __name__ == "__main__":
    df = fl.load('~/goinfre/athlete_events.csv')
    #fl.display(df, 15)
    YoungestFellah(df, 2010)
    pass