# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 16:52:43 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/05 19:54:24 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

class   Evaluator:       
    def __init__(self, w, coef):
        try:
            if type(w) is list:
                for i in w:
                    if type(i) is not str:
                        raise TypeError
                self.words = np.asarray(w)
            if type(coef) is list:
                for j in coef:
                    if type(j) is not float and int:
                        raise TypeError
                self.coefs = np.asarray(coef)
            else:
                raise TypeError
        except TypeError:
            print("TypeERROR, send two list of words and coefficients")
            exit (0)
    
    def zip_evaluate(coef, w):
        i = 0
        lst = zip(w, coef)
        for p in lst:
            i += len(p[0]) * p[1]
        return print(i)
