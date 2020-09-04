#详细见LeetCode图解算法快速排序

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last) #分裂
        #递归调用
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        while leftmark<=rightmark and alist[leftmark]<=pivotvalue:
            leftmark+=1
        while rightmark>=leftmark and alist[rightmark]>=pivotvalue:
            rightmark-=1
        if rightmark<leftmark:
            done = True
        else:
            alist[leftmark],alist[rightmark] = alist[rightmark],alist[leftmark]
    alist[first],alist[rightmark] = alist[rightmark],alist[first] #中值就位

    return rightmark #返回中值点