def HelloWorld():
    print("Hello World")

def problem1():
    # Calculate hypotnuse
    a=int(input('enter number 1 '))
    b=int(input('enter number 2 '))
    c=(a**2+b**2)
    print("Hypotonuse is:",c)

def problem2():
    # String splitting + concat
    s=input('Enter String ')
    nums = list(map(int, input("\nEnter the numbers : ").strip().split()))[:4]
    print(s[nums[0]:nums[1]+1] , s[nums[2]:nums[3]+1])

def problem3():
    # loops :D
    nums = list(map(int, input("\nEnter the numbers : ").strip().split()))[:2]
    sum=0
    for i in range(nums[0],nums[1]+1):
        if i%2==0:
            continue
        else:
            sum=sum+i
    print(sum)
def problem4():
    # read file contents
    i=1
    f = open("hw1.txt", "r")
    for lines in f.readlines():
        if i%2==0:
            print(lines,end='')
        i+=1
problem4()