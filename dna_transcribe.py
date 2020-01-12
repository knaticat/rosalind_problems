# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 23:19:32 2020

@author: HP-PC
"""

def dna_transcribe(Seq):
    new = list(Seq)
    for i in range(len(Seq)):
        if new[i]=="T":
            new[i]="U"
    string = ''.join(new)
    return string
            

l = dna_transcribe("AAAGTGTTTTTCC")
print(l)