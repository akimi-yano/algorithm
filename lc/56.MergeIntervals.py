# 56. Merge Intervals

# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

 

# Constraints:

# intervals[i][0] <= intervals[i][1]



# This works  !!! - making a new arr to return 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 1:
            return []
        intervals.sort()
        merged = []

        prev_start, prev_end = intervals[0]
        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]
            # if the previous end is after the current start:
            if prev_end >= cur_start:
                prev_end = max(prev_end, cur_end)
            else:
                merged.append([prev_start, prev_end])
                prev_start, prev_end = cur_start, cur_end
        merged.append([prev_start, prev_end])
        return merged
    
# This is a solution without making a new arr (modified the original arr and return it)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 1:
            return []
        intervals.sort()
        insert_loc = 0

        prev_start, prev_end = intervals[0]
        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]
            # if the previous end is after the current start:
            if prev_end >= cur_start:
                prev_end = max(prev_end, cur_end)
            else:
                intervals[insert_loc] = [prev_start, prev_end]
                insert_loc += 1
                prev_start, prev_end = cur_start, cur_end
        intervals[insert_loc] = [prev_start, prev_end]
        insert_loc += 1
        while len(intervals) > insert_loc:
            intervals.pop()
        return intervals