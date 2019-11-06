# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 16:27:51 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/04 17:18:54 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import re

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("ERROR")
        exit(0)
    if len(sys.argv) == 2:
        array = re.sub(r'\b\w{1,3}\b', '', sys.argv[1])
        print(array.split())