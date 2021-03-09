# 306. Additive Number
# Medium

# 498

# 492

# Add to List

# Share
# Additive number is a string whose digits can form additive sequence.

# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

# Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

 

# Example 1:

# Input: "112358"
# Output: true
# Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
#              1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# Example 2:

# Input: "199100199"
# Output: true
# Explanation: The additive sequence is: 1, 99, 100, 199. 
#              1 + 99 = 100, 99 + 100 = 199
 

# Constraints:

# num consists only of digits '0'-'9'.
# 1 <= num.length <= 35
# Follow up:
# How would you handle overflow for very large input integers?

# This solution works:

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        def helper(prev1, prev2, idx):
            nonlocal num
            if idx >= len(num):
                return True
            cur_str = str(prev1 + prev2)
            if cur_str != num[idx:idx+len(cur_str)]:
                return False
            return helper(prev2, int(cur_str), idx+len(cur_str))
            
        for first in range(1, len(num)):
            for second in range(first+1, len(num)):
                num1 = num[:first]
                num2 = num[first:second]
                if len(num2) == 0:
                    continue
                if len(num2) > 1 and num2[0] == '0':
                    continue
                if len(num1) > 1 and num1[0] == '0':
                    continue
                if helper(int(num1), int(num2), len(num1)+len(num2)):
                    return True
        return False
