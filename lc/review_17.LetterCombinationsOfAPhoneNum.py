# 17. Letter Combinations of a Phone Number
# Medium

# 9934

# 678

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
        if not digits:
            return []
        num_to_letters = {}
        i = 0
        for num in range(2, 10):
            num_to_letters[str(num)] = []
            turn = 3
            if num in (7,9):
                turn = 4
            for _ in range(turn):
                num_to_letters[str(num)].append(chr(ord('a')+i))
                i += 1
     
        def helper(idx):
            if idx > len(digits)-1:
                return [[]]
            ans = []
            number = digits[idx]
            for char in num_to_letters[number]:
                ans.extend([char] + temp for temp in helper(idx+1))
            return ans
  
        return ["".join(arr) for arr in helper(0)]
    