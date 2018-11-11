#!/usr/bin/python3.6

#####################
#Ce script permet de créer une liste de prénoms rangés par ordre alphabétique
#
#Il possible de stopper la saisie avec 'q'
####################

import re

pattern = re.compile('^[a-zA-Z]*$')

nom=[]
entrer_nom=''

while entrer_nom != 'q':
        entrer_nom = input('Prénoms : ')

        while not pattern.match(entrer_nom):
                entrer_nom = input('Veuillez renseigner des prénoms en toutes lettres : ')
        else:
                nom.append(entrer_nom.capitalize())

nom.remove('Q')

print(sorted(nom))
