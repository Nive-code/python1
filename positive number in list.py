# This is a Python program to print all positive numbers in a range (Task2)

numList = []

Number = int(input("Please enter the Total number of list Elements: "))
for i in range(1,Number + 1):
    value = int(input("Please enter the value of %d Element : " %i))
    numList.append(value)
print("\nPositive Number in this list are : ")
for j in range(Number):
    if(numList[j] >= 0):
        print(numList[j], end = ' ')
