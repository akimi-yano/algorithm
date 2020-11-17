# 1655. Distribute Repeating Integers
# Hard

# 41

# 4

# Add to List

# Share
# You are given an array of n integers, nums, where there are at most 50 unique values in the array. You are also given an array of m customer order quantities, quantity, where quantity[i] is the amount of integers the ith customer ordered. Determine if it is possible to distribute nums such that:

# The ith customer gets exactly quantity[i] integers,
# The integers the ith customer gets are all equal, and
# Every customer is satisfied.
# Return true if it is possible to distribute nums according to the above conditions.


# Example 1:

# Input: nums = [1,2,3,4], quantity = [2]
# Output: false
# Explanation: The 0th customer cannot be given two different integers.
# Example 2:

# Input: nums = [1,2,3,3], quantity = [2]
# Output: true
# Explanation: The 0th customer is given [3,3]. The integers [1,2] are not used.
# Example 3:

# Input: nums = [1,1,2,2], quantity = [2,2]
# Output: true
# Explanation: The 0th customer is given [1,1], and the 1st customer is given [2,2].
# Example 4:

# Input: nums = [1,1,2,3], quantity = [2,2]
# Output: false
# Explanation: Although the 0th customer could be given [1,1], the 1st customer cannot be satisfied.
# Example 5:

# Input: nums = [1,1,1,1,1], quantity = [2,3]
# Output: true
# Explanation: The 0th customer is given [1,1], and the 1st customer is given [1,1,1].

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= 1000
# m == quantity.length
# 1 <= m <= 10
# 1 <= quantity[i] <= 105
# There are at most 50 unique values in nums.

# This solution works !

class Solution:
    def canDistribute(self, a: List[int], customers: List[int]) -> bool:
        '''
        remove an O(m) factor by precalculating subset sums
        iterating through all submasks of all masks is O(3^m)
        https://cp-algorithms.com/algebra/all-submasks.html
        
        formula to check all the cases: submask = (submask-1) & mask
        '''
        c = Counter(a)
        a = sorted(c.values())
        
        n = len(a)
        m = len(customers)
        
        ALL = (1 << m) - 1
        
        
        mask_sum = defaultdict(int)
        
        for mask in range(1 << m):
            for i in range(m):
                if (1 << i) & mask:
                    mask_sum[mask] += customers[i]
                    
        @lru_cache(None)
        def recurse(i, mask):
            
            if mask == 0:
                return True
    
            if i == n:
                return False
            
            submask = mask
            
            while submask:
                
                if mask_sum[submask] <= a[i] and recurse(i+1, mask ^ submask):
                    return True
                
                submask = (submask-1) & mask
            
            return recurse(i+1, mask)
                
        return recurse(0, ALL)