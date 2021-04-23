# 696. Count Binary Substrings
# Easy

# 1454

# 245

# Add to List

# Share
# Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

# Substrings that occur multiple times are counted the number of times they occur.

# Example 1:
# Input: "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

# Notice that some of these substrings repeat and are counted the number of times they occur.

# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
# Example 2:
# Input: "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
# Note:

# s.length will be between 1 and 50,000.
# s will only consist of "0" or "1" characters.

# This solution works:

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        '''
        look at 2 adjacent groups of 1s and 0s and get the min
        2 path: 1) use an array to append the count of each group (1 or 0); 2) get the min of 2 adjacent groups
        '''
        count = 1
        arr = []
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                arr.append(count)
                count = 1
            else:
                count += 1
        arr.append(count)
        
        ans = 0
        for x, y in zip(arr, arr[1:]):
            ans += min(x, y)
        return ans