'''
50. Pow(x, n)
Solved
Medium
Topics
Companies
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        Instead of reducing the exponent n by 1 at each recursive call
        we will reduce it by half
        '''
        # base case
        if n == 0:
            return 1
        # handle negative case -> change it to positive
        if n < 0:
            return 1/self.myPow(x, -n)

        # odd case
        if n % 2 == 1:
            return x * self.myPow(x * x, (n-1)//2)
        # even case
        else:
            return self.myPow(x * x, n//2)
        
# Time: O(logN)
# Space: O(logN)


# Another approach which is slightly better in terms of space complexity as we are not using recursion.

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1/x
        
        ans = 1
        while n != 0:
            # odd case, make it even by using one or if n == 1 add the value
            if n % 2 == 1:
                ans = ans * x
                n = n - 1
            # even case
            x = x * x
            n = n // 2
        return ans

# Time: O(logN)
# Space: O(1)