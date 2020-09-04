def sumList(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0]+sumList(numlist[1:])
print(sumList([1,2,3,4,5,6,7,8]))