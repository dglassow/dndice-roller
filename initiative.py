#/*******************************************************************************\
#|                                                                               |
#| - Created by D.Glassow & J. Weathers                                          |
#|                                                                               |
#| - any variable or function inside will be available from any of your scripts. |
#|                                                                               |
#\*******************************************************************************/


# take user input for party size
pSize = input("Enter party size: ")
print('Party size is: ' + pSize)

# take user input for monster party size
mSize = (input("Enter monster party size: "))
print('Monster size is: ' + mSize)
# Prompt user: Roll for party? Y/N
  #If No, take user imput for party values
pMembers = []

while True:
 roll = input("roll for party? Y/N: ")
 if roll.upper() == "Y":
     print()
     print("Rolling for party")
     print()
     exit()

 elif roll.upper() == "N":
     print("__________________________")
     roll = input("Please enter party order ")
     exit()
 else:
     continue

# Roll for monsters
# Save all values to an array & sort by turn



#/*******************************************************************************\
#|                                                                               |
#| End sciprt                                                                    |
#|                                                                               |
#\*******************************************************************************/
# TO DO
# Include monster stats and execute combat rolls
