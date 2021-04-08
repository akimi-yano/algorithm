# 17. Letter Combinations of a Phone Number
# Medium

# 5754

# 513

# Add to List

# Share
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].


# This solution works:

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        chars = {}
        count = 0
        for k in range(2,10):
            chars[str(k)] = []
            for _ in range(3):
                chars[str(k)].append( chr(ord('a')+count) )
                count += 1
            if k == 7 or k == 9:
                chars[str(k)].append( chr(ord('a')+count) )
                count += 1

        def helper(i):
            if i > len(digits)-1:
                return [[]]
            ans = []
            for num in chars[digits[i]]:
                ans.extend([num]+arr for arr in helper(i+1))
            return ans
        return ["".join(arr) for arr in helper(0)]
            