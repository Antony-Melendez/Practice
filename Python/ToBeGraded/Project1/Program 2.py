'''
Programer: Antony Melendez
Description: Calculate and output Name and the Amount of each person's 
check including 15% tip.
Date: 9/24/20
'''

name = input("input your name: ")
mItems = int(input("Enter the total amount of menu items: "))
aDrinks = int(input("Enter the total amount of drinks: "))
tip = 0.15 #the 15% tip 

total = mItems + aDrinks * tip

print(name + " your total is: " + "$" + str(total))