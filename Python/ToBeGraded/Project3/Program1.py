"""
Programmer: Antony Melendez
Descriptions: Write a program that displays the various coffee drinks your vending machine offers along with the option number for each drink
Date: 10-16-20
"""
# variables
drink_1, drink_1_Price_Small = "Espresso", 1.75
drink_2, drink_2_Price_Small = "Americano", 1.75
drink_3, drink_3_Price_Small,  = "Café au Lait", 1.75
drink_4, drink_4_Price_Small = "Latte", 1.75

userMoney = 0
changeMoney = 0

print("Welcom! \n***********************************************************")
# show all options
print('1', drink_1, drink_1_Price_Small)
print('2', drink_2, drink_2_Price_Small)
print('3', drink_3, drink_3_Price_Small)
print('4', drink_4, drink_4_Price_Small)
print("\n***********************************************************")
# ask user input

while(True):
    userChoice = input("What would you like ? (1-4) :")

    if userChoice == '1':
        print("Please enter: " + str(drink_1_Price_Small))
        userMoney = float(input(":"))
        changeMoney = userMoney - drink_1_Price_Small
        if userMoney <= drink_1_Price_Small:
            print("Insufficient funds, no sale! ")
            print("would you like to try again? Y/N")
            userChoiceContinue = input("").capitalize()
            if userChoiceContinue == 'Y':
                print("Please enter: " + str(drink_1_Price_Small))
                userMoney = float(input(":"))
                changeMoney = userMoney - drink_1_Price_Small
            elif userChoiceContinue == 'N':
                print("Have a nice day")
            else:
                continue
        break
    elif userChoice == '2':
        print("Please enter: " + str(drink_2_Price_Small))
        userMoney = float(input(":"))
        changeMoney = userMoney - drink_2_Price_Small
        if userMoney <= drink_2_Price_Small:
            print("Insufficient funds, no sale! ")
            print("would you like to try again? Y/N")
            userChoiceContinue = input("").capitalize()
            if userChoiceContinue == 'Y':
                print("Please enter: " + str(drink_2_Price_Small))
                userMoney = float(input(":"))
                changeMoney = userMoney - drink_2_Price_Small
            elif userChoiceContinue == 'N':
                print("Have a nice day")
            else:
                continue
        break
    elif userChoice == '3':
        print("Please enter: " + str(drink_3_Price_Small))
        userMoney = float(input(":"))
        changeMoney = userMoney - drink_3_Price_Small
        if userMoney <= drink_3_Price_Small:
            print("Insufficient funds, no sale! ")
            print("would you like to try again? Y/N")
            userChoiceContinue = input("").capitalize()
            if userChoiceContinue == 'Y':
                print("Please enter: " + str(drink_3_Price_Small))
                userMoney = float(input(":"))
                changeMoney = userMoney - drink_3_Price_Small
            elif userChoiceContinue == 'N':
                print("Have a nice day")
            else:
                continue
        break
    elif userChoice == '4':
        print("Please enter: " + str(drink_4_Price_Small))
        userMoney = float(input(":"))
        changeMoney = userMoney - drink_4_Price_Small
        if userMoney <= drink_4_Price_Small:
            print("Insufficient funds, no sale! ")
            print("would you like to try again? Y/N")
            userChoiceContinue = input("").capitalize()
            if userChoiceContinue == 'Y':
                print("Please enter: " + str(drink_4_Price_Small))
                userMoney = float(input(":"))
                changeMoney = userMoney - drink_4_Price_Small
            elif userChoiceContinue == 'N':
                print("Have a nice day")
            else:
                continue
        break

print("\n***********************************************************")
# exit program and print recipt
print("- recipt -")
print("your change is: " + str(changeMoney))
print("Thank you – enjoy your drink!")
print("\n***********************************************************")
