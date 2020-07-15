# 215. Kth Largest Element in an Array
# Medium

# Share
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Example 1:

# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:

# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.

# my solution - O(NlogK)
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = [nums[0]]
        j = 1
        
        # fill the minheap for the capacity of k
        while len(minheap)<k:
            heapq.heappush(minheap,nums[j])
            j+=1
            
        # only swap what is in the minheap if the elem is larger than minheap[0]
        for i in range(j, len(nums)):
            if nums[i]>minheap[0]:
                heapq.heappop(minheap)
                heapq.heappush(minheap,nums[i])
                
        return minheap[0]



# same solution with heap library methods
# k+(n-k)*log(k) time
def findKthLargest1(self, nums, k):
    heap = nums[:k]
    heapq.heapify(heap)  # create a min-heap whose size is k 
    for num in nums[k:]:
        if num > heap[0]:
           heapq.heapreplace(heap, num)
        # or use:
        # heapq.heappushpop(heap, num)
    return heap[0]
  
  
# fastest
# O(n) time, (worst case O(N^2) especially for duplicates) quicksort-Partition method   
# If there are lots of duplictes it becomes 0(N^2) - because the pivot only can move -1 from the last elem of arr
def findKthLargest(self, nums, k):
    pos = self.partition(nums, 0, len(nums)-1)
    if pos > len(nums) - k:
        return self.findKthLargest(nums[:pos], k-(len(nums)-pos))
    elif pos < len(nums) - k:
        return self.findKthLargest(nums[pos+1:], k)
    else:
        return nums[pos]
 
# Lomuto partition scheme   
def partition(self, nums, l, r):
    pivot = nums[r]
    lo = l 
    for i in xrange(l, r):
        if nums[i] < pivot:
            nums[i], nums[lo] = nums[lo], nums[i]
            lo += 1
    nums[lo], nums[r] = nums[r], nums[lo]
    return lo

# with extra storage, quick select, O(n) even with duplicates (space : O(N))


