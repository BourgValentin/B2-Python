#!/usr/bin/python3.6

####################
#Ce script permet de créer un dictionnaires associant un prénom et une note, puis de calculer la
#moyenne des notes
#
#Il est possible d'arreter la saisie avec 'q'
###################

import re

pattern = re.compile('^[a-zA-Z]*$')
pattern_note = re.compile('^(([0-9])|(1[0-9])|20)$')

somme = 0
count = 0
dico={}
prenom = ""
note = ""

while prenom != "q":

        prenom=input("Prénom ? ")
        note=input("Note ? ")
        if not pattern.match(prenom):
                prenom=input("Prénom ? ")

        elif not pattern_note.match(note):
                note=input("Note ? ")
        else:
                dico[prenom] = note
print(dico)

print(count)
