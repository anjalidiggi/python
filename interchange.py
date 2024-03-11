def swapList(newList):
    newList[0], newList[-1] = newList[-1], newList[0]

    return newList


# code
newList = [36, 34, 32, 30, 29]
print(swapList(newList))