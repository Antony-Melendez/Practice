'''
Programmer : Antony Melendez
Description: Python Program to check if a Number is Odd or Even
Program 1 : 

Date: 09/22/2020
'''

numberInput = int(input(" Please Enter any Integer Value : "))

if(numberInput % 2 == 0):
    print("{0} is an Even Number".format(numberInput))
else:
    print("{0} is an Odd Number".format(numberInput))
