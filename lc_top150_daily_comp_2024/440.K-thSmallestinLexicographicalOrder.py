'''
440. K-th Smallest in Lexicographical Order
Solved
Hard
Topics
Companies
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

 

Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
Example 2:

Input: n = 1, k = 1
Output: 1
 

Constraints:

1 <= k <= n <= 109
'''

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        '''
               _
          / /   \    \ 
        1   2   3  ... 9  
     /   \ 
    0(10) 1(11) ...
  /
0(100) ...

        Just count the number of nodes by going to right and down
        '''
        def count_num_between_cur_and_cur_plus_one(cur):
            next_cur = cur+1
            steps = 0
            while cur <= n:
                steps += min(next_cur-cur, n-cur+1)
                cur *= 10
                next_cur *= 10
            return steps

        # cur is cur current num to the k 
        cur = 1
        # since we are starting at cur = 1, this is 0 indexed so subtract 1 from k
        k -= 1

        while k:
            # trying to see if we can go right
            dist = count_num_between_cur_and_cur_plus_one(cur)
            # going right
            if dist <= k:
                cur += 1
                k -= dist
            # going down
            else:
                cur *= 10
                k -= 1
        return cur