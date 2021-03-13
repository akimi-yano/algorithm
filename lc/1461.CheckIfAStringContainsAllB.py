# 1461. Check If a String Contains All Binary Codes of Size K
# Medium

# 447

# 56

# Add to List

# Share
# Given a binary string s and an integer k.

# Return True if every binary code of length k is a substring of s. Otherwise, return False.

 

# Example 1:

# Input: s = "00110110", k = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.
# Example 2:

# Input: s = "00110", k = 2
# Output: true
# Example 3:

# Input: s = "0110", k = 1
# Output: true
# Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
# Example 4:

# Input: s = "0110", k = 2
# Output: false
# Explanation: The binary code "00" is of length 2 and doesn't exist in the array.
# Example 5:

# Input: s = "0000000001011100", k = 4
# Output: false
 

# Constraints:

# 1 <= s.length <= 5 * 10^5
# s consists of 0's and 1's only.
# 1 <= k <= 20

# This approach does not work:

# class Solution:
#     def hasAllCodes(self, s: str, k: int) -> bool:
#         def helper(n):
#             if n == 1:
#                 return [["0"],["1"]]
            
#             ans = []
#             arr = helper(n-1)
#             ans.extend(["0"] + elem for elem in arr)
#             ans.extend(["1"] + elem for elem in arr)
#             return ans
#         all_options = set("".join(temp) for temp in helper(k))
        
#         for start in range(len(s)):
#             elem = s[start:start+k]
#             if elem in all_options:
#                 all_options.remove(elem)
        
#         return not all_options
        


# This solution works:

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        all_options = set([])
        
        for start in range(len(s)):
            elem = s[start:start+k]
            if len(elem) == k:
                all_options.add(elem)
        
        return len(all_options) == (2 ** k)
        