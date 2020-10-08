'''
Programer: Antony  Melendez
Description:
Date: 
'''

weatherCondition = input("How is the weather today? (rainy/ sunny/ windy)").lower().strip()

if (weatherCondition =="rainy"):
    print("take an amberela")
elif(weatherCondition =="sunny"):
    print("===wear sunglasses===")
elif(weatherCondition =="windy"):
    print("+++ take your hat +++")
else:
    print("stay home")
    print("exiting the program")