'''
70. Climbing Stairs
Easy
18.1K
569
Companies
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        
        '''
        either climb 1 or 2 step to get to n
        3
        
        helper(2) + helper(1)
        helper(2-1=1) + helper(2-2=0) + helper(1)
        
        2 
        helper(2)
        
        '''
        
        def helper(n):
            if n in memo:
                return memo[n]
            if n == 1:
                return 1
            elif n == 2:
                return 2
            total = helper(n-1) + helper(n-2)
            memo[n] = total 
            return memo[n]
        memo = {}
        return helper(n)

'''
Another approach
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        prevprev = 1
        prev = 2
        
        for num in range(3, n+1):
            total = prev + prevprev
            prevprev = prev
            prev = total 

        return total
