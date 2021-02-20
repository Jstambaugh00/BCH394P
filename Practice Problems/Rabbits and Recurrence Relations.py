# Rabbits and Reoccurrence
# Jacob Stambaugh
# 2/20/2021

# Problem:
'''A sequence is an ordered collection of objects (usually numbers), which are allowed to repeat. Sequences can be finite
or infinite. Two examples are the finite sequence (π,−2–√,0,π) and the infinite sequence of odd numbers (1,3,5,7,9,…).
We use the notation an to represent the n-th term of a sequence.

A recurrence relation is a way of defining the terms of a sequence with respect to the values of previous terms. In the
case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were alive the previous
month, plus any new offspring. A key observation is that the number of offspring in any month is equal to the number of
rabbits that were alive two months prior. As a result, if Fn represents the number of rabbit pairs alive after the n-th
month, then we obtain the Fibonacci sequence having terms Fn that are defined by the recurrence relation Fn=Fn−1+Fn−2
(with F1=F2=1 to initiate the sequence). Although the sequence bears Fibonacci's name, it was known to Indian
mathematicians over two millennia ago.

When finding the n-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation to
generate terms for progressively larger values of n. This problem introduces us to the computational technique of
dynamic programming, which successively builds up solutions by using the answers to smaller cases.'''

# Sample Input:
# 5 3

# Sample Output:
# 19

'''
1:1
2: 1 
3: 4 = 1 +3*1
4: 7= 4 + 3*1
5: 19 = 12+7 
'''

def wascally_rabbit(txt):
    # read in inputs from file
    line = txt.readline()
    line=line.strip('\r\n')
    line  = line.split(' ')
    n=int(line[0])
    k=int(line[1])

    # memory of past relations
    rabbit_dict={1:1,2:1}
    ans=rec(3,n,k,rabbit_dict)
    return rabbit_dict

def rec(i,n,k,rabbit_dict):
    # base case
    if i==n:
        f1 = rabbit_dict.get(i - 1)
        f0 = rabbit_dict.get(i - 2)
        rabbit_dict.update({n: f1 + k * f0})
        return

    # recursion

    f1 = rabbit_dict.get(i - 1)
    f0 = rabbit_dict.get(i - 2)
    rabbit_dict.update({i: f1 + k * f0})
    return rec(i+1,n,k,rabbit_dict)

file = open('input.txt')
ans=(wascally_rabbit(file))
print(ans.get(30))