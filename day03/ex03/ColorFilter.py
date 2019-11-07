# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ColorFilter.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/07 16:21:45 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/07 19:18:23 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt 
from ImageProcessor import ImageProcessor
import numpy as np
from NumPyCreator import NumPyCreator
from time import sleep

class ColorFilter():
    
    def invert(self, array):
        return 1 - array
    
    def to_blue(self, array):
        print(array)
        new = np.zeros(array.shape)
        new[:, :, 2:] = array[:, :, 2:]
        return new
        
    def to_green(self, array):
        return array * (0,1,0)
    
    def to_red(self, array):
        array = self.to_blue(array[0][0][::-1])
        return array

    

if __name__ == "__main__":
    imp = ImageProcessor()
    npc = NumPyCreator()
    cp = ColorFilter()
    
    a = imp.load('./42AI.png')
    a = cp.to_red(a)
    
    imp.display(a)
    #cf = ColorFilter()
    #arr = cf.invert(arr)
    #imp.display(arr)
    