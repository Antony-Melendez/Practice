'''
Progrmmer: Antony Melendez
Description: score an exam 
Date: 10/6/20
'''
#inputs 
exam1 = int(input("Enter the score fro the first exam: "))
exam2 = int(input("Enter the score froe the second exam: "))
exam3 = int(input("Enter the score for the second exam: "))

#Find Average score
averageScore = (exam1 + exam2 + exam3) / 3

#Calculate grade
if(averageScore >= 98 and 100):
    print("Grade: A+")
elif(averageScore >= 95 and 97):
    print("Grade: A")
elif(averageScore >= 91 and 94):
    print("Grade: A-")
elif(averageScore >= 88 and 90):
    print("Grade: B+")
elif(averageScore >= 84 and 87):
    print("Grade: B")
elif(averageScore >= 80 and 83):
    print("Grade: B-")
elif(averageScore >= 75 and 79):
    print("Grade: C+")
elif(averageScore >= 70 and 74):
    print("Grade: C")
elif(averageScore >= 60 and 70):
    print("Grade: C")
elif (averageScore <= 60):
    print("Grade: NC")

#Print average score 
print(averageScore)