# frequency_counting

# Given an array of integers, and a target value determine if there are two integers that add to the sum.

# Input: [4,2,6,5,7,9,10], 13

# Output: true

def addToSum(arr, target):
    memo = set([])
    for num in arr:
        if num not in memo:
            memo.add(target-num)
    for num in arr:
        if num in memo:
            return True
    return False
print(addToSum([4,2,6,5,7,9,10], 13))