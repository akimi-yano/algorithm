# 179. Largest Number
# Medium

# 2367

# 264

# Add to List

# Share
# Given a list of non negative integers, arrange them such that they form the largest number.

# Example 1:

# Input: [10,2]
# Output: "210"
# Example 2:

# Input: [3,30,34,5,9]
# Output: "9534330"
# Note: The result may be very large, so you need to return a string instead of an integer.




# This approach does not work :

# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
        # memo = {}
        # for i in range(10):
        #     memo[str(i)]=i
        # # print(memo)
        # for num in nums:
        #     for char in str(num):
        #         print(char)
        '''
        [1,2,3,4,5,6]
        654321
        
        
        Input: [10,2]
        Output: "210"
        
        1[0] vs 2
        


        Input: [3,30,34,5,9]
        Output: "9534330"
        
        3 5 9
        30 34
        
        9 5 34 3 30
        '''
        
# This solution does not work 
# class TrieNode:
#     def __init__(self):
#         self.next = {}
#         self.is_end = False

# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         root = TrieNode()
        
#         for num in nums:
#             cur = root
#             for char in str(num):
#                 if char not in cur.next:
#                     cur.next[char] = TrieNode()
#                 cur = cur.next[char] 
#             cur.is_end = True
#         # print(root.next['1'])
        
#         ans = []
        
#         number = ""
#         for n in range(10):
#             cur = root
#             while str(n) in cur.next:
#                 number += str(n)
#                 if cur.next[str(n)].is_end:
#                     ans.append(number)
                
#                 for n in range(10):
#                     if str(n)  in cur.next:
#                         cur = cur.next[str(n)] 
#         print(ans)
#         return "".join(reversed(ans))
            
            
        
# This solution works  !!!


# If we use the default string comparator of sort(), and concatenate sorted strings,
# cases as ['3', '30'] will fail for '3' < '30' but we want '330' rather than '303'.
# If we use customized cmp_func such that string x is smaller than string y if x + y < y + x, '30' < '3', we will get '330' at last.

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def cmp_func(x, y):
            """Sorted by value of concatenated string increasingly."""
            if x + y > y + x:
                return 1
            elif x == y:
                return 0
            else:
                return -1
            
        # Build nums contains all numbers in the String format.
        nums = [str(num) for num in nums]
        
        # Sort nums by cmp_func decreasingly.
        nums.sort(key = cmp_to_key(cmp_func), reverse = True)
        
        # Remove leading 0s, if empty return '0'.
        return ''.join(nums).lstrip('0') or '0'