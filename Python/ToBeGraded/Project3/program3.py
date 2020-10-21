"""
Programmer: Antony Melendez
Descriptions: Write a program that displays the various coffee drinks your vending machine offers along with the option number for each drink
Date: 10-18-20
"""
# variables
drink_1, drink_1_Price_Small, drink_1_Price_Medium, drink_1_Price_Large = "Espresso", 1.75, 3.50, 5.25
drink_2, drink_2_Price_Small, drink_2_Price_Medium, drink_2_Price_Large = "Americano", 1.75, 3.50, 5.25
drink_3, drink_3_Price_Small, drink_3_Price_Medium, drink_3_Price_Large = "Café au Lait", 1.75, 3.50, 5.25
drink_4, drink_4_Price_Small, drink_4_Price_Medium, drink_4_Price_Large = "Latte", 1.75, 3.50, 5.25

print("Welcom! \n***********************************************************")
# show all options
print('1', drink_1, '(', 'small: $', drink_1_Price_Small, 'Medium: $',
      drink_1_Price_Medium, 'Large: $', drink_1_Price_Large, ')')
print("\n")
print('2', drink_2, '(', 'small: $', drink_2_Price_Small, 'Medium: $',
      drink_2_Price_Medium, 'Large: $', drink_2_Price_Large, ')')
print("\n")
print('3', drink_3, '(', 'small: $', drink_3_Price_Small, 'Medium: $',
      drink_3_Price_Medium, 'Large: $', drink_3_Price_Large, ')')
print("\n")
print('4', drink_4, '(', 'small: $', drink_4_Price_Small, 'Medium: $',
      drink_4_Price_Medium, 'Large: $', drink_4_Price_Large, ')')

print("\n***********************************************************")
# Take user input && print user choice
while(True):
    userChoice = input("What would you like ? (1-4):")

    if userChoice == '1':
        print("You have ordered a: " + drink_1)
        break
    elif userChoice == '2':
        print("You have ordered a: " + drink_2)
        break
    elif userChoice == '3':
        print("You have ordered a: " + drink_3)
        break
    elif userChoice == '4':
        print("You have ordered a: " + drink_4)
        break
    else:
        print("Invalid drink try again: ")
        continue

print("\n***********************************************************")
# Program ends
