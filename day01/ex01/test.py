# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 11:06:14 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/05 12:08:21 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from game import GotCharacter, Stark

if __name__ == "__main__":
    random = GotCharacter("Rando")
    print(random.character_id)
    random = Stark(random)
    print(random.familly_name, random.character_id)
    random = Stark(random)
    print(random.familly_name, random.character_id)
    
    