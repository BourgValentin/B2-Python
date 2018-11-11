#!/usr/bin/python3.6

####################
#Le jeu consiste a trouver un nombre entre 1 et 1OO
#
#Il est possible d'appuyer sur 'q' pour quitter
#
#Appuyer sur CTRL+C affichera un message puis eteindra le programme
####################

import re
import random
import signal
import sys

pattern = re.compile("^[1-9][0-9]?$|^100$|^[q]$")

def kill(sig, frame):
        print('Tu as entré CTRL+C, le programme va s\'arréter')
        sys.exit(0)

signal.signal(signal.SIGINT, kill)

print("Trouvez un nombre entre 1 et 100 : ")

random_nbr = random.randint(1,100)

user_input = input("Saisie :")

while not pattern.match(user_input):
    print("Erreur : Veuillez entrer un nombre ou q pour quitter : ")
    user_input = input("Saisie :")
else:
    pass

while pattern.match(user_input) and user_input != 'q':

        if int(user_input) > random_nbr:
            print("Plus petit : ")
            user_input = input("Saisie :")

        elif int(user_input) < random_nbr:
            print("Plus grand : ")
            user_input = input("Saisie :")
            
        elif int(user_input) == random_nbr:
            print("Vous avez gagné !")
            break
    
if user_input == 'q':
    print("La réponse était : ", random_nbr)
