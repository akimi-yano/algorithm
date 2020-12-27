# 1703. Minimum Adjacent Swaps for K Consecutive Ones
# Hard

# 40

# 2

# Add to List

# Share
# You are given an integer array, nums, and an integer k. nums comprises of only 0's and 1's. In one move, you can choose two adjacent indices and swap their values.

# Return the minimum number of moves required so that nums has k consecutive 1's.

 

# Example 1:

# Input: nums = [1,0,0,1,0,1], k = 2
# Output: 1
# Explanation: In 1 move, nums could be [1,0,0,0,1,1] and have 2 consecutive 1's.
# Example 2:

# Input: nums = [1,0,0,0,0,0,1,1], k = 3
# Output: 5
# Explanation: In 5 moves, the leftmost 1 can be shifted right until nums = [0,0,0,0,0,1,1,1].
# Example 3:

# Input: nums = [1,1,0,1], k = 2
# Output: 0
# Explanation: nums already has 2 consecutive 1's.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is 0 or 1.
# 1 <= k <= sum(nums)


'''


We consider a more complex test case nums = [1,0,1,0,0,1,1,0,0,0,1,1,0,1] and k=4

In this problem, only the position of ones is relevant.

pos = [p for p,x in enumerate(nums) if x == 1]
# [0, 2, 5, 6, 10, 11, 13]
The problem is now to consider every sliding window of side k. The task is to move each element of the window to the median of the window. (If k is even, we can choose either of the two most middle positions). If we calculate the cost from scratch for each of the window, we will TLE. We need to use the cost of one window to compute the cost of the next window.

This is the trick - we consider pos[i] - i for each of the ones. The idea is this - if the current element is the jth element in the window and the left most element in the window is j units away you do not need to move the element.

it is a common trick in competitive programming to use a[i] - i to convert a "min sum of moves to make numbers consecutive" problem into a "min sum of moves to a single point".

pos = [p-i for i,p in enumerate(pos)]
# [0, 1, 3, 3, 6, 6, 7]
The problem now is to consider every sliding window of side k - the difference of each element in the window with its median. In this example, k=4 and it is now quite obvious that we will choose the right-most window for the cost of 4.

We want to reuse the computation for one sliding window for the next sliding window.

We split the sliding window into three parts - the median, the part left of the median and the part right of the median. We consider the cost of the left and right parts separately.

Before: abc | d | e   fg
After:   bc   d | e | fgh
The old median is d and the new median is e.

Before the window moves

   .   .   .
       .   .
           .
 a   b   c   d   e   f   g  (h)
               .   .   .
               .   .
               .
After the window moves

       .   .   .
           .   .
               .
(a)  b   c   d   e   f   g   h
                   .   .   .
                   .   .
                   .
Comparing the difference, x is lost, o is added.

   x   .   .   o
       x   .   o
           x   o
 a   b   c   d   e   f   g   h
               x   .   .   o
               x   .   o
               x   o
In summary

For the left part, the cost decreases by d-a and increases by (e-d)*sizeleft
For the right part, the cost increases by h-e and decreases by (e-d)*sizeright
The similar procedure happens if k is even, but sizeleft is not the same as sizeright.

Before: abc | d | e   f
After:   bc   d | e | fg

'''
# This solution works 

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        pos = [p for p,x in enumerate(nums) if x == 1]

        # it is just the number of zeros up to that specific 1
        pos = [p-i for i,p in enumerate(pos)]        
        
        mid = k//2
        sizeleft = mid
        sizeright = k-1-sizeleft
        
        curleft = sum(abs(x - pos[mid]) for x in pos[:sizeleft])
        curright = sum(abs(x - pos[mid]) for x in pos[mid+1:k])        
        minres = curleft + curright
        
        for ptr in range(1, len(pos)-k+1):
            curleft -= (pos[ptr+mid-1] - pos[ptr-1])
            curleft += (pos[ptr+mid] - pos[ptr+mid-1]) * sizeleft
            
            curright -= (pos[ptr+mid] - pos[ptr+mid-1]) * sizeright
            curright += (pos[ptr+k-1] - pos[ptr+mid])
            
            minres = min(minres, curleft+curright)
            
        return minres

