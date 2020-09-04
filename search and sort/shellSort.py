#谢尔排序

def shellSort(alist):
    sublistcount = len(alist)//2 #设定间隔
    while sublistcount>0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount) #对子列表进行排序
        sublistcount = sublistcount//2 #间隔缩小

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        pos = i
        while pos>=gap and alist[pos-gap]>currentvalue:
            alist[pos] = alist[pos-gap]
            pos = pos-gap
        alist[pos] = currentvalue