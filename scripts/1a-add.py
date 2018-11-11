#!/usr/bin/python3.6

######################
#Ce script permet de calculer la somme de 2 nombres
######################

import re

pattern = re.compile('^[0-9]*$')

def ajouter():

    nombre1=input("Veuillez renseigner le premier nombre : ")

    while pattern.match(nombre1) == None:

      print("Veuillez entrer un nombre")
      nombre1=input("Nombre = ")

    else:
      nombre1=(int(nombre1))


    nombre2=input("Veuillez renseigner la seconde valeur à calculer : ")

    while pattern.match(nombre2) == None:

      print("Veuillez entrer un nombre")
      nombre2=input("Valeur : ")

    else:
      nombre2=(int(nombre2))

    print("Résultat = " + str(nombre1+nombre2))

ajouter()
