# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:16:19 2020

@author: admin
"""
def fun_O1(n):
    a = 5
    b = 6
    c= 10
    for i in range(n):
        for j in range(n):
            x = i*i
            y = j*j
            z = i*j
    for k in range(n):
        w = a*k+45
        v = b*b
    d = 33
    return x,y,z,w,v,d

print(fun_O1(10))