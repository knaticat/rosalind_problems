# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 19:42:58 2020

@author: HP-PC
"""

def CreateStack():
    stack =[]
    return stack
def Size(stack):
    return len(stack)

def isEmpty(stack):
    if Size(stack)== 0:
        return True
def push(stack, item):
    stack.append(item)
def pop(stack):
    if isEmpty(stack):
        return 
    return stack.pop()


def reverse_compliment(Seq):
    n = len(Seq)
    stack = CreateStack()
    for i in range(0,n,1):
        push(stack,Seq[i])
    Seq = ""
    
    for i in range(0,n,1):
        m = pop(stack)
        if m =="A":
            Seq+= "T"
        elif m == "G":
            Seq+="C"
        elif m == "C":
            Seq+="G"
        elif m=="T":
            Seq+="A"
        else: return print("Error")
    return Seq
    