# Identifying Unknown DNA Quickly
# Jacob Stambaugh
# 2/22/2021

# Problem:
'''The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example,
the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is
called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling
information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a
four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows
for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
'''

# Sample Input:
# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
# TCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
# ATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
# TGGGAACCTGCGGGCAGTAGGTGGAAT

# Sample Output:
# Rosalind_0808
# 60.919540


def countGC(string):
    count =0
    le=0
    for i in string:
        le+=1
        if i == 'G' or i == 'C':
            count+=1
    return count,le

def main(file):
    name=None
    count=0
    dnadict={}
    le=0
    for line in file.readlines():
        line=line.strip('\r\n')

        # end prev read and begin new read
        if line[0]=='>':
            # first read
            if name==None:
                line = line.split('>')
                name = line[1]

            else:
                # save prev count
                dnadict.update({name: round((count/le)*100,7)})

                # start new count
                count=0
                le=0
                line=line.split('>')
                name=line[1]

        # read line and update count
        else:
            c,l=countGC(line)
            count=count+c
            le=le+l
    dnadict.update({name: round((count/le)*100,7)})

    top=0
    ind=''
    for i in dnadict.keys():
        if dnadict.get(i)>top:
            ind=i
            top=dnadict.get(i)

    return dnadict

file = open('input.txt')
ans=(main(file))
print(ans)