# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 09:17:19 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/06 10:13:21 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_filter(function, *args):
    new_lst = []
    for x in args:
        for elem in x:
            if function(elem) == True:
                new_lst.append(elem)
    return new_lst