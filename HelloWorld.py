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

problem2()