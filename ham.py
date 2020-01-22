# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 12:44:35 2020

@author: HP-PC
"""

from Bio.Seq import Seq

def hamming_distance(s,t):
    counter=0
    first_seq = Seq(s)
    second_seq = Seq(t)
    
    for i in range(len(first_seq)):
        if first_seq[i]!= second_seq[i]:
            counter+=1
        else: continue
    return counter