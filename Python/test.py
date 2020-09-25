'''
Programer: Antony Melendez
Description: Just testing stuff
Date: 09/24/20
'''

mItems = int(input("Enter the number of menu items: "))  # items from menu
dItems = int(input("Enter the number of drinks: "))  # drinks
tip = 0.15  # tip percent
mPrice = 1.75  # menu items price
dPrice = 1  # drinks price

mTotal = mItems * mPrice
dTotal = dItems * dPrice
aTotal = mTotal + dTotal * tip

print("Your total is: $" + str(aTotal))
