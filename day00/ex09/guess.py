# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 18:01:52 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/04 18:13:37 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import randint

if __name__ == "__main__":
    print("Hi this i an interaction game\nYou'll have to choose a number")
    print("Do your best !\nExit to quit the game !")
    x = randint(1,99)
    arr = input("Ready or Exit ?    ")
    i = 0
    while arr != "Exit":
        nb = int(input("\nGuess between 1 and 99   "))
        i += 1
        if nb > x:
            print("TOO HIGH")
        if nb < x:
            print("TOO LOW")
        if nb == x:
            print("CONGRAT, the number was {}, you won with {} try".format(x, i))
            arr = input("Continue ? Yes/Exit ?     ")
        if arr == 'Yes':
            x = randint(1, 99)
            i = 0
    print("Salut la miff")