# 823. Binary Trees With Factors
# Medium

# 1258

# 134

# Add to List

# Share
# Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

# We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

# Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

 

# Example 1:

# Input: arr = [2,4]
# Output: 3
# Explanation: We can make these trees: [2], [4], [4, 2, 2]
# Example 2:

# Input: arr = [2,4,5,10]
# Output: 7
# Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
 

# Constraints:

# 1 <= arr.length <= 1000
# 2 <= arr[i] <= 109
# All the values of arr are unique.


# This solution works:


class Solution:
    MOD = 10**9 + 7
    '''
    [2,4]
    '''
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr_set = set(arr)

        @lru_cache(None)
        def helper(num):
            nonlocal arr_set
            total = 1
            for left in arr_set:
                # if left cannot divide num, skip
                if num % left:
                    continue
                right = num // left
                # if right is not in arr_set, skip
                if right not in arr_set:
                    continue
                total += helper(left) * helper(right)

            return total 
        
        return sum(helper(num) for num in arr) % Solution.MOD
    