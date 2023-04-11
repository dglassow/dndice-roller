#/*******************************************************************************\
#|                                                                               |
#| - Created by D.Glassow & J. Weathers                                          |
#|                                                                               |
#| - any variable or function inside will be available from any of your scripts. |
#|                                                                               |
#\*******************************************************************************/
import random

# take user input for party size
pSize = input("Enter party size: ")
pSize = int(pSize)

# take user input for monster party size
mSize = (input("Enter monster party size: "))

#Prompt user: Enter players
pMembers = []
initiative = []
players = {'Name': [pMembers], 'roll': [initiative]}

for i in range(pSize):
  pName = input("Enter player name: ")
  pMembers.append(pName)


# Prompt user: Roll for party? Y/N
  #If No, take user imput for party values

while True:
  roll = input("Roll for party? Y/N: ")
  if roll.upper() == "Y":
    print("Rolling for party")
    for i in range(pSize):
      rolls = random.randrange(1,20)
      initiative.append(rolls)
    break

  elif roll.upper() == "N":
    for i in range(pSize):
      rolls = input("Please enter initiative for " + pMembers[i] + ':')
      initiative.append(rolls)
    break
  else:
    print('Invalid Entry')
    break

for i in range(pSize):
  print(pMembers[i], initiative[i])
# Roll for monsters
# Save all values to an array & sort by turn


#/*******************************************************************************\
#|                                                                               |
#| End sciprt                                                                    |
#|                                                                               |
#\*******************************************************************************/
# TO DO
# Include monster stats and execute combat rolls
