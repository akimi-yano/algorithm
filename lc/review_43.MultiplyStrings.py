# 43. Multiply Strings
# Medium

# 3359

# 1332

# Add to List

# Share
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"
 

# Constraints:

# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.


# This solution works:


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        10
        10
       x
        '''
        def helper(arr, start, num):
            i = start
            while num:
                while i >= len(arr):
                    arr.append(0)
                new_num = (arr[i] + num) // 10
                arr[i] = (arr[i] + num) % 10
                i += 1
                num = new_num

        ans = [0]
        for i, n1 in enumerate(reversed(num1)):
            for j, n2 in enumerate(reversed(num2)):
                helper(ans, i + j, int(n1) * int(n2))
        return ''.join(reversed([str(elem) for elem in ans]))
