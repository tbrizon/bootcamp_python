# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NumPyCreator.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/07 09:38:25 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/07 11:32:27 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

class NumPyCreator:

    def __init__(self):
        pass

    def from_list(self, lst, t=None):
        return np.asarray(lst, dtype = t)
        
    def from_tuple(self, tpl, t=None):
        return np.asarray(tpl, dtype = t)

    def from_iterable(self,it, t='int'):
        return np.fromiter(it, t)

    def from_shape(self, shape, value = 0, t=None):
        return np.full(shape, value, dtype = t)
    
    def random(self, shape):
        return np.random.rand(shape[0], shape[1])
    
    def identity(self, value, t=None):
        return np.identity(value, dtype =t)
            
    
        
            


if __name__ == "__main__":
    npc = NumPyCreator()
    npc.from_list([[1,2,3],[6,3,4]])
    npc.from_list([[1,2,3],[6,3,4]], t = 'float')
    npc.from_tuple(("a", "b", "c"))
    x = range(8)
    npc.from_iterable(x)
    shape = (3, 5)
    npc.from_shape(shape)
    print(npc.random(shape))
    print(npc.identity(4, t = 'int'))
    pass