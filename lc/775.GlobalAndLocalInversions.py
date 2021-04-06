# 775. Global and Local Inversions
# Medium

# 707

# 244

# Add to List

# Share
# We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

# The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

# The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

# Return true if and only if the number of global inversions is equal to the number of local inversions.

# Example 1:

# Input: A = [1,0,2]
# Output: true
# Explanation: There is 1 global inversion, and 1 local inversion.
# Example 2:

# Input: A = [1,2,0]
# Output: false
# Explanation: There are 2 global inversions, and 1 local inversion.
# Note:

# A will be a permutation of [0, 1, ..., A.length - 1].
# A will have length in range [1, 5000].
# The time limit for this problem has been reduced.

# This solution works:

'''
use sorted list and check every time before you add new num
'''

from sortedcontainers import SortedList
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        local = 0
        for i in range(1, len(A)):
            if A[i-1] > A[i]:
                local += 1
        s_list = SortedList()
        glob = 0
        for num in A:
            idx = s_list.bisect_right(num)
            num_larger = len(s_list) - idx
            glob += num_larger
            s_list.add(num)
        return local == glob
    
# This solution works - optimization:
'''
handling local and global in the same loop
'''
from sortedcontainers import SortedList
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        s_list = SortedList()
        glob = 0
        local = 0
        for i, num in enumerate(A):
            idx = s_list.bisect_right(num)
            num_larger = len(s_list) - idx
            glob += num_larger
            s_list.add(num)
            if i == 0:
                continue
            if A[i-1] > A[i]:
                local += 1
        return local == glob
    
# This solution works - optimization:


class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        '''
        for prevmax keep track of the max of the prevprev value
        as the rule is that the prev prev value cannot be larger than current num
        everything before previous one has to be smaller than or equal to
        if there is single one that is not following the rule, then return False
        '''
        prevmax = prev = float('-inf')
        for num in A:
            if prevmax > num:
                return False
            prevmax = max(prevmax, prev)
            prev = num
        return True
