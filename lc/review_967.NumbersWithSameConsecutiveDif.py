# 967. Numbers With Same Consecutive Differences
# Medium

# 1464

# 146

# Add to List

# Share
# Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

# Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

# You may return the answer in any order.

 

# Example 1:

# Input: n = 3, k = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.
# Example 2:

# Input: n = 2, k = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 

# Constraints:

# 2 <= n <= 9
# 0 <= k <= 9


# This solution works:


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def helper(remaining, cur):
            nonlocal ans
            if remaining == 0:
                ans.append(cur)
                return
            for num in range(10):
                if n != remaining:
                    #the diff has to be k and the 0 is ok
                    prev = cur % 10
                    if prev + k == num:
                        helper(remaining-1, cur*10+num)
                    elif prev - k == num:
                        helper(remaining-1, cur*10+num)
                elif num != 0:
                    #no leading 0
                    helper(remaining-1, cur+num)
        
        ans = []
        helper(n, 0)
        return ans