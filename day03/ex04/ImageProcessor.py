# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ImageProcessor.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/07 11:34:32 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/07 19:15:47 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from NumPyCreator import NumPyCreator
import numpy as np
import matplotlib
from matplotlib._png import read_png
import matplotlib.pyplot as plt 


class ImageProcessor:
    def __init__(self):
        pass

    def load(self,path,show=False):
        img_plt = plt.imread(path)
        size_x = img_plt.shape[0]
        size_y = img_plt.shape[1]
        print("size : {} x {}".format(size_x, size_y))
        return img_plt

    def display(self, array):
        
        plt.imshow(array)
        plt.show()
    
    def random(self, array):
        
        npc = NumPyCreator()
        shape = npc.random((array.shape[0],array.shape[1]))
        array = array * shape
        return array


if __name__ == "__main__":
    
    imp = ImageProcessor()
    array = imp.load("./logo_v4_noir.png")
    imp.display(array)
