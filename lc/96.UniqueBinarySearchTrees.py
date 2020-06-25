# 96. Unique Binary Search Trees

# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

# Example:

# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

import math

# DP
def numtrees_tab(n):
    res = [0] * (n+1)
    res[0] = 1
    for i in range(1, n+1):
        for j in range(i):
            res[i] += res[j] * res[i-1-j]
        # print(res)
    return res[n]
print("tabulation: ",numtrees_tab(3))
print("tabulation: ",numtrees_tab(4))
print("tabulation: ",numtrees_tab(10))

# Catalan Number  (2n)!/((n+1)!*n!)  
def numtrees_math(n):
    return math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1))
    
print("math: ",numtrees_math(3))   
print("math: ",numtrees_math(4))  
print("math: ",numtrees_math(10)) 

# recursion + memo
def numtrees_memo(n):
    memo = {}
    def helper(k):
        if k in memo:
            return memo[k]
        if k<2:
            return 1
        sum = 0
        for i in range(k):
            sum+=helper(i)*helper(k-i-1)
        memo[k]=sum
        return sum
    return helper(n)
print("memorization: ",numtrees_memo(3))
print("memorization: ",numtrees_memo(4))
print("memorization: ",numtrees_memo(10))