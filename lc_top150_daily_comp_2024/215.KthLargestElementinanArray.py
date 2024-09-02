'''
215. Kth Largest Element in an Array
Solved
Medium
Topics
Companies
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
'''

# This solution works!

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        [3,2,1,5,6,4], k = 2
                   ^
        minheap
        head->{ 5
              6
        } <- kth largest is the smallest elem of the k capacity heap
        '''
        minheap = []
        for num in nums:
            # とりあえずヒープに入れる
            heapq.heappush(minheap, num)
            # k より多くなったら、トップからポップする。
            if len(minheap) > k:
                heapq.heappop(minheap)
        return minheap[0]
    
# Time: O(NlogK) where N is the number of elements on the list nums and the logK is the each operation of heap (fact: height of the heap that has k element is log k)
# Space: O(K) where k is the capacity of the heap 