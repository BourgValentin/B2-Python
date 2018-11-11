#!/usr/bin/python3.6

import re
import random

pattern = re.compile("^[1-9][0-9]?$|^100$")

def win():
    launch = open('2a-mol-launch.txt', 'w')
    launch.write("Félicitations vous avez gagné !")
    launch = open('2a-mol-launch.txt', 'r')
    print(launch.read())
    
random_nbr = random.randint(1,100)

launch = open('2a-mol-launch.txt','w')
launch.write("Vous devez trouvez un nombre 1 et 100 :")

launch = open('2a-mol-launch.txt','r')
print(launch.read())

launch = open('2a-mol-launch.txt','w')
launch.write(input('Nombre : '))

launch = open('2a-mol-launch.txt','r')
launch_input = launch.read()


while pattern.match(launch_input):

        if int(launch_input) < random_nbr:
            launch = open('2a-mol-launch.txt', 'w')
            launch.write("Plus")
            launch = open('2a-mol-launch.txt', 'r')
            print(launch.read())
            launch = open('2a-mol-launch.txt', 'w')
            launch.write(input('Nombre : '))
            launch = open('2a-mol-launch.txt', 'r')
            launch_input = launch.read()
            launch.close()

        elif int(launch_input) > random_nbr:
            launch = open('2a-mol-launch.txt', 'w')
            launch.write("Moins")
            launch = open('2a-mol-launch.txt', 'r')
            print(launch.read())
            launch = open('2a-mol-launch.txt', 'w')
            launch.write(input('Nombre : '))
            launch = open('2a-mol-launch.txt', 'r')
            launch_input = launch.read()
            launch.close()

        elif int(launch_input) == random_nbr: 
            break

if pattern.match(launch_input) and int(launch_input) == random_nbr:
    win()

while not pattern.match(launch_input):
    
    launch = open('2a-mol-launch.txt', 'w')
    launch.write('Veuillez saisir un nombre')
    launch = open('2a-mol-launch.txt', 'r')
    print(launch.read())
    launch = open('2a-mol-launch.txt', 'w')
    launch.write(input('Nombre : '))
    launch = open('2a-mol-launch.txt', 'r')
    launch_input = launch.read()
    
                
    
