#冒泡排序
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]

#冒泡排序改进，如果有一趟比对没有发生交换，则排序结束
def shortBubbleSort(alist):
    exchange = True
    passnum = len(alist)-1
    while passnum>0 and exchange:
        for i in range(passnum):
            exchange = False
            if alist[i]>alist[i+1]:
                exchange = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        passnum-=1