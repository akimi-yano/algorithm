# 673. Number of Longest Increasing Subsequence
# Medium

# 1846

# 104

# Add to List

# Share
# Given an integer array nums, return the number of longest increasing subsequences.



# Example 1:

# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
# Example 2:

# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.



# Constraints:

# 0 <= nums.length <= 2000
# -106 <= nums[i] <= 106

# this approach does not work 

# class Solution:
#     def findNumberOfLIS(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         memo = {}
            
#         def helper(i, length, prev):
#             if i > len(nums)-1:
#                 if length not in memo:
#                     memo[length] = 0
#                 memo[length] += 1
#                 return
    
#             if  prev < nums[i]:
#                 length += 1
#                 helper(i+1, length, nums[i])
#                 length -= 1
#             helper(i+1, length, prev)
            
#         helper(0, 0, float('-inf'))

#         max_length = max(memo.keys())
#         return memo[max_length]

# this approach does not work 

# class Solution:
#     def findNumberOfLIS(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         def helper(i, prev):
#             if i >= len(nums)-1 and prev < nums[i]:
#                 return (1, 1)
#             opt1 = None
#             if  prev < nums[i]:
#                 opt1 = max(ans, 1+ helper(i+1, nums[i]))
#             opt2 = max(ans, helper(i+1, prev))
#             if not opt1:
#                 return opt2
#             else:
#                 if opt1 < opt2:
#                     return opt2
#                 elif opt1 > opt2:
#                     return opt1
#                 else:
#                     return 2
        
#         return helper(0, float('-inf'))

# this approach does not work   
    
# class Solution:
#     def findNumberOfLIS(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         def helper(i, prev):
#             if i >= len(nums)-1 and prev < nums[i]:
#                 return (1, 1)
#             opt1 = None
#             if  prev < nums[i]:
#                 opt1 = max(ans, 1+ helper(i+1, nums[i]))
#             opt2 = max(ans, helper(i+1, prev))
#             if not opt1:
#                 return opt2
#             else:
#                 if opt1 < opt2:
#                     return opt2
#                 elif opt1 > opt2:
#                     return opt1
#                 else:
#                     return 2
        
#         return helper(0, float('-inf'))



# This solution works !
'''
recursion + memorization
save the information of i and prev
how many i are there? - len(nums) - N
how many prev are there? - len(nums) - N
so time and space complexity is N * N = N^2
Time complexity: O(N^2) after memorization (its exponential before memorization)
Space complexity: O(N^2) which is a combination of the informaiton we store
there are multiple cases, and its important to write down and handle all the cases patiently !
'''

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        memo = {}

        def helper(i, prev):
            key = (i, prev)
            if key in memo:
                return memo[key]
            
            ans = (0, 1)
            # if i is out of bounds, we have length 0, count 1
            if i > len(nums)-1:
                pass
            else:
                # if prev is smaller than the current num, we have two options
                if  prev < nums[i]:
                    # option 1: use the number at nums[i]
                    len1, count1 = helper(i+1, nums[i])
                    len1 += 1
                    # option 2: skip the number at nums[i]
                    len2, count2 = helper(i+1, prev)
                    
                    # now, compare the results
                    if len1 > len2:
                        ans = (len1, count1)
                    elif len1 < len2:
                        ans = (len2, count2)
                    else:
                        ans = (len1, count1 + count2)
                else:
                    ans = helper(i+1, prev)
                    

            memo[key] = ans
            return ans
        
        return helper(0, float('-inf'))[1]