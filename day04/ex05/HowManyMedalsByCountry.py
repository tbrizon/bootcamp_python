# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    HowManyMedalsByCountry.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/12/02 13:28:25 by tbrizon           #+#    #+#              #
#    Updated: 2019/12/02 13:50:51 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FilerLoader
import pandas as pd


def HowManyMedalsByCountry(data, country):
    x = data.loc[(data['Team'] == country)]
    grouped = x.groupby(['Year', 'Medal']).size().unstack(fill_value = 0)
    grouped = grouped.rename(columns={'Bronze' : "B", 'Silver' : 'S', 'Gold' : 'G'})
    print(grouped.reindex(columns = ['G', 'S', 'B']).to_dict('index'))

if __name__ == "__main__":
    data = FilerLoader.load('/private/tmp/tbrizon/bootcamp_python/day04/ressources/athlete_events.csv')
    HowManyMedalsByCountry(data, 'France')
    pass