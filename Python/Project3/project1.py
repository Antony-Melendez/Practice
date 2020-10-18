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
Chips_1, crips_1_Price = "Café au Lait", 1.00
Chips_2, crips_2_Price = "Latte ", 2.00

print("Welcome! \n***************************************************")
money = float(input("Please insert money $: "))

print("your total is : $" + str(money) +
      "\n***************************************************")
change = money
# show all options
print("Item: {}, Price {} ".format(drink_1, drink_1_Price))
print("Item: {}, Price {} ".format(drink_2, drink_2_Price))
print("Item: {}, Price {} ".format(Chips_1, crips_1_Price))
print("Item: {}, Price {} ".format(Chips_2, crips_2_Price))


# Asking the user to make a selection.
while change > 0:
    customer_choice = input(
        "What would you like to buy? \n*************************************************** \n")

    if customer_choice == "Coca_Cola" or customer_choice == "coca cola" and change >= drink_1_Price:
        print("You have chosen a", drink_1,
              "these cost", drink_1_Price, "each,")
        change = round((change - drink_1_Price), 2)
        print("You have this much money remaining: $", change)

    elif customer_choice == "Pepsi" or customer_choice == "pepsi" and change >= drink_2_Price:
        print("You have chosen a", drink_2,
              "these cost", drink_2_Price, "each,")
        change = round((change - drink_2_Price), 2)
        print("You have this much money remaining: $", change)

    else:
        print("Insufficient funds, no sale!")