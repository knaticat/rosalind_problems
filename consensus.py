# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:57:13 2020

@author: HP-PC
"""

from Bio import SeqIO
arr = [seq_record.seq for seq_record in SeqIO.parse(r"C:\Users\DELL\Downloads\rosalind_cons(3).txt", "fasta")]
n= len(arr[0])
freq_matrix = {base: [0]*n for base in 'ACGT'}

for dna in arr:
    for index,base in enumerate(dna):
        freq_matrix[base][index]+=1
consensus = ''
for i in range(n):
        max_freq = -1
        max_freq_base = None
        
        for base in 'ACGT':
            if freq_matrix[base][i] > max_freq:
                max_freq = freq_matrix[base][i]
                max_freq_base = base
        consensus+= max_freq_base
print(consensus)

for key, value in freq_matrix.items():
    print(key ,  ' '.join(map(str, value)))


    