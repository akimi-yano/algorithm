# 1323. Maximum 69 Number
# Easy

# 388

# 65

# Add to List

# Share
# Given a positive integer num consisting only of digits 6 and 9.

# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).



# Example 1:

# Input: num = 9669
# Output: 9969
# Explanation: 
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666. 
# The maximum number is 9969.
# Example 2:

# Input: num = 9996
# Output: 9999
# Explanation: Changing the last digit 6 to 9 results in the maximum number.
# Example 3:

# Input: num = 9999
# Output: 9999
# Explanation: It is better not to apply any change.


# Constraints:

# 1 <= num <= 10^4
# num's digits are 6 or 9.


# This solution works:
class Solution:
    def maximum69Number (self, num: int) -> int:
        flipped = False
        num_str = str(num)
        ans = ""
        for n in num_str:
            if n == "9":
                ans += n
            else:
                if not flipped:
                    flipped = True
                    ans += "9"
                else:
                    ans += "6"
        return ans


# This solution works:
class Solution:
    def maximum69Number (self, num: int) -> int:
        temp = num
        digit = 0
        pos = 0
        while temp:
            digit +=1
            if temp%10 == 6:
                pos = digit
            temp //=10

        ans = 0
        cur = 1
        while num:
            if cur == pos:
                ans += 9 *10 ** (cur -1)
            else:
                ans+= (num%10)*10 **(cur -1)
            num//=10
            cur+=1
        return ans
        
# This solution works !
class Solution:
    def maximum69Number(self, num):
        return int(str(num).replace('6', '9', 1))