# 917. Reverse Only Letters
# Easy

# 1148

# 47

# Add to List

# Share
# Given a string s, reverse the string according to the following rules:

# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

 

# Example 1:

# Input: s = "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:

# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
 

# Constraints:

# 1 <= s.length <= 100
# s consists of characters with ASCII values in the range [33, 122].
# s does not contain '\"' or '\\'.


# This solution works:


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s_list = list(s)
        left = 0
        right = len(s_list)-1
        while left < right:
            if not s_list[left].isalpha():
                left += 1
            elif not s_list[right].isalpha():
                right -= 1
            else:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        return "".join(s_list)