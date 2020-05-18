
# Week1 Exam
# Complete the 'mergeArrays' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
# merge two sorted arrays

def mergeArrays(a, b):    
    ans = []
    i = 0
    k = 0
    while len(a)>i and len(b)>k:
        if a[i]>= b[k]:
            ans.append(b[k])
            k+=1
        else:
            ans.append(a[i])
            i+=1
    while len(b)>k:
        ans.append(b[k])
        k+=1
    while len(a)>i:
        ans.append(a[i])
        i+=1
    return ans

#
# Complete the 'dnaComplement' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

# AT are complement
# CG are complement
# Rotate the input string and swap each element with its complement
# return string 

def dnaComplement(s):
    ans=""
    for i in range(len(s)-1,-1,-1):
        if s[i] == "A":
            ans+="T"
        elif s[i] == "T":
            ans+="A"
        elif s[i] == "C":
            ans+="G"
        else:
            ans+="C"
    return ans 


#
# Complete the 'minimumStepsToOne' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER num as parameter.
#

# take aways:::: output has to be a variable name that is different from the input !!

# //recursion passing in count - dont do it if you want to turn it into memorization
# def minimumStepsToOne(num):
#     def helper(n,count):
#         if n == 1:
#             return count
#         new_count = helper(n-1,count+1)
#         if n%2==0:
#             new_count = min(new_count,helper(n//2,count+1))
#         if n%3==0:
#             new_count = min(new_count,helper(n//3,count+1))
#         return new_count    
#     return helper(num,0)
# print(minimumStepsToOne(4))
# print(minimumStepsToOne(3))
# print(minimumStepsToOne(2))

# //memorization solution - still hit the max recursion depth 
# def minimumStepsToOne(num):
#     memo = {}
#     def helper(n):
#         if n in memo:
#             return memo[n]
#         if n == 1:
#             return 0
#         new_count = 1 + helper(n-1)
#         if n%2==0:
#             new_count = min(new_count,1 + helper(n//2))
#         if n%3==0:
#             new_count = min(new_count,1 + helper(n//3))
#         memo[n] = new_count
#         return new_count    
#     return helper(num)
# print(minimumStepsToOne(4))
# print(minimumStepsToOne(3))
# print(minimumStepsToOne(2))
# print(minimumStepsToOne(5400))


# // tabulation solution
def minimumStepsToOne(num):
    tab = {1: 0}
    for n in range(2,num+1):
        temp = tab[n-1]
        if n%2==0:
            temp = min(temp,tab[n//2])
        if n%3==0:
            temp = min(temp,tab[n//3])
        temp +=1
        tab[n]=temp
    return tab[num]

print(minimumStepsToOne(8))
