# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 14:07:15 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/04 15:21:31 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == "__main__":
    
    languages = {
        'Python' : 'Guid van Rossum',
        'Ruby' : 'Yukihiro Matsumoto',
        'PHP' : 'Rasmus Lerdorf',
    }
    for key, value in languages.items():
        print("{} was created by {}".format(key, value))
    