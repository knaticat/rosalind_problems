# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 12:37:30 2020

@author: HP-PC
"""

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

my_seq= Seq("", IUPAC.unambiguous_rna)
str(my_seq.translate(to_stop = True))