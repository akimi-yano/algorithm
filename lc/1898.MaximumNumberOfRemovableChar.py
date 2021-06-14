# 1898. Maximum Number of Removable Characters
# Medium

# 229

# 51

# Add to List

# Share
# You are given two strings s and p where p is a subsequence of s. You are also given a distinct 0-indexed integer array removable containing a subset of indices of s (s is also 0-indexed).

# You want to choose an integer k (0 <= k <= removable.length) such that, after removing k characters from s using the first k indices in removable, p is still a subsequence of s. More formally, you will mark the character at s[removable[i]] for each 0 <= i < k, then remove all marked characters and check if p is still a subsequence.

# Return the maximum k you can choose such that p is still a subsequence of s after the removals.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

 

# Example 1:

# Input: s = "abcacb", p = "ab", removable = [3,1,0]
# Output: 2
# Explanation: After removing the characters at indices 3 and 1, "abcacb" becomes "accb".
# "ab" is a subsequence of "accb".
# If we remove the characters at indices 3, 1, and 0, "abcacb" becomes "ccb", and "ab" is no longer a subsequence.
# Hence, the maximum k is 2.
# Example 2:

# Input: s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]
# Output: 1
# Explanation: After removing the character at index 3, "abcbddddd" becomes "abcddddd".
# "abcd" is a subsequence of "abcddddd".
# Example 3:

# Input: s = "abcab", p = "abc", removable = [0,1,2,3,4]
# Output: 0
# Explanation: If you remove the first index in the array removable, "abc" is no longer a subsequence.
 

# Constraints:

# 1 <= p.length <= s.length <= 105
# 0 <= removable.length < s.length
# 0 <= removable[i] < s.length
# p is a subsequence of s.
# s and p both consist of lowercase English letters.
# The elements in removable are distinct.

# This solution works:

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        def helper(mid):
            temp = []
            for idx in range(mid+1):
                i = removable[idx]
                temp.append((i, new_s[i]))
                new_s[i] = "#"
            s_l = len(new_s)
            p_l = len(p)
            s_i = p_i = 0
            while p_i < p_l and s_i < s_l:
                if p[p_i] == new_s[s_i]:
                    s_i += 1
                    p_i += 1
                else:
                    s_i += 1
            if p_i >= p_l:
                return True
            else:
                while temp:
                    i, elem = temp.pop()
                    new_s[i] = elem
                return False
        
        new_s = list(s)
        left = 0
        right = len(removable)-1
        while left < right:
            mid = (left+right+1)//2
            if not helper(mid):
                right = mid-1
            else:
                left = mid
        if not helper(left):
            return 0
        return left+1