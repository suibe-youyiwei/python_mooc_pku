# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:31:24 2020

@author: admin
"""
#挨个确认
def bool_1(s1,s2): 
    ls1 = list(s1)
    ls2 = list(s2) #进行两个列表的复制
    result = True
    for _ in ls1:
        if _ not in ls2:
            result = False
            break
        else:
            ls2.pop(ls2.index(_))
    return result
print(bool_1("python","typhon"))
#算法复杂度： 1+2+3+...+n = O(n^2)
#两重循环，第一重遍历s1，遍历n次；第二重循环遍历s2，遍历n次


#排序确认
def bool_2(s1,s2):
    ls1 = list(s1)
    ls2 = list(s2)
    result = True
    ls1.sort()
    ls2.sort()
    _ = 0
    while _<len(ls1) and result:
        if ls1[_] == ls2[_]:
            _+=1
        else:
            result = False
    return result

print(bool_2("python","typhon"))
#算法复杂度：O(nlogn)
#一重循环，只遍历一遍
#sort()函数的算法复杂度没有考虑，排序算法复杂度O(nlogn)

#暴力法，n!增长速度过快，没有必要

#计数比较法，为26个字母设计一个计数器，最后对比两个计数器是否相同
def bool_4(s1,s2):
    c1 = [0]*26
    c2 = [0]*26
    for _ in range(len(s1)):
        i = ord(s1[_]) - ord("a")
        c1[i]+=1
    for _ in range(len(s1)):
        i = ord(s2[_]) - ord("a")
        c2[i]+=1
    j = 0
    result = True
    while j<len(c1) and result:
        if c1[j] == c2[j]:
            j+=1
        else:
            result = False
    return result
print(bool_4("python","typhon"))
#算法复杂度：O(n)
#两个循环对于字符串进行计数，操作次数为n，第三个循环操作次数为26，总复杂度2n+26
       

    