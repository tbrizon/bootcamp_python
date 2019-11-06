# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    the_bank.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 17:59:27 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/05 20:52:53 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from time import sleep

class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs): #**kwargs c'est pour declarer
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1
    def transfer(self, amount):
        self.value += amount



class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []
    def add(self, account):
        self.account.append(account)
    def transfer(self, origin, dest, amount):
        typ_authorized = {'origin' : [int, str], 'dest' : [int, str], 'amount' : float}
        typ_argument = {'origin' : type(origin.name), 'dest' : type(dest.name), 'amount' : type(amount)}
        argument_value = {'origin' : origin.name, 'dest' : dest.name, 'amount' : amount}        
        if origin.solde < 0 or origin.solde  < argument_value['amount'] or amount < 0:
            print("you are too poor")
            return False
        for key, tip in typ_argument.items():
            if str(tip) in str(typ_authorized[key]):
                print("[{}] ok ".format(key))
            else:
                print("[error] on {} =  {}, {} not allowed, prefere{}".format(key, argument_value[key], typ_argument[key], typ_authorized[key]))
                self.account = self.add(origin)
                return False
        return True



    def fix_account(self, account):
        if self.account:
            print("account with problem :")
            print(self.account)
            return True
        else:
            return False