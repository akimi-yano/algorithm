# 1189. Maximum Number of Balloons
# Easy

# 798

# 60

# Add to List

# Share
# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

# Example 1:



# Input: text = "nlaebolko"
# Output: 1
# Example 2:



# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0
 

# Constraints:

# 1 <= text.length <= 104
# text consists of lower case English letters only.


# This solution works:


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        goal_count = Counter('balloon')
        text_count = Counter(text)
        min_total = float('inf')
        
        for char in goal_count:
            min_total = min(min_total, text_count[char] // goal_count[char] )
        return min_total
