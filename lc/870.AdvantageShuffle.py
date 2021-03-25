# 870. Advantage Shuffle
# Medium

# 909

# 57

# Add to List

# Share
# Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

# Return any permutation of A that maximizes its advantage with respect to B.

 

# Example 1:

# Input: A = [2,7,11,15], B = [1,10,4,11]
# Output: [2,11,7,15]
# Example 2:

# Input: A = [12,24,8,32], B = [13,25,32,11]
# Output: [24,32,8,12]
 

# Note:

# 1 <= A.length = B.length <= 10000
# 0 <= A[i] <= 10^9
# 0 <= B[i] <= 10^9

# This solution works:
'''
sort both A & B and B is with index
create a new answer array and if A val > B val then but A val to the smallest B's spot else put A val to the largest B's spot
'''

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        '''
        Input: A = [2,7,11,15], B = [1,10,4,11]
        Output: [2,11,7,15]
        [2,7,11,15] 
        [1,4,10,11]
        '''
        A.sort()
        newB = []
        for i, num in enumerate(B):
            newB.append((num, i))
        B = list(sorted(newB))
        ans = [None for _ in range(len(A))]
        b_small = 0
        b_large = len(B)-1
        for a in range(len(A)):
            if A[a] > B[b_small][0]:
                ans[B[b_small][1]] = A[a]
                b_small += 1
            else:
                ans[B[b_large][1]] = A[a]
                b_large -= 1
        return ans