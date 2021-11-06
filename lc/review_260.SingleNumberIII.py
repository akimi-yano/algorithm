# 260. Single Number III
# Medium

# 2996

# 163

# Add to List

# Share
# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

# Example 1:

# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.
# Example 2:

# Input: nums = [-1,0]
# Output: [-1,0]
# Example 3:

# Input: nums = [0,1]
# Output: [1,0]
 

# Constraints:

# 2 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# Each integer in nums will appear twice, only two integers will appear once.


# This solution works:


'''
If you solved Single Number I or II problems you probably can immediately say, that this problem is about bit manipulations. So, the first step is to evaluate XOR of all numbers, but what is next? It is indeed very difficult question, if we are not allowed to use extra memory and we want to stay with O(n) iterations. So, what exactly we get, when we evaluate XOR of all numbers? We will have num1 ^ num2, where num1 and num2 are desired numbers. We need to use all the imformation given in statement, and so these numbers are different, and it means there will be at least one bit, where they differ, it means one number of num1 and num2 have this bit equal to 0 and other to 1 . Let us remember this bit and traverse data once again: making XOR of numbers, where this bit is equal to 1. Then we get exactly one of our desired numbers. Finally, we can find other number, using num2 = s^num1, where s is XOR of all numbers.

Evaluate s - XOR of all numbers.
nz is non-zero bit. s&(s-1) trick is used to remove last 1: for example for number s = 110100, the value s&(s-1) = 110000, and s & (s-1) ^ s = 110000 ^ 110100 = 000100.
We evaluate num1, using only numbers, where this bit is not absent.
Finally, we evaluate num2 = s ^ num and return answer.
Complexity: time complexity is O(n), where we do 2 passes over data. Additional space complexity is O(1), we use just several additional variables.
'''
class Solution:
    def singleNumber(self, nums):
        s = reduce(xor, nums)
        nz = s & (s-1) ^ s
        num1 = reduce(xor, filter(lambda n: n & nz, nums))
        return(num1, s ^ num1)



# This solution works:


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        a = 0
        b = 0
        for num in nums:
            xor ^= num
        mask = 1
        while(xor&mask == 0):
            mask = mask << 1
        for num in nums:
            if num&mask:
                a ^= num
            else:
                b ^= num
        return [a, b]
            