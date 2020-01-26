from Bio import SeqIO
import itertools
my_seq = [str(seq_record.seq) for seq_record in SeqIO.parse(r"C:\Users\DELL\Downloads\rosalind_grph(1).txt", "fasta")]
identifiers = [seq_record.id for seq_record in SeqIO.parse(r"C:\Users\DELL\Downloads\rosalind_grph(1).txt", "fasta")]

data = dict(zip(identifiers,my_seq))

def overlap(s1, s2, k):
    return s1[-k:] == s2[:k]

def check_overlap(data, k):
    output = []
    for a,b in itertools.combinations(data, 2):
        a_str, b_str = data[a], data[b]
        
        if overlap(a_str, b_str, k):
            output.append((a,b))
        if overlap(b_str, a_str, k):
            output.append((b,a))
    return output
