def uniqueList(numbers):
    newList=[]
    for n in numbers:
        if n not in newList:
            newList.append(n)
    return newList

x=[1, 3, 3, 3, 6, 2, 3, 5]

print(uniqueList(x))
