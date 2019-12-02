# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ProportionBySport.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/12/02 10:52:37 by tbrizon           #+#    #+#              #
#    Updated: 2019/12/02 11:17:16 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from FileLoader import FilerLoader

def proportionBySport(data, year, sport, gender):
    x = data.loc[(data['Year'] == year) & (data['Sport'] == sport) & (data['Sex'] == gender)]
    y = data.loc[(data['Year'] == year) & (data['Sex'] == gender)]
    res = len(x) / len(y)
    print(res)

if __name__ == "__main__":
    data = FilerLoader.load('/private/tmp/tbrizon/bootcamp_python/day04/ressources/athlete_events.csv')
    proportionBySport(data, 2004, 'Tennis', 'F')