# 43. Multiply Strings

# Given two non-negative integers num1 and num2 represented as strings, 
# return the product of num1 and num2, also represented as a string.

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"
# Note:

# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.





# this solution is invalid because it could cause int overflow in other languages
# due to """You must not use any built-in BigInteger library or convert the inputs to integer directly."""

# class Solution:
#     def multiply(self, num1: str, num2: str) -> str:
#         i_to_s={}
#         s_to_i={}
#         nums = "0123456789"
#         for i in range(len(nums)):
#             i_to_s[i]=nums[i]
#             s_to_i[nums[i]]=i
        
#         def str_to_int(num_str):
#             temp = 0
#             for k in range(len(num_str)-1,-1,-1):
#                 temp+=s_to_i[num_str[k]]*10**(len(num_str)-1-k)
#             return temp
        
#         n1 = str_to_int(num1)
#         n2 = str_to_int(num2)
#         prod = n1*n2
        
#         def int_to_str(num_int):
#             temp = []
#             while num_int:
#                 temp.append(i_to_s[num_int%10])
#                 num_int//=10
#             temp.reverse()
#             return "".join(temp)
        
#         ans = int_to_str(prod)
#         return "0" if len(ans)==0 else ans
        
        
        
        
# The solution that works !!!

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        ans = []
        for i, n1 in enumerate(reversed(num1)):
            carry = 0
            for j, n2 in enumerate(reversed(num2)):
                value = int(n1) * int(n2) + carry
                carry, digit = divmod(value, 10)
                self.add_to_ans(ans, digit, i+j)
            if carry > 0:
                self.add_to_ans(ans, carry, i+len(num2))
            # print(num2, n1, ans)
        return ''.join([str(d) for d in reversed(ans)])
    
    def add_to_ans(self, ans, digit, loc):
        if loc >= len(ans):
            ans.append(digit)
            return

        # ans[loc] = (ans[loc] + digit) % 10
        # carry = (ans[loc] + digit) // 10
        # one liner version of above:
        carry, ans[loc] = divmod(ans[loc]+digit, 10)

        if carry > 0:
            self.add_to_ans(ans, carry, loc+1)