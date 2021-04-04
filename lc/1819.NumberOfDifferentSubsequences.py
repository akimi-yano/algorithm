# 1819. Number of Different Subsequences GCDs
# Hard

# 91

# 24

# Add to List

# Share
# You are given an array nums that consists of positive integers.

# The GCD of a sequence of numbers is defined as the greatest integer that divides all the numbers in the sequence evenly.

# For example, the GCD of the sequence [4,6,16] is 2.
# A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

# For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
# Return the number of different GCDs among all non-empty subsequences of nums.

 

# Example 1:


# Input: nums = [6,10,3]
# Output: 5
# Explanation: The figure shows all the non-empty subsequences and their GCDs.
# The different GCDs are 6, 10, 3, 2, and 1.
# Example 2:

# Input: nums = [5,15,40,5,6]
# Output: 7
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 2 * 105

# This solution works - dp:

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        '''
        [4, 4, 8]
        i = 1, 2, ...8
        
        i = 1
        4 % 1 = 0
        8 % 1 = 0
        GCD(4,8) = 4, so skip
        
        i = 2
        4 % 2 = 0
        8 % 2 = 0
        GCD(4, 8) = 4, so skip
        
        i = 3
        4 % 3 = 3 x
        8 % 3 = 2 x
        GCD() N/A, so skip
        
        i = 4
        4 % 4 = 0
        8 % 4 = 0
        GCD(4, 8) = 4 == i, this is a GCD of the subset (4, 8)
        '''
        numset = set(nums)
        maxnum = max(nums)
        ans = 0
        for i in range(1, maxnum + 1):
            cur_gcd = None
            for multiple in range(i, maxnum+1, i):
                if multiple in numset:
                    if cur_gcd is None:
                        cur_gcd = multiple
                    else:
                        # cur_gcd keeps on decreasing as you add more multiples
                        cur_gcd = gcd(cur_gcd, multiple)
                    if cur_gcd == i:
                        ans += 1
                        break
        return ans
#         all_ans = set([])
#         seen = set([])
#         def helper(i, seen):
#             if i > len(nums)-1:
#                 all_ans.union(seen)
#                 return 
            
#             temp = set(seen)
#             for elem in temp:   
#                 seen.add(math.gcd(nums[i], elem))
#                 helper(i+1, seen)
#                 seen.remove(math.gcd(nums[i], elem))
#             helper(i+1, seen)
            
#         helper(0, seen)
#         return len(all_ans)