'''
539. Minimum Time Difference
Solved
Medium
Topics
Companies
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
 

Constraints:

2 <= timePoints.length <= 2 * 104
timePoints[i] is in the format "HH:MM".
'''

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        mins = []
        for time in timePoints:
            mins.append(int(time[:2])*60+int(time[3:]))
        mins.sort()

        min_minute = inf
        for i in range(1, len(mins)):
            min_minute = min(min_minute, mins[i] - mins[i-1])

        # check the same again with first and last only as it is potentially the closest part
        min_minute = min(min_minute, (24*60-mins[-1]) + mins[0])
        return min_minute