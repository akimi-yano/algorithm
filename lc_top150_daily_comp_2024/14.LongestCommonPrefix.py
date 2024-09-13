'''
14. Longest Common Prefix
Easy
Topics
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_str = strs[0]
        for i in range(1, len(strs)):
            word = strs[i]
            for j in range(len(word), -1, -1):
                if word[:j] == common_str[:j]:
                    common_str = common_str[:j]
                    break
        return common_str

# Time: O(S*W)
# Space: O(S*W)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def is_prefix_valid(length):
            maybe_prefix = strs[0][:length]
            for i in range(1, len(strs)):
                word = strs[i]
                if word[:length] != maybe_prefix:
                    return False
            return True

        min_length = float('inf')
        for word in strs:
            min_length = min(min_length, len(word))
    
        left = 0
        right = min_length
        while left < right:
            mid = (left + right + 1) // 2
            if is_prefix_valid(mid):
                left = mid
            else:
                right = mid - 1
        return strs[0][:left]

# Time: O(logW * S) <- binary search of the length of prefix which is the min length of the word W * S is the length of strs
# Space: O(S*W) <- slicing still creates a copy