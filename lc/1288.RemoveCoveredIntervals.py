# 1288. Remove Covered Intervals
# Medium

# 354

# 18

# Add to List

# Share
# Given a list of intervals, remove all intervals that are covered by another interval in the list.

# Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

# After doing so, return the number of remaining intervals.

 

# Example 1:

# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
# Example 2:

# Input: intervals = [[1,4],[2,3]]
# Output: 1
# Example 3:

# Input: intervals = [[0,10],[5,12]]
# Output: 2
# Example 4:

# Input: intervals = [[3,10],[4,10],[5,11]]
# Output: 2
# Example 5:

# Input: intervals = [[1,2],[1,4],[3,4]]
# Output: 1
 

# Constraints:

# 1 <= intervals.length <= 1000
# intervals[i].length == 2
# 0 <= intervals[i][0] < intervals[i][1] <= 10^5
# All the intervals are unique.



# This approach does not work
# class Solution:
#     def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
#         intervals = sorted(intervals, key = lambda elem: elem[1])
#         # print(intervals)
#         prev_s, prev_e = intervals[0]
#         rm = 0
#         for s, e in intervals[1:]:
#             if s <= prev_s:
#                 rm += 1
#             prev_s = s
#             prev_e = e
#         return len(intervals) - rm


# This approach does not work
# class Solution:
#     def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
#         # intervals = sorted(intervals, key = lambda elem: elem[1])
#         # print(intervals)
#         intervals.sort()
#         prev_s, prev_e = intervals[0]
#         rm = 0
#         for s, e in intervals[1:]:
#             if( s <= prev_s and prev_e <= e)or(prev_s <= s and e <= prev_e):
#                 rm += 1
#             prev_s = s
#             prev_e = e
#         return len(intervals) - rm



# This solution works: O(N^2) 
'''
we know that the brute force works because of the constraints: 1 <= intervals.length <= 1000

if N = 1000 (10 ^3)
N^2 is (10^6)

TLE happens around 10^8 so this brute force could pass the test cases - don't forget to break and substract from the N at the end
'''

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        count = 0
        
        for i, (s1,e1) in enumerate(intervals):
            for j, (s2, e2) in enumerate(intervals):
                if i == j:
                    continue
                if s2 <= s1 and e1 <= e2:
                    count += 1
                    break
        return N - count
    

# This solution works and  very intutive ! 
# Complexity: time O(NlogN), space O(1)

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        '''
        1 sort 
        start: small -> large
        end: large -> small
        
        2 keep track of the max_end and compare with cur_end
        if cur_end is smaller than max_end, there is overlap 
        '''
        N = len(intervals)
        remove = 0
        intervals.sort(key = lambda elem: (elem[0], -elem[1]))
        max_end = float('-inf')
        for start, end in intervals:
            if end <= max_end:
                remove += 1
            max_end = max(max_end, end)
        return N - remove