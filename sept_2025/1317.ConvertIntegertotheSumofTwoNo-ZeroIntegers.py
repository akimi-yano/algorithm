'''
1317. Convert Integer to the Sum of Two No-Zero Integers
Solved
Easy
Topics
premium lock icon
Companies
Hint
No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

Given an integer n, return a list of two integers [a, b] where:

a and b are No-Zero integers.
a + b = n
The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

 

Example 1:

Input: n = 2
Output: [1,1]
Explanation: Let a = 1 and b = 1.
Both a and b are no-zero integers, and a + b = 2 = n.
Example 2:

Input: n = 11
Output: [2,9]
Explanation: Let a = 2 and b = 9.
Both a and b are no-zero integers, and a + b = 11 = n.
Note that there are other valid answers as [8, 3] that can be accepted.
 

Constraints:

2 <= n <= 104
'''

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for num in range(1, n):
            str_num = str(num)
            for s_n in str_num:
                if s_n == '0':
                    break
            else:
                the_other = n - num
                str_the_other = str(the_other)
                for s_t_o in str_the_other:
                    if s_t_o == '0':
                        break
                else:
                    return [num, the_other]
            