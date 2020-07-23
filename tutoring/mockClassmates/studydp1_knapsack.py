#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the unboundedKnapsack function below.
def unboundedKnapsack(k, arr):
    def helper(total,i):
        if total == 0:
            return 0
        if total<0:
            return float('inf')
        if i<0:
            return total
        min_val = float('inf')
        min_val = min(min_val, helper(total-arr[i],i))
        min_val = min(min_val,helper(total,i-1))
        return min_val 

    ans = helper(k,len(arr)-1)
    print(k, arr, ans)
    return k-ans


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
