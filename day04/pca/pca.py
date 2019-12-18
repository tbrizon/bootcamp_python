# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pca.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/12/13 16:50:10 by tbrizon           #+#    #+#              #
#    Updated: 2019/12/13 17:22:37 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np


if __name__ == "__main__":
    i = 0

    lst2 = [6, 8, 7, 14.50, 14, 10, 7, 12.50, 9.50]
    lst1 = [6, 8, 6, 14.50, 14, 11, 5.50, 13.00, 9]
    x2 = np.asarray(lst1)
    x1 = np.asarray(lst2)
    lst2_mean, lst1_mean = np.around([x2.mean(), x1.mean()], decimals=2)

    x1_summ = x1.sum(x1)
    x1_summ = x1_summ / x1.ndarray.size() - 1
    print (x1_summ, x1_summ / x1.ndarray.size() - 1)
    x1 = x1 - lst1_mean
    x2 = x2 - lst2_mean
    print(x1, x2)
    

