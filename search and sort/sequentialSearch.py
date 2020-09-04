#顺序查找
def sequentialSearch(alist,item):
    found = False
    pos = 0
    while pos<=len(alist)-1 and not found:
        if alist[pos] == item:
            found = True
        else:
            pos+=1
    return found

#有序表顺序查找
def orderedSequentialSearch(alist,item):
    found = False
    stop = False
    pos = 0
    while pos<=len(alist)-1 and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos]>item:
                stop = True
            else:
                pos+=1
    return found
