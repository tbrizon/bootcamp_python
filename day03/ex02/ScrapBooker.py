# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ScrapBooker.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/07 12:22:24 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/07 16:49:17 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from NumPyCreator import NumPyCreator

class ScrapBooker():
    def __init__(self):
        pass
    
    def crop(self, array, dimensions, position=(0,0)):
        y = dimensions[0]
        x = dimensions[1]
        try:
            if x + position[1] > array.shape[1] or y + position[0] > array.shape[0]:
                raise Exception
            if x < 0 or y < 0:
                raise Exception
            new_arr = array[position[0]:position[0] + y, position[1]:position[1] + x]
            return new_arr
        except Exception:
            print("dimmension error")
            exit (0)

    def thin(self, array, n, axis = 0):
        
        #array = np.delete(array, np.where(array < n)[0], axis = axis)
        
        print (array,'\n')
        #b = np.any(array % n == 0, axis= 0)
        #print(array[:, np.any(array % 2 == 0, axis = 0)])
        #print(np.delete(arra,np.where(array % n == 0)[0], axis = 0))

        print(np.delete(array, np.s_[n::n], axis)
       
    def juxtapose(self, array, n ,axis = 0):
        array = np.concatenate((array, array), axis = 0)
        for i in range(n):
            if axis == 1:
                array = np.concatenate((array, array), axis = 0)
            else:
                array = np.concatenate((array, array), axis = 1)
        return array

    def mosaic(self, array, dimensions):
        array = self.juxtapose(array, dimensions[0], 0)
        array = self.juxtapose(array, dimensions[1], 1)
        return array
        




if __name__ == "__main__":
    nc = NumPyCreator()
    sb = ScrapBooker()
    arra = nc.from_list([[0, 7, 6, 8 ,9], [1, 2 ,3 ,4,5],[2,4,3,2,1],[3, 7, 6, 8 ,9], [4, 2 ,3 ,4,5],[5,4,3,2,1],[6, 7, 6, 8 ,9], [7, 2 ,3 ,4,5],[8,4,3,2,1]])
    
    arra = nc.identity(2)
    print(sb.mosaic(arra, (1,0)))

    

    
