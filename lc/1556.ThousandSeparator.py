# 1556. Thousand Separator

# Add to List

# Share
# Given an integer n, add a dot (".") as the thousands separator and return it in string format.



# Example 1:

# Input: n = 987
# Output: "987"
# Example 2:

# Input: n = 1234
# Output: "1.234"
# Example 3:

# Input: n = 123456789
# Output: "123.456.789"
# Example 4:

# Input: n = 0
# Output: "0"


# Constraints:

# 0 <= n < 2^31

class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0:
            return "0"
        ans = []
    
        while n > 0:
            ans.append(str(n%10))
            n //=10
        
        res = ""
        for i in range(len(ans)-1,-1,-1):
            res += ans[i]
            if i!=0 and i%3==0:
                res+="."
        return res