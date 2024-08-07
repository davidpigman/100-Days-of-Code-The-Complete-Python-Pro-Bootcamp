print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("You are at a crossroads. Do you want to go left or right?")
direction = input("Type 'left' or 'right': ")

if direction == "left":
  print("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
  lake = input("Type 'wait' or 'swim': ")
  if lake == "wait":
    print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
    door = input("Type 'red', 'yellow' or 'blue': ")
    if door == "yellow":
      print("You found the treasure! You Win!")
    elif door == "red":
      print("It's a room full of fire. Game Over.")
    elif door == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")



print('''
                     ^`.                     o
     ^_              \  \                  o  o
     \ \             {   \                 o
     {  \           /     `~~~--__
     {   \___----~~'              `~~-_     ______          _____
      \                         /// a  `~._(_||___)________/___
      / /~~~~-, ,__.    ,      ///  __,,,,)      o  ______/    \
      \/      \/    `~~~;   ,---~~-_`~= \ \------o-'            \
                       /   /            / /
                      '._.'           _/_/
                                      ';|\
''')







rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

intUserChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

lstChoices = [0, 1, 2]

intComChoice = random.randint(0, 2)

if intUserChoice == 0:
    strUserChoice = rock
elif intUserChoice == 1:
    strUserChoice = paper
elif intUserChoice == 2:
    strUserChoice = scissors

if intComChoice == 0:
    strComChoice = rock
elif intComChoice == 1:
    strComChoice = paper
elif intComChoice == 2:
    strComChoice = scissors

print(f"User chose {intUserChoice}\n {strUserChoice}")

print(f"Computer chose {intComChoice}\n {strComChoice}")

if intComChoice == 0:
    if intUserChoice == 0:
        strResult = "Tie"
    elif intUserChoice == 1:
        strResult = "Win"
    elif intUserChoice == 2:
        strResult = "Lose"
elif intComChoice == 1:
    if intUserChoice == 0:
        strResult = "Lose"
    elif intUserChoice == 1:
        strResult = "Tie"
    elif intUserChoice == 2:
        strResult = "Win"
elif intComChoice == 2:
    if intUserChoice == 0:
        strResult = "Win"
    elif intUserChoice == 1:
        strResult = "Lose"
    elif intUserChoice == 2:
        strResult = "Tie"

if strResult == "Win":
    print ("You Win!")
elif strResult == "Lose":
    print ("You Lose!")
elif strResult == "Tie":
    print ("Tie, Try again!")





