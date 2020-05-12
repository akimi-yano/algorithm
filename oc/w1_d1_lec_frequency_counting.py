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
# print(addToSum([4,2,6,5,7,9,10], 13))

# Challenge 1: Sort a Bit Array
# Given a bit array, return it sorted in-place (a bit array is simply an array that contains only bits, either 0 or 1).

# See if you can solve this in O(N) time and O(1) auxiliary space.

# Try to solve this using a frequency count rather than using multiple pointers, or using a comparison sort function.

# Input : [0, 1, 1, 0, 1, 1, 1, 0]

# Output : [0, 0, 0, 1, 1, 1, 1, 1]

def sortBitArr(arr):
    counter =0  
    for i in range(len(arr)):
        if arr[i] ==1:
            counter +=1
            arr[i] = 0
    for s in range(counter):
        arr.pop()
    for k in range(counter):
        arr.append(1)
    return arr
print(sortBitArr([0, 1, 1, 0, 1, 1, 1, 0]))

def sort_bit_array(arr):
    count = arr.count(1)
    return [0] * (len(arr) - count) + [1] * count
print(sort_bit_array([0, 1, 1, 0, 1, 1, 1, 0]))