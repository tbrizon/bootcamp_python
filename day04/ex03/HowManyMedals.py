# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    HowManyMedals.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/12/02 11:17:24 by tbrizon           #+#    #+#              #
#    Updated: 2019/12/02 12:46:47 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from FileLoader import FilerLoader
import numpy as np

def HowManyMedals(data, name):
    x = data.loc[(data['Name'] == name)]
    ym = x.groupby(["Year", "Medal"])
    value = ym.size().unstack(fill_value=0)
    value = value.to_dict('index')
    print (value)
    

if __name__ == "__main__":
    data = FilerLoader.load('/private/tmp/tbrizon/bootcamp_python/day04/ressources/athlete_events.csv')
    HowManyMedals(data, 'Kjetil Andr Aamodt')