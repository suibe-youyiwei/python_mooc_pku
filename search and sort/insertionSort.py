#插入排序
def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        pos = index
        while pos>0 and alist[pos-1]>currentvalue:
            alist[pos] = alist[pos-1]
            pos-=1
        alist[pos] = currentvalue