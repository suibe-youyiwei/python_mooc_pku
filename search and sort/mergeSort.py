#归并排序
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        left = alist[:mid]
        right = alist[mid:]
        mergeSort(left)
        mergeSort(right)
        #将左右半部合并
        i = j = k = 0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                alist[k] = left[i]
                i+=1
            else:
                alist[k] = right[j]
                j+=1
            k+=1
        #归并左部分剩余项
        while i<len(left):
            alist[k] = left[i]
            i+=1
            k+=1
        #归并右部分剩余项
        while j<len(right):
            alist[k] = right[j]
            j+=1
            k+=1

def mergeSort_py(alist):
    if len(alist)<=1:
        return alist
    mid = len(alist)//2
    left = mergeSort_py(alist[:mid])
    right = mergeSort_py(alist[mid:])

    #合并左右半部
    merged = []
    while left and right:
        if left[0]<=right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)
    return merged