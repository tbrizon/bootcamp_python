# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 10:54:49 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/05 18:30:46 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GotCharacter:
    i = 0
    def __init__(self,first_name, is_alive = True):        
        self.first_name = first_name
        self.character_id = GotCharacter.i
        self.is_alive = is_alive
        GotCharacter.i += 1
    
    def info(self):
        txt = []
        txt.append("ID = {}".format(self.character_id))
        a = '\n'.join(txt)
        
        return a

    def __str__(self):
        prin = self.info()
        return prin
 

class Stark(GotCharacter):

    def __init__ (self, first_name=None, is_alive = True):
        super().__init__(first_name =first_name, is_alive=is_alive)
        self.familly_name = 'Stark'

    def __dict__(self):
        dic = {
            'prenom' : self.first_name,
            'alive' : self.is_alive,
            'family_name' : self.familly_name,
            'house_word' : "Winter is Coming",
        }
        return dic
        
    def __str__(self):
        txt = []
        parent = super().__str__()
        txt.append("herite de : \n{}\n\n".format(parent))
        txt.append("prenom : {}".format(self.first_name))
        print("\n\n\n{}\n\n\n".format(self.familly_name))
        i = '\n'.join(txt)
        return i
    
    """
    faire un heritage permet grace a super de faire des classe qui possede
    les attributs de la classe parent en plus de leurs attributs
    on peut initialiser les attributa de la classe parent a la classe fils
    """
