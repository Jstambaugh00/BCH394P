# Transcribing DNA into RNA
# Jacob Stambaugh
# 1/21/2020

# Problem:
'''An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.
Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.'''''

# Sample Input:
# GATGGAACTTGACTACGTAAATT

# Sample Output:
# GAUGGAACUUGACUACGUAAAUU

def rec(s,i):
    # base case
    if i==len(s)-1:
        if s[i]=='T':
            return 'U'
        else:
            return s[i]
    # Recursive
    if s[i]=='T':
        return 'U'+rec(s,i+1)
    else:
        return s[i] + rec(s,i+1)

# Main/Driver Code
s='ATGGAGCTACCATGCTTGCGACATGAAGCCAGTCTAAATCTACCCGTATCGATGTAAATATGGGAGCACCATTGTTGCTCGCCGTTCTCAACCCGGAATGCCTCGAGCGTAGTCACAGATGTTCCGGTTCACTATAGTACCCATCAACAACTAGATAGAATGCACAGTGGGGCACCTTAAATCTATTTATTAGGTCTTTACAGGGTGGTCTGTATACAGTTAGTAGAAGGTGTAAGCACATCTTGGCGATACAGGACGTATTCTGCGATCGCTCTCGGTTGTATCGCATCATAGCGACTGTCCAGACTTCTACAGATCCATTATCCACAGACATAACGTTATTTACGCAAGCGATCGCCCGGACTTTTTTACTGTGGGAAGGAAGTCAGGCTACTCATGCATCAAAAGCGAGCCTATCCATTGCAAAGGCGAAATAACATGGGTTTCGTTACCCCTGGTCGAGTTTACGGACAGAGGGTTATATATTAAACAAAGGAAAGAAACTCGATTCCTTTCAATAATAGGACGGGTCCACATATACAAAGAACACCCTTCATTGTCATATCGGTCATGGACGGGAAGCGAGAGACTTGGTGCCCCAAGCTTGATACGTCACGCTTTTATCCGAAACGAAGTACCCGCGATTTTGCTAAGCAGGGCGGCGAGTTCCAGTGTTACTGTGTAGCTACAGTCTCTTCGCCGTAATGTTTTTAAGATCCTAAGTAATGCGGGATGGATACTCTTGCCATTGTCGGCACCGGACTACCAACATGGACTCTGTCTACGGGTTAAAACAGCACGACACTCAAACGGCCTCAGGGGGTTAGGATGTAAACCACAGCAAACGCGAGGAAGCGGTAGTAGCTAGTTTACTACTTGCTATCATCGATGCGGCACTGGCCTACGAGTTTACGGAAAGGTAGTCCTTCCTAAGCTGCCTGCGAGAGTATGTAAGAAAATCCCCGGCTTGCATAGACATCTTGCATTTTCATCGCACA'
# Save to file
f = open("ans.txt", "x")
f.write(rec(s,0))

# has runtime complexity of O(N)
