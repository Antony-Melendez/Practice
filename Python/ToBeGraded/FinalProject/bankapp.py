''''
Programmer: Antony Melendez

Description: this code is to emulate a bank app by being able to log in new user or existing users
and being able to deposit mondey or withdraw money from existing accounts

Date: 11-17-2020

'''

f_read = open("UserInformtion.txt", 'r')

Usernames = []
passWords = []
balences = []

for i in f_read:
    infoList = i.split()
    Usernames.append(infoList[0])
    passWords.append(infoList[1])
    balences.append(infoList[2])

    print(Usernames)
    print(passWords)
    print(balences)


def userVerification():
    userNameInput = input("Enter your username: ")
    if userNameInput in Usernames:
        userpasswordInput = input(userNameInput + " Enter your password: ")

    if userpasswordInput in passWords:
        LoggedIn(userNameInput)
    else:
        print("Wrong Information try again: ")


def LoggedIn(userNameInput):
    print("Welcome! " + userNameInput)


userVerification()
