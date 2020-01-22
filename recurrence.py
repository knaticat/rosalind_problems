# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:05:12 2020

@author: biotik
"""
def fib(n,k):
    fibo = [0]
    for i in range(1,n+1,1):
        if i <= 2: f = 1
        else: f = fibo[i-1] + k*fibo[i-2]
        fibo.append(f)
    return fibo[n]
