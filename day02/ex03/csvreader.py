# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    csvreader.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 14:35:51 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/06 17:06:22 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time

def truc():
    print("salut")

class CsvReader(object):
    def __init__(self, name, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.name = name

    def getdata(self):
        print(self.data)

    def __enter__(self):
        s = []
        f =  open(self.name, 'r')
        for line in f:
            s.append(line.split(','))
        self.data = s

    def __exit__(self, type, value, traceback):
        print("end of file")

if __name__ == "__main__":
    with CsvReader('good.csv') as f:
        f.getdata()
    