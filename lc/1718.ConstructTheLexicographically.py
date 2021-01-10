# 1718. Construct the Lexicographically Largest Valid Sequence
# Medium

# 61

# 5

# Add to List

# Share
# Given an integer n, find a sequence that satisfies all of the following:

# The integer 1 occurs once in the sequence.
# Each integer between 2 and n occurs twice in the sequence.
# For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
# The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

# Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

# A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.


# Example 1:

# Input: n = 3
# Output: [3,1,2,3,2]
# Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
# Example 2:

# Input: n = 5
# Output: [5,3,1,4,3,5,2,4,2]


# Constraints:

# 1 <= n <= 20

# This solution works - back tracking

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0 for _ in range(n*2-1)]
        used = set([])
        
        
        def helper(idx):
            if len(used) == n:
                return True
            if idx >= len(ans):
                return False
            if ans[idx] != 0:
                return helper(idx+1)

            for num in range(n, 0, -1):
                if num in used:
                    continue
                if num != 1 and (idx+num >= len(ans) or ans[idx+num] != 0):
                    continue
                
                # fill ans
                used.add(num)
                ans[idx] = num
                if num != 1:
                    ans[idx+num] = num

                if helper(idx+1):
                    return True
                
                # else, backtrack
                if num != 1:
                    ans[idx+num] = 0
                ans[idx] = 0
                used.remove(num)
            return False
            
        helper(0)
        return ans