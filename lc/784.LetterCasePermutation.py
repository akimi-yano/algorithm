# 784. Letter Case Permutation
# Medium

# 1846

# 121

# Add to List

# Share
# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

# Return a list of all possible strings we could create. You can return the output in any order.

 

# Example 1:

# Input: S = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
# Example 2:

# Input: S = "3z4"
# Output: ["3z4","3Z4"]
# Example 3:

# Input: S = "12345"
# Output: ["12345"]
# Example 4:

# Input: S = "0"
# Output: ["0"]
 

# Constraints:

# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.

# This solution works:

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        @lru_cache(None)
        def helper(i):
            if i > len(S)-1:
                return [[]]
            ans = []
            if S[i].isalpha():
                ans.extend([S[i].lower()] + temp for temp in helper(i+1))
                ans.extend([S[i].upper()] + temp for temp in helper(i+1))
            else:
                ans.extend([S[i]] + temp for temp in helper(i+1))
            return ans        
        arr = helper(0)
        return ["".join(elem) for elem in arr]
