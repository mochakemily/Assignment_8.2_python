# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <Emily Mochak>
# Creation Date: <9/22/2020>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you,
    	you see two caves. In one cave, the dragon is friendly
    	and will share his treasure with you. The other dragon
    	is greedy and hungry, and will eat you on sight.''')
    print()

def chooseCave():
#cave = ''
#while cave != '1' and cave != '2':
     cave = ''
     while cave != '1' and cave != '2':
#indentation was off - 1
#print('Which cave will you go into? (1 or 2)')
#cave = input()
          print('Which cave will you go into? (1 or 2)')
          cave = input()
#indentation was off
#return caves

     return cave
#needed to return a single cave

def checkCave(chosenCave):
    #print('You approach the cave...')
      print('You approach the cave...')
    #sleep for 2 seconds
      time.sleep(2)
    #print('It is dark and spooky...')
      print('It is dark and spooky...')
    #sleep for 2 seconds
#time.sleep(3)
      time.sleep(2)
#needed to be 2 and not 3 - 4
    #print('A large dragon jumps out in front of you! He opens his jaws and...')
      print('A large dragon jumps out in front of you! He opens his jaws and...')
    #print()
      print()
    #sleep for 2 seconds
    #time.sleep(2)
      time.sleep(2)
    #friendlyCave = random.randint(1, 2)
      friendlyCave = random.randint(1, 2)
#indentation for this whole section is off


      if chosenCave == str(friendlyCave):
            print('Gives you his treasure!')
      else:
#print
#('Gobbles you down in one bite!')
            print("Gobbles you down in one bite!")
#print statement needed to be on one line

playAgain = 'yes'

#while playAgain == 'yes' or playAgain = 'y':
while playAgain == 'yes' or playAgain == 'y':
#second playAgain needed another =
      displayIntro()
#caveNumber = choosecave()
      caveNumber = chooseCave()
#The c in Cave needed to be upper case
      checkCave(caveNumber)

      print('Do you want to play again? (yes or no)')
      playAgain = input()
      if playAgain == 'no':
#print("Thanks for planing")
         print("Thanks for playing!")
#playing was mispelled