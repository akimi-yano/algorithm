# 1849. Splitting a String Into Descending Consecutive Values
# Medium

# 43

# 31

# Add to List

# Share
# You are given a string s that consists of only digits.

# Check if we can split s into two or more non-empty substrings such that the numerical values of the substrings are in descending order and the difference between numerical values of every two adjacent substrings is equal to 1.

# For example, the string s = "0090089" can be split into ["0090", "089"] with numerical values [90,89]. The values are in descending order and adjacent values differ by 1, so this way is valid.
# Another example, the string s = "001" can be split into ["0", "01"], ["00", "1"], or ["0", "0", "1"]. However all the ways are invalid because they have numerical values [0,1], [0,1], and [0,0,1] respectively, all of which are not in descending order.
# Return true if it is possible to split s​​​​​​ as described above, or false otherwise.

# A substring is a contiguous sequence of characters in a string.

 

# Example 1:

# Input: s = "1234"
# Output: false
# Explanation: There is no valid way to split s.
# Example 2:

# Input: s = "050043"
# Output: true
# Explanation: s can be split into ["05", "004", "3"] with numerical values [5,4,3].
# The values are in descending order with adjacent values differing by 1.
# Example 3:

# Input: s = "9080701"
# Output: false
# Explanation: There is no valid way to split s.
# Example 4:

# Input: s = "10009998"
# Output: true
# Explanation: s can be split into ["100", "099", "98"] with numerical values [100,99,98].
# The values are in descending order with adjacent values differing by 1.
 

# Constraints:

# 1 <= s.length <= 20
# s only consists of digits.

# This solution works:

class Solution:
    def splitString(self, s: str) -> bool:
        @lru_cache(None)
        def helper(idx, prev):
            nonlocal s
            if idx >= len(s):
                return True
            for end in range(idx+1, len(s)+1):
                num = int(s[idx:end])
                if prev - num == 1 and helper(end, num):
                    return True
            return False
        
        for end in range(1, len(s)):
            first = int(s[:end])
            if helper(end, first):
                return True
        return False


# This approach does not work:
        
#         def helper(i, arr, temp):
#             nonlocal ans
            
#             if i > len(s)-1:
#                 if not temp:
#                     return
#                 string = "".join(temp)
#                 new_arr = list(arr)
#                 new_arr.append(string)
#                 ans.append(new_arr)
#                 return 
            
#             helper(i + 1, arr, temp + [s[i]])
#             string = "".join(temp + [s[i]])
#             helper(i + 1, arr + [string], [])
        
#         ans = []
#         helper(0, [], [])
#         for arr in ans:
#             for i, num in enumerate(arr):
#                 arr[i] = int(num)
        
#         for arr in ans:
#             if len(arr) < 2:
#                 continue
#             invalid = False
#             for i in range(1, len(arr)):
#                 if arr[i-1] - arr[i] != 1:
#                     invalid = True
#                     break
#             if not invalid:
#                 return True
#         return False
            