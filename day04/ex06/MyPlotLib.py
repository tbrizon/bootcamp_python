# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    MyPlotLib.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/12/02 14:10:16 by tbrizon           #+#    #+#              #
#    Updated: 2019/12/02 15:45:07 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
https://realpython.com/python-histograms/
https://matplotlib.org/3.1.1/gallery/statistics/hist.html
https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.hist.html
https://medium.com/python-pandemonium/data-visualization-in-python-histogram-in-matplotlib-dce38f49f89c
"""

from FileLoader import FilerLoader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib
from HowManyMedalsByCountry import HowManyMedalsByCountry

class MyPlotLib(object):
    def __init__():
        pass
    def histogram(data, features):
        # An "interface" to matplotlib.axes.Axes.hist() method
        x = 0
        medals = []
        years = []
        for key, value in features.items():
            for k, v in value.items():
                x = x + v
            medals.append(x)
            years.append(key)
            x = 0
        size = np.arange(len(years))
        hist, bin_ledge = np.histogram(medals)
        print(hist, bin_ledge)
    
        n, bins, patches = plt.hist(x=medals, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
        plt.grid(axis='y', alpha=0.75)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('My Very Own Histogram')
        plt.text(23, 45, r'$\mu=15, b=3$')
        maxfreq = n.max()
        # Set a clean upper y-axis limit.
        plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
        plt.show()
        
        
if __name__ == "__main__":
    data = FilerLoader.load('/private/tmp/tbrizon/bootcamp_python/day04/ressources/athlete_events.csv')
    mp = MyPlotLib
    x = HowManyMedalsByCountry(data, 'France')
    mp.histogram(data, x)
    pass