#!/bin/python3

import math
import os
import random
import re
import sys


# this does not work 
# def unboundedKnapsack(k, arr):
    # def helper(total,i):
    #     if total == 0:
    #         return 0
    #     if total<0:
    #         return float('inf')
    #     if i<0:
    #         return total
    #     min_val = float('inf')
    #     min_val = min(min_val, helper(total-arr[i],i))
    #     min_val = min(min_val,helper(total,i-1))
    #     return min_val 

    # ans = helper(k,len(arr)-1)
    # print(k, arr, ans)
    # return k-ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    while True:
        try:
            nk = input().split()
        except:
            break

        n = int(nk[0])

        k = int(nk[1])

        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)

        fptr.write(str(result) + '\n')

    fptr.close()

# this tablation does not work 
# def unboundedKnapsackTab(k, arr):
#   tab = [i for i in range(k+1)]  
  
#   for row in range(1,len(arr)+1):
#     for col in range(len(tab)):
#       not_use = tab[col]
#       used = tab[col]+arr[row-1]
#       if not_use<=k and used<=k:
#         tab[col] = used
#       elif not_use<=k:
#         tab[col] = not_use
#   return tab[len(tab)-1]

# Input (stdin)
# Download
# 5
# 1 2000
# 1
# 2 10
# 5 9
# 2 2000
# 2 1
# 2 2000
# 1999 1999
# 3 3
# 4 4 5
# Expected Output
# Download
# 2000
# 10
# 2000
# 1999
# 0

# didnt pass the test case above due to max depth of recursion
# def unboundedKnapsack(k, arr):
#     options = set(arr)
#     memo = {}
#     def helper(remaining):
#         if remaining in memo:
#             return memo[remaining]
#         ans = remaining
#         for option in options:
#             candidate = remaining - option
#             if candidate >= 0:
#                 ans = min(ans, helper(candidate))
#         memo[remaining] = ans
#         return ans

#     return k-helper(k)



# this works - passed all cases !!! 

def unboundedKnapsack(k, arr):
    choices = set(arr)
    tab = [True] + [False for i in range(k)]
    for i in range(1, len(tab)):
        for choice in choices:
            tab[i] |= i-choice >= 0 and tab[i-choice]
            if tab[i]:
                break
    tab.reverse()
    diff = tab.index(True)
    return k - diff