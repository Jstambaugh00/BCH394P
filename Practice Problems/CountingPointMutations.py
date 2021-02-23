# Identifying Unknown DNA Quickly
# Jacob Stambaugh
# 2/23/2021

# Problem:
'''
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of
corresponding symbols that differ in s and t. See Figure 2.

Given: ATwo DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
'''

# Sample Input:
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT

# Sample Output
# 7

def count_mutations(string1,string2):
    count = 0
    for i in range(len(string1)):
        if string1[i]!=string2[i]:
            count+=1
    return count


# Driver code
file = open('input.txt')
string1 = file.readline()
string2 = file.readline()
string1 = string1.strip('\r\n')
string2 = string2.strip('\r\n')

ans=count_mutations(string1,string2)
print(ans)
