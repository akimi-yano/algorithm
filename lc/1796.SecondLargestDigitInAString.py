# 1796. Second Largest Digit in a String
# Easy

# 12

# 14

# Add to List

# Share
# Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

# An alphanumeric string is a string consisting of lowercase English letters and digits.

 

# Example 1:

# Input: s = "dfa12321afd"
# Output: 2
# Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
# Example 2:

# Input: s = "abc1111"
# Output: -1
# Explanation: The digits that appear in s are [1]. There is no second largest digit. 
 

# Constraints:

# 1 <= s.length <= 500
# s consists of only lowercase English letters and/or digits.

# This solution works:

class Solution:
    def secondHighest(self, s: str) -> int:
        nums = []
        alpha = set("abcdefghijklmnopqrstuvwxyz")
  
        for elem in s:
            if elem not in alpha:
                nums.append(int(elem))
        nums = list(set(nums))
        nums.sort(reverse=True)

        if len(nums) < 2:
            return -1
        return nums[1]
    