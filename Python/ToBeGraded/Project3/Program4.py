"""
Programmer: Antony Melendez
Descriptions: Write a program that combines programs 1 through 3 into one vending machine user interface program
Date: 10-18-20
"""
# variables
drink_1 = "Espresso"
drink_2 = "Americano"
drink_3 = "Café au Lait"
drink_4 = "Latte"

sSize = 1.75
mSize = 3.50
lSize = 5.25

userMoney = 0
changeMoney = 0

print("Welcom! \n***********************************************************")
# show all options
print('1', drink_1, '(', 'small: $', sSize, 'Medium: $',
      mSize, 'Large: $', lSize, ')')
print("\n")
print('2', drink_2, '(', 'small: $', sSize, 'Medium: $',
      mSize, 'Large: $', lSize, ')')
print("\n")
print('3', drink_3, '(', 'small: $', sSize, 'Medium: $',
      mSize, 'Large: $', lSize, ')')
print("\n")
print('4', drink_4, '(', 'small: $', sSize, 'Medium: $',
      mSize, 'Large: $', lSize, ')')

print("\n***********************************************************")
# Take user input && print user choice

while(userMoney <= 0):
    userChoicePick = input("What would you like ? (1-4) :")

    if userChoicePick == '1':
        print("you have picked a :" + drink_1)
    elif userChoicePick == '2':
        print("you have picked: " + drink_2)
    elif userChoicePick == '3':
        print("you have picked: " + drink_3)
    elif userChoicePick == '4':
        print("you have picked: " + drink_4)
    else:
        print("Invalid number")
        continue

    userChoiceSize = input("What size would you like? (S-M-L)").capitalize()

    if userChoiceSize == 'S':
        print("you have picked small size")
        print("Please enter: " + str(sSize))
        userMoney = float(input(":"))
        changeMoney = userMoney - sSize
        if userMoney <= sSize:
            print("Insufficient funds, no sale! ")
            print("would you like to try again? Y/N")
            userChoiceContinue = input("").capitalize()
            if userChoiceContinue == 'Y':
                print("Please enter: " + str(sSize))
                userMoney = float(input(":"))
                changeMoney = userMoney - sSize
            elif userChoiceContinue == 'N':
                print("Have a nice day")
            else:
                continue
    if userChoiceSize == 'M':
        print("you have picked small size")
        print("Please enter: " + str(mSize))
        userMoney = float(input(":"))
        changeMoney = userMoney - mSize
        if userMoney <= mSize:
            print("Insufficient funds, no sale! ")
            print("would you like to try again? Y/N")
            userChoiceContinue = input("").capitalize()
            if userChoiceContinue == 'Y':
                print("Please enter: " + str(mSize))
                userMoney = float(input(":"))
                changeMoney = userMoney - mSize
            elif userChoiceContinue == 'N':
                print("Have a nice day")
            else:
                continue
    if userChoiceSize == 'L':
        print("you have picked small size")
        print("Please enter: " + str(lSize))
        userMoney = float(input(":"))
        changeMoney = userMoney - lSize
        if userMoney <= mSize:
            print("Insufficient funds, no sale! ")
            print("would you like to try again? Y/N")
            userChoiceContinue = input("").capitalize()
            if userChoiceContinue == 'Y':
                print("Please enter: " + str(lSize))
                userMoney = float(input(":"))
                changeMoney = userMoney - lSize
            elif userChoiceContinue == 'N':
                print("Have a nice day")
            else:
                continue
    else:
        print("Invalid letter")
        continue

print("\n***********************************************************")
# exit program and print recipt
print("- recipt -")
print("your change is: " + str(changeMoney))
print("Thank you – enjoy your drink!")
print("\n***********************************************************")
