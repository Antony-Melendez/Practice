"""
Programmer: Antony Melendez
Descriptions: Write a program to determine the drink size based on the letter the user enters
Date: 10-17-20
"""
# variables / str
sSize = " Small Size "
mSize = " Medium Size "
lSize = " Large Size "

# Greet user && show sizes
print("Welcom! \n***********************************************************")

print("S: {}".format(sSize))
print("M: {}".format(mSize))
print("L: {}".format(lSize))

print("\n***********************************************************")

# Take user input
while(True):
    userChoice = input("What size would you like ? :").upper()

    if userChoice == 'S':
        print("You have ordered a:" + sSize + "drink" + " ,the price multiplier is 1")
        break

    elif  userChoice == 'M':
        print("You have ordered a:" + mSize + "drink" + " ,the price multiplier is 2")
        break

    elif  userChoice == 'L':
       print("You have ordered a:" + lSize + "drink" + " ,the price multiplier is 3")
       break
    
    else:
        print("Invalid drink size try again: ")
        continue

# print user choice
print("You have ordered a:" , userChoice)

print("\n***********************************************************")
#Program ends 
