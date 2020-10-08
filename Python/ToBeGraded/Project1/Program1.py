'''
Programmer: Antony Melendez 
Description: Calculating thr gross revenue with the givin fornula
Date: 9/24/20
'''

lName = input("Enter your last name: ")
fName = input("Enter your first name: ")
hWorked = float(input("Ente the total hours worked: "))
hWage = float(input("Enter the hourly wage: "))

gWage = hWorked * hWage

print( fName + ' ' + lName + ' ' + "Your gross wage is: " + str(gWage))