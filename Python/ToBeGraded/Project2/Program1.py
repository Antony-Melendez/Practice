'''
Progrmmer: Antony Melendez
Description: Calculate the federal tax, state tax and the net salary for one employee.
Date: 10/6/20
'''

state = input(
    "Please enter the state you live in (CA, NV, WA, AZ )").capitalize()
grossSalary = float(input("Please enter your gross salary: "))

if(grossSalary >= 100000):
    print("Federal tax is 20 percent")
    federalTax = 20 
    
else:
    print("Federal tax is 15 percent")
    federalTax = 15
    

if(state == "AZ" or state == "WA" or state == "NV" or state == "CA"):
    print("Your state tax is 10 percent")
    stateTax = 10
    
else:
    print("Your state tax is 12 percent")
    stateTax = 12
   
totalTax = federalTax - stateTax

netSalary = grossSalary / totalTax

print("Your net salary is: $ " + str(netSalary))
