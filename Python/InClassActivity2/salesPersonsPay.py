'''
programmer : Antony Melendez
Description:this program allows the user to enter values for salesperson's base salary,total
Program 2 : SalesPersonPay
Date: 09/17/2020
'''
totalSales = int(input("what is the totalsales per person? "))
commissionRate = float(input("what is the commion Rate? "))
baseSalary = float(input("what is the base Salary ? "))

salePersonPay = baseSalary + (totalSales * commissionRate)
print(salePersonPay)
salePersonPay = round(salePersonPay, 2)
print("salePersonPay: " , salePersonPay)