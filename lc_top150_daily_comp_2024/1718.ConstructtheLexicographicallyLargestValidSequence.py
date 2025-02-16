'''
1718. Construct the Lexicographically Largest Valid Sequence
Medium
Topics
Companies
Hint
Given an integer n, find a sequence that satisfies all of the following:

The integer 1 occurs once in the sequence.
Each integer between 2 and n occurs twice in the sequence.
For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.

 

Example 1:

Input: n = 3
Output: [3,1,2,3,2]
Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
Example 2:

Input: n = 5
Output: [5,3,1,4,3,5,2,4,2]
 

Constraints:

1 <= n <= 20
'''

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # backtracking
        # construct it from lagest to smallest
        def helper(i):
            if not unseen:
                return True
            if ans[i]:
                return helper(i+1)
            # check from the largest
            for num in reversed(range(1,n+1)):
                j = i + num if num != 1 else i
                if num in unseen and j < n+n-1 and not ans[j]:
                    ans[i] = ans[j] = num
                    unseen.remove(num)

                    if helper(i+1):
                        return True
                    # back tracking
                    ans[i] = ans[j] = 0
                    unseen.add(num)
        
        ans = [0] * (n+n-1)
        unseen = set(range(1,n+1))
        helper(0)
        return ans
