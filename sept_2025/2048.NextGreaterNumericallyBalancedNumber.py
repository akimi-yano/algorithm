'''
2048. Next Greater Numerically Balanced Number
Medium
Topics
premium lock icon
Companies
Hint
An integer x is numerically balanced if for every digit d in the number x, there are exactly d occurrences of that digit in x.

Given an integer n, return the smallest numerically balanced number strictly greater than n.

 

Example 1:

Input: n = 1
Output: 22
Explanation: 
22 is numerically balanced since:
- The digit 2 occurs 2 times. 
It is also the smallest numerically balanced number strictly greater than 1.
Example 2:

Input: n = 1000
Output: 1333
Explanation: 
1333 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times. 
It is also the smallest numerically balanced number strictly greater than 1000.
Note that 1022 cannot be the answer because 0 appeared more than 0 times.
Example 3:

Input: n = 3000
Output: 3133
Explanation: 
3133 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times.
It is also the smallest numerically balanced number strictly greater than 3000.
 

Constraints:

0 <= n <= 106
 
'''

def generate(num: int, count: list[int], nums: list[int]) -> None:
    if num > 0 and is_beautiful(count):
        nums.append(num)
    if num > 1224444:
        return

    for d in range(1, 8):
        if count[d] < d:
            count[d] += 1
            generate(num * 10 + d, count, nums)
            count[d] -= 1

def is_beautiful(count: list[int]) -> bool:
    for d in range(1, 8):
        if count[d] != 0 and count[d] != d:
            return False
    return True

nums = []
generate(0, [0]*10, nums)
nums.sort()

class Solution:    
    def nextBeautifulNumber(self, n: int) -> int:
        res = bisect_right(nums, n)
        return nums[res]