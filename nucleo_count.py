# -*- coding: utf-8 -*-
"""
Spyder Editor
author: biotik
"""
def SeqCounter(Seq):
    a,g,t,c=0,0,0,0
    
    for i in range(len(Seq)):
        if Seq[i]=="A":
            a+=1
        elif Seq[i]=="G":
            g+=1 
        elif Seq[i]=="T":
            t+=1
        elif Seq[i]=="C":
            c+=1
        else:
            print("Sequence Invalid")
            break
    return print(str(a)+" "+str(c)+" "+str(g)+" "+str(t))       


