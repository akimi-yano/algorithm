# 647. Palindromic Substrings
# Medium

# 6512

# 156

# Add to List

# Share
# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters.


# This solution works:


class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(left, right):
            temp = 0
            while left>=0 and right<=len(s)-1 and s[left] == s[right]:
                temp += 1
                left -= 1
                right += 1
            return temp
            
        ans = 0
        for mid in range(len(s)):
            ans += helper(mid, mid)
            if mid != len(s)-1:
                ans += helper(mid, mid+1)
        return ans
        