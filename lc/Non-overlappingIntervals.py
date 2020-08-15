# Non-overlapping Intervals

# Solution
# Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

# Example 1:

# Input: [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
# Example 2:

# Input: [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
# Example 3:

# Input: [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

# Note:

# You may assume the interval's end point is always bigger than its start point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.



# This works !!!!

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        memo = {}
        def helper(i):
            if i in memo:
                return memo[i]
            if i>len(intervals)-1:
                return 0
            # if we delete it at i
            min_rm = 1+helper(i+1)
            # if we dont delete it at i (but delete at different index)
            cur_end = intervals[i][1]
            next_idx = i+1
            while next_idx<len(intervals) and cur_end>intervals[next_idx][0]:
                next_idx +=1
            min_rm = min(min_rm,next_idx-(i+1)+helper(next_idx))
            memo[i] = min_rm
            return min_rm
        return helper(0)
    
    
# For these type of questions (like merge intervals, meeting rooms) 
# I am used to sort the start value (not better but just get used to). 
# The idea is keep an 'end' value (initialize it as the end of first interval), 
# loop over the rest of intervals, when there is overlap (b.begin < a.end), 
# remove an interval (remove the one the has larger end value, so end=min(a.end,b.end)); 
# when there is no overlay, just update end to the b.end.

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        if not intervals:
            return 0
        
        intervals.sort()
        
        end, remove = intervals[0][1], 0
        for i in xrange(1, len(intervals)):
            if intervals[i][0] < end: # overlap
                remove += 1
                end = min(end, intervals[i][1]) # remove the one has larger end value
            else: 
                end = intervals[i][1]
        
        return remove
    


# Did it and this works + intuitive !

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        
        end = intervals[0][1]
        count = 0
        
        for i in range(1, len(intervals)):
            if intervals[i][0]<end: #overlapping !
                count+=1
                end= min(end,intervals[i][1]) # remove the larger one
            else: 
                end = intervals[i][1]
        
        return count