# 1035. Uncrossed Lines
# Medium

# 991

# 23

# Add to List

# Share
# We write the integers of A and B (in the order they are given) on two separate horizontal lines.

# Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

# A[i] == B[j];
# The line we draw does not intersect any other connecting (non-horizontal) line.
# Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

# Return the maximum number of connecting lines we can draw in this way.


# Example 1:


# Input: A = [1,4,2], B = [1,2,4]
# Output: 2
# Explanation: We can draw 2 uncrossed lines as in the diagram.
# We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
# Example 2:

# Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
# Output: 3
# Example 3:

# Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
# Output: 2


# Note:

# 1 <= A.length <= 500
# 1 <= B.length <= 500
# 1 <= A[i], B[i] <= 2000

# This solution works !:

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:

        memo = {}
        def helper(i, j):
            key = (i, j)
            if key in memo:
                return memo[key]
            count = 0
            if i > len(A)-1 or j > len(B)-1:
                pass
            
            else:
                while i <= len(A)-1 and j <= len(B)-1 and A[i] == B[j]:
                    i += 1
                    j += 1
                    count += 1
                count += max(helper(i, j+1), helper(i+1, j))
            
            memo[key] = count
            return count 
        
        return helper(0, 0)

# This solution works !
'''
optimization: preprocessing the dictionary with value with all the indexes ! 
'''

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        memo = {}
        num_locs = {}
        
        def search(idxs, prev_idx):
            left, right = 0, len(idxs) - 1
            while left < right:
                mid = (left + right) // 2
                if idxs[mid] <= prev_idx:
                    left = mid + 1
                else:
                    right = mid
            return idxs[left] if idxs[left] > prev_idx else None

        def helper(aidx, prev_bidx):
            key = (aidx, prev_bidx)
            if key in memo:
                return memo[key]

            ans = 0
            if aidx >= len(A):
                pass
            else:
                elem = A[aidx]
                # option 1: skip A[aidx]
                ans = helper(aidx+1, prev_bidx)
                # option 2: pair A[aidx]
                if elem in num_locs:
                    bidxs = num_locs[elem]
                    bidx = search(bidxs, prev_bidx)
                    if bidx is not None:
                        ans = max(ans, 1 + helper(aidx + 1, bidx))
            memo[key] = ans
            return ans
        
        for i, b in enumerate(B):
            if b not in num_locs:
                num_locs[b] = []
            num_locs[b].append(i)
        
        return helper(0, -1)