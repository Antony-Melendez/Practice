'''
Programmer: Antony Melendez
Description:When user choose the options 1-4, the appropriate functions will be called to do addition, subtraction, Multiplication, and Division or quit the program.
Date:10-27-20

Welcome to calculator.py
your options are:
 
1) Addition
2) Subtraction
3) Multiplication
4) Division
5) Quit calculator.py

'''


def validationUserInput():
    while(True):
        try:
            option = int(input(
                "welcome to calculator.py \n your options are: \n1)addition \n 2)subtraction\n 3)multiplication \n4)Divition \n5)Quit calculator.py \nChoose your option: \n "))
            return option

        except:
            print("Wrong input... input was not an integer")
            continue


def rangeValidation(option):
    while(option <= 0 or option > 5):
        print("not within the range try again... 1-5")
        option = int(input("welcome to calculator.py \n your options are: \n1)addition \n 2)subtraction\n 3)multiplication \n4) Divition \n5)Quit calculator.py \nChoose your option: \n "))

    validationUserInput(option)
    return option


def addition(number1, number2):
    add = number1 + number1
    return add


def subtraction(number1, number2):
    sub = number1 - number2
    return sub


def multiplication(number1, number2):
    mult = number1 * number2
    return mult


def divition(number1, number2):
    div = number1 / number2
    return div


def Main():
    answer = "YES"
    while(answer == "YES"):
        option = validationUserInput()

        if(option >= 1 and option <= 4):
            num1 = int(input("Please enter the first int number: "))
            num2 = int(input("Please enter the second int number: "))

            if option == 1:
                print(num1, " + ", num2, " = ", addition(num1, num2))

            elif option == 2:
                print(num1, " - ", num2, " = ", subtraction(num1, num2))

            elif option == 3:
                print(num1, " * ", num2, " = ", multiplication(num1, num2))

            elif option == 4:
                print(num1, " / ", num2, " = ", divition(num1, num2))
        else:
            option == 5
            exit()

        answer = input("Do you want to continue? YES/NO ").upper()
        print("Goodbye")


Main()
