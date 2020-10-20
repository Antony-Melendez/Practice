'''
Programmer: Antony Melendez 
Description: making a bending machine with python
Date: 10/16/20
'''

# variables / item list
money = 0
change = money

drink_1, drink_1_Price = "Espresso ", 1.00
drink_2, drink_2_Price = "Americano ", 1.00
drink_3, drink_3_Price = "Café au Lait", 1.00
drink_4, drink_4_Price = "Latte ", 2.00

print("Welcome! \n***************************************************")
money = float(input("Please insert money $: "))

print("your total is : $" + str(money) +
      "\n***************************************************")
change = money
# show all options
print("Item: {}, Price {} ".format(drink_1, drink_1_Price))
print("Item: {}, Price {} ".format(drink_2, drink_2_Price))
print("Item: {}, Price {} ".format(drink_3, drink_3_Price))
print("Item: {}, Price {} ".format(drink_4, drink_4_Price))