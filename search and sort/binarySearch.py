#详细见LeetCode刷题二分查找
def binarySearch(alist,item):
    found = False
    left = 0
    right = len(alist)-1
    while left<=right and not found:
        mid = (left+right)//2
        if alist[mid] == item:
            found = True
        else:
            if alist[mid]>item:
                right = mid-1
            else:
                left = mid+1
    return found

#二分法的递归实现
def binarySearch_re(alist,item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist)//2
        if alist[mid] == item:
            return True
        else:
            if alist[mid]>item:
                return binarySearch_re(alist[:mid],item)
            else:
                return binarySearch_re(alist[mid+1:item])