# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    MyPlotLib.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/12/02 14:10:16 by tbrizon           #+#    #+#              #
#    Updated: 2019/12/13 16:52:07 by tbrizon          ###   ########.fr        #
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
from scipy.stats import gaussian_kde
import seaborn as sns

class MyPlotLib(object):
    def __init__():
        pass

    def pairplot(df, features):
        sns.pairplot(df[features])
        plt.show()
    def density(df, features):
        
        for feature in features:
            if df[feature].dtypes is object:
                print ('Non numerical value, error')
                exit ()
            ndf = df.fillna(0)
            ndf = ndf[ndf[feature] > 0]
            sns.distplot(ndf[feature], hist=True, kde=True, 
            bins=int(100), 
            kde_kws={'shade' : True, 'linewidth': 2},
            label = feature)
        plt.legend(prop={'size': 7}, title = 'Features')
        plt.title('Features Density')
        plt.show()
        
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def histovie(df, features):
        """
        il me faut la valeur max de chaque feature pour en faire les xmax de mon histo
        il me faut le nombre de ligne de chaque feature pour en faire le y max 
        """
        
        i = 1
        for feature in features:
            if df[feature].dtypes is object:
                print ('Non numerical value, error')
                exit ()
            i += 1
            x_max = df[feature].max()
            y_max = df[feature].count()
            ndf = df.fillna(0)
            ndf = ndf[ndf[feature] > 0]
            values = ndf[feature].values
            hist, bin = np.histogram(values)
            plt.figure()
            n, bins, patches = plt.hist(x=values, bins=100, color='#0504aa',
                            alpha=0.9, rwidth=0.85)
            plt.title('{} Histogram'.format(feature))
        plt.show()
        
if __name__ == "__main__":
    features = ['Age', 'Height', 'Weight']
    data = FilerLoader.load('/Users/tbrizon/Desktop/tbrizon_42/bootcamp_python/day04/ressources/athlete_events.csv')
    mp = MyPlotLib
    x = HowManyMedalsByCountry(data, 'France')
    #mp.histovie(data, features)
    mp.density(data, features)
    #mp.pairplot(data, features)
    pass