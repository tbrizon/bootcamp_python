# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    YoungestFellah.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/08 17:02:12 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/27 12:28:14 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FilerLoader as fl
import pandas as pd


def YoungestFellah(data, year):
    yf = {
        'f' : [],
        'm' : []
    }

    m = data.loc[(data['Year'] == year) & (data['Sex'] == 'M')].sort_values(by =['Age'])
    f = data.loc[(data['Year'] == year) & (data['Sex'] == 'F')].sort_values(by =['Age'])

    x = m['Age'][:1].values[0]
   
    yf['m'] = m['Age'][:1].values[0]
    yf['f'] = f['Age'][:1].values[0]
    print(yf)
    

if __name__ == "__main__":
    df = fl.load('../ressources/athlete_events.csv')
    YoungestFellah(df, 2004)
    pass