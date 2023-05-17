# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Omar Flores
# Creation Date: 5/9/23
# Below is a simple program with several errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = ''
        
        #the whole while block should not be indented. Try deleting the indentation
    while cave != '1' and cave != '2':
      print('Which cave will you go into? (1 or 2)')
      #needs to have text to promp the user to input something. Try adding ': '
      cave = input(': ')
      #cave = input()
#while cave != '1' and cave != '2':
            #print('Which cave will you go into? (1 or 2)')
            #cave = input()
    #should not be an s in cave
    return cave
    #return caves
#def checkCave(chosenCave):
#change the value to cave because that's what the cave is set to.
def checkCave(cave):
    print('You approach the cave...')
    #sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    #sleep for 2 seconds
    time.sleep(3)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    #sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

    #if chosenCave == str(friendlyCave):
    # chosenCave should be cave so that it matches up with the cave input.
    if cave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        #print 'Gobbles you down in one bite!'
        # the print words need to have a parenthesis. Try adding () around 'Gobbles you down in one bite!'.
        print ('Gobbles you down in one bite!')

displayIntro()
#chooseCave() needs an uppercase C and needs to be isolated to call the function
chooseCave()
#caveNumber = choosecave()
#caveNumber could be cave because that is what the variable is called we set earlier.
#set a default value for cave '' so that the code can run.
cave = ''
checkCave(cave)
#checkCave(caveNumber)
    
print("Thanks for planing")
