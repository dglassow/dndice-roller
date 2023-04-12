#/*******************************************************************************\
#|                                                                               |
#| - Created by D.Glassow & J. Weathers                                          |
#|                                                                               |
#| - A simple python script that rolls for initiative according to DnD 5e        |
#|                                                                               |
#\*******************************************************************************/
import random

# take user input for party size
pSize = int(input("Enter party size: "))

# take user input for monster party size
mSize = int(input("Enter monster party size: "))

#Prompt user: Enter players
pMembers = []
initiative = []
players = {'Name': [pMembers], 'roll': [initiative]}

for i in range(pSize):
  pName = input("Enter player name: ")
  pMembers.append(pName)
  modifier = input("Enter initiative mod: ")
  modifier = int(modifier)
  initiative.append(modifier)

# Prompt user: Roll for party? Y/N
  #If No, take user imput for party values

while True:
  roll = input("Roll for party? Y/N: ")
  if roll.upper() == "Y":
    print("Rolling for party")
    for i in range(pSize):
      rolls = random.randrange(1,20)
      modifier = initiative[i]
      rolls = int(rolls + modifier)
      initiative[i] = rolls
    break

  elif roll.upper() == "N":
    for i in range(pSize):
      rolls = input("Please enter initiative for " + pMembers[i] + ':')
      initiative.append(rolls)
    break
  else:
    print('Invalid Entry')
    break

# Roll for monsters
for i in range(mSize):
  print("Rolling for Monsters")
  mNum = str(i + 1)
  monster = "monster" + mNum
  rolls = random.randrange(1,20)
  rolls = int(rolls)
  pMembers.append(monster)
  initiative.append(rolls)

# Save all values to an array & sort by turn
totalPlayers = pSize + mSize

for i in range(totalPlayers):
  print(pMembers[i], initiative[i])


#/*******************************************************************************\
#|                                                                               |
#| End sciprt                                                                    |
#|                                                                               |
#\*******************************************************************************/
# TO DO
# Include monster stats and execute combat rolls
