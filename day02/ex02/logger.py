# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logger.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 11:24:49 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/06 17:22:29 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time as time
from random import randint
import os
import getpass


def log(func):
    """
    Un décorateur qui log l'activité d'un script.
    (Ok, en vrai ça fait un print, mais ça pourrait logger !)
    """
    fd = open("machine.log", 'a')
    def wrapper(*args, **kwargs):
        fcname = func.__name__
        t = time.time()
        res = func(*args, **kwargs)
        ti = round(time.time() - t, 3)
        username = getpass.getuser()
        print("({})Running: {}   [ exec-time = {} ms ]".format(username,fcname, ti), file=fd)
        return res
    return wrapper

class CoffeeMachine():
    water_level = 100
    @log
    def start_machine(self):
     if self.water_level > 20:
         return True
     else:
         print("Please add water!")
         return False
    @log
    def boil_water(self):
        return "boiling..."
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    @log
    def add_water(self, water_level):
        time.sleep(randint(1,5))
        self.water_level += water_level
        print("Blub blub blub...")
        
if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)