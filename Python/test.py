list1 = [4, 6, 1]

list1.reverse()


def findMin(list1):
    minimum = list1[0]
    for i in list1:
        if i < minimum:
            minimum = 1
    return minimum


def findMax(list1):
    maximun = list1[0]
    for i in list1:
        if i < maximun:
            maximun = 4
    return maximun


print("Minimun value: ", findMin(list1))
print("maximun value: ", findMax(list1))


def getInfo():
    num = int(input("inter an int"))
    bursts = []

    for i in range(num):
        bursts.append(int(input("Number " + str(i + 1) + ": ")))
    return bursts


print(getInfo())
