'''
386. Lexicographical Numbers
Solved
Medium
Topics
Companies
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]
 

Constraints:

1 <= n <= 5 * 104
'''

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        num = 1
        '''
        1 -> ok
        10 -> ok
        100 -> not ok
          100 -> 10
          10 -> 11
        11 -> ok
        110 -> not ok
          110 -> 11
          11 -> 12
        
        '''
        while True:
            if num <= n:
                ans.append(num)
                if len(ans) == n:
                    return ans
                num *= 10
            else:
                num //= 10
                while num % 10 == 9:
                    num //= 10
                num += 1

# Try and error approach :)