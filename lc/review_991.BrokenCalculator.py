# 991. Broken Calculator
# Medium

# 1076

# 146

# Add to List

# Share
# There is a broken calculator that has the integer startValue on its display initially. In one operation, you can:

# multiply the number on display by 2, or
# subtract 1 from the number on display.
# Given two integers startValue and target, return the minimum number of operations needed to display target on the calculator.

 

# Example 1:

# Input: startValue = 2, target = 3
# Output: 2
# Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
# Example 2:

# Input: startValue = 5, target = 8
# Output: 2
# Explanation: Use decrement and then double {5 -> 4 -> 8}.
# Example 3:

# Input: startValue = 3, target = 10
# Output: 3
# Explanation: Use double, decrement and double {3 -> 6 -> 5 -> 10}.
 

# Constraints:

# 1 <= x, y <= 109


# This solution works:


class Solution:
    def brokenCalc(self, X, Y):
        '''
        Approach 1: Work Backwards
        Intuition

        Instead of multiplying by 2 or subtracting 1 from X, we could divide by 2 (when Y is even) or add 1 to Y.

        The motivation for this is that it turns out we always greedily divide by 2:

        If say Y is even, then if we perform 2 additions and one division, we could instead perform one division and one addition for less operations [(Y+2) / 2 vs Y/2 + 1].

        If say Y is odd, then if we perform 3 additions and one division, we could instead perform 1 addition, 1 division, and 1 addition for less operations [(Y+3) / 2 vs (Y+1) / 2 + 1].

        Algorithm

        While Y is larger than X, add 1 if it is odd, else divide by 2. After, we need to do X - Y additions to reach X.
        
        '''    
        ans = 0
        while Y > X:
            ans += 1
            if Y%2: Y += 1
            else: Y //= 2

        return ans + X-Y