# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_map.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 09:17:22 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/06 10:14:52 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_map(founction, *args):
    result = []
    for e in args:
        new_lst = [founction(x) for x in e]
        result.append(new_lst)
    return result
    