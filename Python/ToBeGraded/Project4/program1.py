''''
Programmer: Antony Melendez

Description: Create a menu to allow the user to add, insert, remove,
find the maximum, the minimum, and sort the list in descending order
(larger to smaller value). Declare your list as list of string.

Date: 10-30-2020

Options:
1- Add an item to the list
2- Remove an item from the list
3- Insert an item to the list
4- Find maximum
5- Find Minimum
6- Sort the list in descending order
7- Quit the program
'''

# Variables
userNames = []
menuPrices = []

# funtions


# adds names and prices to the lists -- done
def addToList():
    userNumber = int(input("How many name entries will you need? "))
    for i in range(userNumber):
        names = input("Please insert the user names: " +
                      str(i + 1) + ":").capitalize()
        userNames.append(names)

    userNumber = int(input("How many price entries will you need? "))
    for i in range(userNumber):
        prices = input("Please insert the price(s): " +
                       str(i + 1) + ":")
        menuPrices.append(prices)

    print(userNames, menuPrices)


# removes names from the lists -- bug -- when the user removes all the items from the list the program crashes
def removeFromList():
    _removed = int(input(":"))
    del(userNames[_removed])
    print(userNames)

    print(
        "******************************************************************************************")


# inserts new item to index 0 -- done
def insertToList():
    insertingNew = input("where do you want to insert?")
    userNames.insert(0, insertingNew)


# find the mximun in the lists
def findMaximun():
    print(max(userNames))
    print(max(menuPrices))


# find the minimun in the list -- done
def fingMinimum():
    print(min(userNames))
    print(min(menuPrices))


# sorts the list -- done
def sortList():
    userNames.sort(reverse=True)
    menuPrices.sort(reverse=True)
    print(userNames, menuPrices)


# checks if the intput was an integer or not
def validationUserInput():
    print(
        "******************************************************************************************")

    while(True):
        try:
            option = int(
                input("Welcome! \n Your option are: \n 1)Add an item to the list \n 2) Remove an item from the list \n 3) Insert an item to the list \n 4) Find maximum \n 5) Find Minimum \n 6) Sort the list in descending order \n 7) Quit the program\n  choose: "))
            print(
                "******************************************************************************************")
            return option

        except:
            print("Wrong input... input was not an integer")
            continue


# checks if the user enter the correct input from the givin options -- done
def rangeValidation(option):
    while(option <= 0 or option > 7):
        print("not within the range try again... 1-7")
        option = int(input("Welcome!\n Your option are: \n 1)Add an item to the list \n 2) Remove an item from the list \n 3) Insert an item to the list \n 4) Find maximum \n 5) Find Minimum \n 6) Sort the list in descending order \n 7) Quit the program "))

    validationUserInput(option)
    return option


# made this function to close the program and print out goodbye -- done
def endProgram():
    print("Goodbye...")
    exit()


# asks the user what option they want to use -- done
def start():
    answer = "YES"
    while(answer == "YES"):
        option = validationUserInput()
        if option == 1:
            addToList()
        elif option == 2:
            removeFromList()
        elif option == 3:
            insertToList()
        elif option == 4:
            findMaximun()
        elif option == 5:
            fingMinimum()
        elif option == 6:
            sortList()
        elif option == 7:
            endProgram()

    answer = input("Do you want to continue? YES/NO ").upper()


# Calls the start Funtion
start()
