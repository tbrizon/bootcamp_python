# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    SpatioTemporalData.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/12/02 12:47:40 by tbrizon           #+#    #+#              #
#    Updated: 2019/12/02 13:27:05 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from FileLoader import FilerLoader


class SpatioTemporalData(object):
    def __init__(self, data):
        data = data

    def when(self, city):
        lst = []
        x = data.loc[(data['City'] == city)]
        grouped = x.groupby(['Year'])
        res = grouped.size()
        for values in res.items():
            lst.append(values[0])
        print(lst)


        
    def where(self, year):
        x = data.loc[(data['Year'] == year)]
        print(x['City'][:1].values[0])
        

if __name__ == "__main__":
    data = FilerLoader.load('/private/tmp/tbrizon/bootcamp_python/day04/ressources/athlete_events.csv')
    sp = SpatioTemporalData(data)
    sp.when('Paris')
    pass