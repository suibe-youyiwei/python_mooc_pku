# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:09:46 2020

@author: admin
"""
import time
def fun_sum(n):
    start = time.time() #time函数可以表示当前时间
    sum_num = 0
    for _ in range(1,n+1):
        sum_num+=_
    end = time.time()
    need = end - start
    return sum_num,need

print(fun_sum(100000)[1])
