#选择排序
def selectionSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        maxpos = 0
        for pos in range(1,passnum+1):
            if alist[pos]>alist[maxpos]:
                maxpos = pos
        alist[pos],alist[passnum] = alist[passnum],alist[pos]