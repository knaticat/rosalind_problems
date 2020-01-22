# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 12:27:11 2020

@author: HP-PC
"""

def mendel(k,m,n):
    prob = ((k*k - k + 2*(k*m + k*n)) + (0.75*(m*m - m) + m*n))/((k+m+n)*(k+m+n-1))
    return prob