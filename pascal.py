#Copyright Ashrith Kanakanala 2018
finRow = int(input("Please enter the desired Row Number: "))

#Initial Row
curList = [1]

#Variables
curRow = 1
a = 0
b = 1
newList = []
#print(curRow)

while curRow < finRow:
    newList.append(1)
    if len(curList) > 1:
        listNum = len(curList) - 1
        while b <= listNum:
            num = int(curList[a]) + int(curList[b])
            a += 1
            #print("a is",a)
            b += 1
            #print("b is",b)
            newList.append(num)

    newList.append(1)

    a = 0
    b = 1

    curList.clear()
    curList = newList.copy()
    newList.clear()
    curRow += 1
    #print(curList)
print(curList)
