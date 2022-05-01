# 844. Backspace String Compare
# Easy

# 4071

# 194

# Add to List

# Share
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

 

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# Example 3:

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
 

# Constraints:

# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.
 

# Follow up: Can you solve it in O(n) time and O(1) space?


# This solution works:


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        arr1 = []
        for elem in s:
            if elem == '#':
                if arr1:
                    arr1.pop()
            else:
                arr1.append(elem)
                
        arr2 = []
        for elem in t:
            if elem == '#':
                if arr2:
                    arr2.pop()
            else:
                arr2.append(elem)
        
        return arr1 == arr2