'''
Topic: Bit manipulation
'''

'''
--------------------------------------------------------------------------------------------
Single Number
https://leetcode.com/problems/single-number/
136. Single Number
Easy

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''
def singleNumber(self, nums: List[int]) -> int:
  
  #     a ^ a = 0
#     a ^ 0 = a
    
#     xor -> either a or b, but not both
    
#     a xoR 0 =
    
    
#     1111100000
#     0000000000
    
#     1111100000
    
    
#     a xor a xor b xor b xor c
    
#     0 xor 0 xor c
#     ---> c

        output = 0
        for num in nums:
            output = output ^ num
        return output


'''
https://leetcode.com/problems/single-number-ii/
'''

# 1. dict time O(N) space O(N)
# 2. sort time O(NlogN) space O(1)
# 3. a+a+a+b+b+b+c+c = 3a+3b+2c, use set. Time O(N) Space O(N)
# 4. bitwise a XOR a = 0, 0 XOR a = a
# a XOR a XOR a XOR b XOR b XOR b XOR c XOR c =  a XOR b XOR c
    
    # Time O(N) Space O(1)
    def singleNumber(self, nums: List[int]) -> int:
        
        seen_once = 0
        seen_twice = 0
        for num in nums:
            seen_once = seen_once ^ num & ~seen_twice
            seen_twice = seen_twice ^ num & ~seen_once

        return seen_once

'''
https://leetcode.com/problems/single-number-iii/
'''
# a XOR 0 = a
# XOR if one, but not both
# a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
# a XOR a = 0
# a XOR b XOR a XOR c = 0 XOR b XOR c = b XOR c
# x & (-x) to isolate the rightmost 1-bit. 
# x & (-x) keep the rightmost 1-bit and to set all the other bits to 0
# Brain Kernighan's algorithm a & (a-1), turn off the rightmost 1-bit

    

'''    
    # Time O(N) Space O(1), runtime = 60 ms
    def singleNumber(self, nums: List[int]) -> List[int]:  
        
        if not nums: return []
    
        a_xor_b = 0
        for num in nums:
            a_xor_b ^= num
            
        rightmost_1_bit = a_xor_b & (- a_xor_b)
        
        a = 0
        for num in nums:
            if num & rightmost_1_bit:
                a ^= num
        return [a, a_xor_b ^ a]
'''        
        
    
'''
    # Time O(N) Space O(N), runtime = 56 ms
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        num_dict = collections.Counter(nums)
        
        return [k for k,v in num_dict.items() if v == 1]
        
''' 


'''
231. Power of Two
https://leetcode.com/problems/power-of-two/
Given an integer n, write a function to determine if it is a power of two.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
Example 4:

Input: n = 4
Output: true
Example 5:

Input: n = 5
Output: false
 

Constraints:

-231 <= n <= 231 - 1

'''

def isPowerOfTwo(self, n: int) -> bool:
  
  if not n or n<1: return False
  
  return n & (n-1)  == 0




