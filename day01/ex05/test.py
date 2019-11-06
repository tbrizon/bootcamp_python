# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 18:10:19 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/05 20:52:43 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from the_bank import Account, Bank


if __name__ == "__main__":
    Gege = {
        'solde' : 1500,
        'previsionnel' : 100,
        'agence' : 'Paris',
        'value'  : 100000
    }

    Holi = {
        'solde' : 800,
        'previsionnel' : 100,
        'agence' : 'Paris',
        'value'  : 100000
        }

    le_mechant = {
        'solde' : -5,
        'previsionnel' : 100,
        'agence' : 'aris',
        'value'  : 100000
    }
    
    g = Account("Gege", **Gege)
    h = Account("Holi", **Holi)
    lm = Account("le_mechant", **le_mechant)
    
    bank = Bank()
    bank.transfer(h, g, 500)
    bank.fix_account(0)