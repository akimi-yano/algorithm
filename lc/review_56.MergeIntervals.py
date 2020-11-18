# 56. Merge Intervals
# Medium

# 5640

# 336

# Add to List

# Share
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104


# this solution works 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
        1-3
         2---6
               8-10
                    15-18
        ''' 
        ans = []
        intervals.sort(key = lambda x : (x[0],-x[1]))
        smallest_start, largest_end = intervals[0]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if smallest_start <= start <= largest_end:
                smallest_start = min(smallest_start, start)
                largest_end = max(largest_end, end)
            else:
                ans.append([smallest_start, largest_end])
                smallest_start, largest_end = start, end
        ans.append([smallest_start, largest_end])
        return ans 
    
    
# This solution works ! - optimization 

class Solution:
    '''
    Just go through the intervals sorted by start coordinate and either combine the current interval with the previous one if they overlap, or add it to the output by itself if they don't.
    '''
    def merge(self, intervals):
        out = []
        for i in sorted(intervals, key=lambda i: i[0]):
            if out and i[0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1], i[1])
            else:
                out += i,
        return out
