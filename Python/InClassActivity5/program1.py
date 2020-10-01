#Programmer: Antony Melendez
#Description: program to accept the food expenses of 3 Guests (one at a time). Using Accumulation concept, calculate and display the total expenses from all  3 guests combined. 
#Date: 10/1/20

guests = 0
total = 0
while(guests <= 3):
    name = input("Enter the guests name: ")
    expenses = float(input("Enter the expenses for the "+ name +": $ "))
    total = total + expenses
    guests += 1
    print("total", round(total,2))
    
print(total)