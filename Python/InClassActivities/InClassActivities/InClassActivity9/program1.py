'''
Programmer: Antony Melendez
Description: write a program to ask 5 users for their gender and age. Print the total number of users that their
age is under or 40 years old and are female or they are male and older than or 25 years old.
Date:10-27-20
'''


def userInformantion():
    for i in range(5):
        gender.append(input("What is your gender ? F/M ").upper())
        age.append(int(input("How old are? ")))


def requirements():
    count = 0
    for i in range(5):
        if ((age[i] <= 40 and gender[i] == 'F') or (gender[i] == 'M' and age[i] >= 25)):
            count += 1
    return count


def main():
    global gender
    global age
    gender = []
    age = []
    userInformantion()

    print(gender)
    print(age)
    print("The total count of users that meet our requirements is: ", requirements())


main()
