# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    AdvancedFilter.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/08 11:40:01 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/08 16:14:28 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from ImageProcessor import ImageProcessor
from NumPyCreator import NumPyCreator
from ScrapBooker import ScrapBooker
from time import sleep
class AdvancedFilter():
    def __init__(self):
        pass
    
    def concat(self, array3D):
        pass

    def make_kernel(self, kernel, array, size, position):
        y_ = position[1] - 1
        x_ = position[0] - 1
        to_kernel = ScrapBooker.crop(self, array, size, position=(y_, x_))
        value = kernel * to_kernel
        value = np.sum(value)
        value = value / (size[0] * size[1])
        return value


    def mean_blur(self, array3D, size =(3 , 3)):
        kernel = np.full(size, 1)
        new = np.copy(array3D)
        
        for y in enumerate(array3D):
            if y[0] >= size[1] - 1 and y[0] < new.shape[0] - 1:
                for x in  enumerate(y[1]):
                    
                    if x[0] >= size[1] - 1 and x[0] < new.shape[1] - 1 :
                        
                        new[y[0]][x[0]] = self.make_kernel(kernel,array3D,size,(y[0],x[0]))
                        
                        
        return (new)


if __name__ == "__main__":
    imp = ImageProcessor()
    npc = NumPyCreator()
    af = AdvancedFilter()

    

    array = imp.load('./Fourmisse.png')
    imp.display(array)
    test = np.random.randint(9,size =(8,8))
    print (test)    
    #imp.display(array)
    arr = af.mean_blur(array)
    print(arr)
    print('\n', test)
    imp.display(arr)
    
    

