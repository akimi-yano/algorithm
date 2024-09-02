'''
56. Merge Intervals
Solved
Medium
Topics
Companies
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''

# This approach works:

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        intervals = [[1,3],[2,6],[8,10],[15,18]]

                    1---3
                      2----6
                               8----10
                                         15---18
        '''
        '''
        [[1,4],[2,3]]
                    1------4
                      2--3
        '''
        stack = []
        # by sorting i can garantee that the start is ordered from small to large, but still need to check for the end
        intervals.sort()
        for start, end in intervals:
            if stack and stack[-1][1] >= start:
                prev_start, prev_end = stack.pop()
                stack.append([prev_start, max(prev_end, end)])
            else:
                stack.append([start, end])
        return stack
    
    # Time: O(NlogN) sorted
    # Space: O(N) for creating answer list