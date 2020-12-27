# 1707. Maximum XOR With an Element From Array
# Hard

# 25

# 6

# Add to List

# Share
# You are given an array nums consisting of non-negative integers. You are also given a queries array, where queries[i] = [xi, mi].

# The answer to the ith query is the maximum bitwise XOR value of xi and any element of nums that does not exceed mi. In other words, the answer is max(nums[j] XOR xi) for all j such that nums[j] <= mi. If all elements in nums are larger than mi, then the answer is -1.

# Return an integer array answer where answer.length == queries.length and answer[i] is the answer to the ith query.

 

# Example 1:

# Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
# Output: [3,3,7]
# Explanation:
# 1) 0 and 1 are the only two integers not greater than 1. 0 XOR 3 = 3 and 1 XOR 3 = 2. The larger of the two is 3.
# 2) 1 XOR 2 = 3.
# 3) 5 XOR 2 = 7.
# Example 2:

# Input: nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
# Output: [15,-1,5]
 

# Constraints:

# 1 <= nums.length, queries.length <= 105
# queries[i].length == 2
# 0 <= nums[j], xi, mi <= 109


# This approach does not work 

# class Solution:
#     def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
#         nums.sort()
#         ans = [-1 for _ in queries]
        
#         mxi_queries = [(m, x, i) for i, (x, m) in enumerate(queries)]
#         mxi_queries.sort(reverse=True)
#         for m, x, i in mxi_queries:
#             while nums and nums[-1] > m:
#                 nums.pop()
#             if not nums:
#                 continue
    
#             best = -1
#             for num in nums:
#                 best = max(best, x ^ num)
#             ans[i] = best
#         return ans


# This solution works!

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        lookup = Counter()
        for shift in range(31, -1, -1):
            for num in nums:
                shifted = num >> shift
                lookup[(shift, shifted)] += 1
                
        def remove_from_lookup(num):
            for shift in range(31, -1, -1):
                shifted = num >> shift
                lookup[(shift, shifted)] -= 1

        nums.sort()
        ans = [-1 for _ in queries]
        
        mxi_queries = [(m, x, i) for i, (x, m) in enumerate(queries)]
        mxi_queries.sort(reverse=True)
        for m, x, i in mxi_queries:
            while nums and nums[-1] > m:
                remove_from_lookup(nums.pop())
            if not nums:
                continue

            cur = 0
            for shift in range(31, -1, -1):
                want_bit = 1
                if (x >> shift) & 1:
                    want_bit = 0
                lookup_key = (shift, (cur << 1) | want_bit)
                if lookup[lookup_key] > 0:
                    cur = (cur << 1) | want_bit
                else:
                    cur = (cur << 1) | (1 ^ want_bit)
            ans[i] =  x ^ cur
        return ans