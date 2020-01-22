# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 18:59:07 2020

@author: HP-PC
"""

def bad_char_table(pattern):
    badchar = {}
    for i in range(len(pattern)):
        a = pattern[i]
        badchar.setdefault(a,-1)
        badchar[a]=i
    return badchar

def good_suffix_preprocess1(pattern,shift,bpos):
    m = len(pattern)
    j = m+1
    i = m
    bpos[i] = j
    
    while i>0:
        while j<=m and pattern[i-1]!=pattern[j-1]:
            if shift[j]==0:
                shift[j]=j-i
            j= bpos[j]
        i-=1
        j-=1
        bpos[i]= j
def good_suffix_preprocess2(pattern, shift, bpos):
    m = len(pattern)
    j= bpos[0]
    for i in range(m+1):
        if shift[i]==0:
            shift[i]= j
        if i==j:
            j= bpos[j]
            
def search(text,pattern):
    s=0
    m = len(pattern)
    n= len(text)
    bpos= [0]*(m+1)
    shift = [0]*(m+1)
    
    badchar = bad_char_table(pattern)
    good_suffix_preprocess1(pattern,shift,bpos)
    good_suffix_preprocess2(pattern,shift,bpos)
    
    while s<=n-m:
        j = m-1
        while j>= 0 and pattern[j]== text[s+j]:
            j-=1
        if j<0:
            print(s+1)
            s+=shift[0]
        else:
            s+= max(shift[j+1], j - badchar.get(text[s+j],0)) 