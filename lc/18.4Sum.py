# 18. 4Sum
# Medium

# 2375

# 351

# Add to List

# Share
# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note:

# The solution set must not contain duplicate quadruplets.

# Example:

# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]



# This solution does not  work - TLEd !!!


# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
#         def helper(arr, i):
            
#             if len(arr)==4 and sum(arr) == target:
#                 ans.add(tuple(sorted(arr)))
#                 return
#             if i  > len(nums)-1:
#                 return
    
#             temp = list(arr)
#             temp.append(nums[i])
#             helper(temp, i+1)
#             helper(arr, i+1)
        
        
#         ans = set([])
#         for i in range(len(nums)):
#             helper([], i)
        
#         return [list(elem) for elem in ans]

# This solution does not work: TLE 

# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
#         def helper(arr, i):
            
#             if len(arr)==4 and sum(arr) == target:
#                 ans.add(tuple(arr))
#                 return
#             if i  > len(nums)-1:
#                 return
       
#             temp = list(arr)
#             temp.append(nums[i])
#             helper(temp, i+1)
#             helper(arr, i+1)
        
#         nums.sort()
#         ans = set([])
#         for i in range(len(nums)):
#             helper([], i)
        
#         return [list(elem) for elem in ans]


# This solution does not  work - TLEd:
    
# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
#         def helper(arr, i):
            
#             if len(arr)==4 and sum(arr) == target:
#                 ans.add(tuple(arr))
#                 return
#             if i  > len(nums)-1:
#                 return
       
            
#             arr.append(nums[i])
#             helper(arr, i+1)
#             arr.pop()
#             helper(arr, i+1)
        
#         nums.sort()
#         ans = set([])
#         for i in range(len(nums)):
#             helper([], i)
        
#         return [list(elem) for elem in ans]

# Still TLED !

# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
#         def helper(arr, i, total):
            
#             if len(arr)==4 and total == target:
#                 ans.add(tuple(arr))
#                 return

            
#             if i  > len(nums)-1:
#                 return
       
            
#             arr.append(nums[i])
#             helper(arr, i+1, total+nums[i])
#             arr.pop()
#             helper(arr, i+1, total)
        
#         nums.sort()
#         ans = set([])
        
#         helper([], 0, 0)
        
#         return [list(elem) for elem in ans]
        



# This solution works !!! O(N**3)

from itertools import combinations
from collections import Counter
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        counts = Counter(nums)
        ans = set([])
        for comb in combinations(nums, 3):
            last = target - sum(comb)
            if last in counts:
                # how many last are there in the comb dictionary ? + 1
                if Counter(comb)[last] + 1 <= counts[last]:
                    ans.add(tuple([num for num in sorted(comb + (last,))]))
        return ans
    
# This solution works !!! O(N**2) - optimization

from itertools import combinations
from collections import Counter
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        counts = Counter(nums)
        ans = set([])
        twosum_dict = {}
        for comb in combinations(nums, 2):
            twosum = sum(comb)
            if twosum not in twosum_dict:
                twosum_dict[twosum] = set([])
            twosum_dict[twosum].add(tuple([num for num in sorted(comb)]))
        # print(twosum_dict)
        for twosum_one, tuples_one in twosum_dict.items():
            twosum_two = target - twosum_one
            if twosum_two in twosum_dict:
                tuples_two = twosum_dict[twosum_two]
                for tup1 in tuples_one:
                    for tup2 in tuples_two:
                        tup1_tup2_counts = Counter(tup1 + tup2)
                        valid = True
                        for num, count in tup1_tup2_counts.items():
                            if counts[num] < count:
                                valid = False
                                break
                        if valid:
                            ans.add(tuple([num for num in sorted(tup1 + tup2)]))
        return ans