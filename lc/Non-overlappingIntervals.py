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