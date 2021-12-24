# 56. Merge Intervals
# Medium

# 10845

# 459

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


# This solution works:


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        min_s, max_e = intervals[0]
        for s, e in intervals[1:]:
            if min_s <= s <= max_e <= e or min_s <= s <= e <= max_e:
                max_e = max(e, max_e)
            else:
                ans.append([min_s, max_e])
                min_s = s
                max_e = e
        ans.append([min_s, max_e])
        return ans