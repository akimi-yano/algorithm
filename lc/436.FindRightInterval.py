# 436. Find Right Interval

# Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

# For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

# Note:

# You may assume the interval's end point is always bigger than its start point.
# You may assume none of these intervals have the same start point.


# Example 1:

# Input: [ [1,2] ]

# Output: [-1]

# Explanation: There is only one interval in the collection, so it outputs -1.


# Example 2:

# Input: [ [3,4], [2,3], [1,2] ]

# Output: [-1, 0, 1]

# Explanation: There is no satisfied "right" interval for [3,4].
# For [2,3], the interval [3,4] has minimum-"right" start point;
# For [1,2], the interval [2,3] has minimum-"right" start point.


# Example 3:

# Input: [ [1,4], [2,3], [3,4] ]

# Output: [-1, 2, -1]

# Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
# For [2,3], the interval [3,4] has minimum-"right" start point.
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.



# This solution passed 11/17 test cases but TLEd !!!! Not recommended ! 

# import heapq
# class Solution:
#     def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
#         minheap = []
#         ans = []
#         for i in range(len(intervals)):
#             start,end = intervals[i]
#             heapq.heappush(minheap,(start,end,i))
        
#         for i in range(len(intervals)):
#             starti,endi = intervals[i]
#             temp = []
#             added = False
#             while minheap:
#                 startj,endj,j = heapq.heappop(minheap)
#                 temp.append((startj,endj,j))
#                 if i!=j and endi<=startj:
#                     ans.append(j)
#                     added = True
#                     break
#             if not added:
#                 ans.append(-1)
#             while temp:
#                 heapq.heappush(minheap,temp.pop())
        
#         return ans


# Need to make sure that I am comparing the start and the end
# This solution works !

import heapq
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        # save the index and sort 
        new_intervals = []
        for j in range(len(intervals)):
            start,end = intervals[j]
            new_intervals.append((start,end,j))
        new_intervals.sort()
        
        # make a minheap for end
        minheap = []
        # initialize ans arr with -1s and update it as it goes
        ans = [-1 for interval in intervals]
        for start,end,j in new_intervals:
            # start larger than or equal to previous end 
            while minheap and minheap[0][0] <= start:
                _, i = heapq.heappop(minheap)
                ans[i] = j
            heapq.heappush(minheap, (end, j))
        return ans 
    
    
    
# This solution also works ! binary search :) but the same time complexity and space complexity

import heapq
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_and_idx = [(start, i) for i, (start, end) in enumerate(intervals)]
        start_and_idx.sort()
        print(start_and_idx)
        
        def helper(start_and_idx, input_end):
            left = 0
            right = len(start_and_idx)
            while left < right:
                mid = (left + right) // 2
                start, idx = start_and_idx[mid]
                if start < input_end:
                    left = mid + 1
                else:
                    right = mid
            if left >= len(start_and_idx):
                return -1
            return start_and_idx[left][1]
        
        ans = []
        for _, end in intervals:
            right_interval_idx = helper(start_and_idx, end)
            ans.append(right_interval_idx)
        
        return ans