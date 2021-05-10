# 1354. Construct Target Array With Multiple Sums
# Hard

# 458

# 61

# Add to List

# Share
# Given an array of integers target. From a starting array, A consisting of all 1's, you may perform the following procedure :

# let x be the sum of all elements currently in your array.
# choose index i, such that 0 <= i < target.size and set the value of A at index i to x.
# You may repeat this procedure as many times as needed.
# Return True if it is possible to construct the target array from A otherwise return False.

 

# Example 1:

# Input: target = [9,3,5]
# Output: true
# Explanation: Start with [1, 1, 1] 
# [1, 1, 1], sum = 3 choose index 1
# [1, 3, 1], sum = 5 choose index 2
# [1, 3, 5], sum = 9 choose index 0
# [9, 3, 5] Done
# Example 2:

# Input: target = [1,1,1,2]
# Output: false
# Explanation: Impossible to create target array from [1,1,1,1].
# Example 3:

# Input: target = [8,5]
# Output: true
 

# Constraints:

# N == target.length
# 1 <= target.length <= 5 * 10^4
# 1 <= target[i] <= 10^9

# This solution works:

import heapq
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        '''
        Put all negative elements to heap and evaluate sum s of all elements.
        Start to do steps: extract the biggest elements elem. If it is equal to 1, we are good: it means, that all smaller elements also equal to 1 and we can return True. If it happen that s == elem, it means that we actually have only one element in target, and it is not equal to 1: we can not do anything with it, so we return False.
        Next, we need to put new element in our heap. And here we have another subtle point: imagine, that we have [100, 3]. Then on the next step we have [97, 3], then [94, 3] and so on. In the given example we need only 33 steps to converge, however if we have [10000000, 1] we will get TLE for sure. Note, that what we did is similar to one step of Eucledian algorithm, there is classical improvement, where instead of (m, n) -> (m-n, n) step we do (m, n) -> (m%n, n) step. Note also, that in the case [99, 3] we want to stop on [3, 3], not going to [0, 3], so we need to modify step a bit: I did it using cand = (elem - 1) % (s - elem) + 1. Here s - elem is sum of all elements except elem.
        Check if cand == elem and if it is the case, it means, that we can not do the step, so we are stuch and we return False.
        Finally, we update s: subtract elem and add new element cand and push -cand to our heap.
        '''
        # start from the target and the largest one is the total sum of the rest and newnum (prevnum)
        maxheap = []
        for num in target: 
            heappush(maxheap, -num)
        total = sum(target)
        while True:
            maxnum = -heappop(maxheap)
            if maxnum == 1: 
                return True
            if total == maxnum: 
                return False
            # doing this mod because it is not efficient to do -1 many many times and do +1 later
            newnum = (maxnum - 1) % (total - maxnum) + 1
            if newnum == maxnum: 
                return False
            total = total - maxnum + newnum
            heappush(maxheap, -newnum)
        