'''
757. Set Intersection Size At Least Two
Hard
Topics
premium lock icon
Companies
You are given a 2D integer array intervals where intervals[i] = [starti, endi] represents all the integers from starti to endi inclusively.

A containing set is an array nums where each interval from intervals has at least two integers in nums.

For example, if intervals = [[1,3], [3,7], [8,9]], then [1,2,4,7,8,9] and [2,3,4,8,9] are containing sets.
Return the minimum possible size of a containing set.

 

Example 1:

Input: intervals = [[1,3],[3,7],[8,9]]
Output: 5
Explanation: let nums = [2, 3, 4, 8, 9].
It can be shown that there cannot be any containing array of size 4.
Example 2:

Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
Output: 3
Explanation: let nums = [2, 3, 4].
It can be shown that there cannot be any containing array of size 2.
Example 3:

Input: intervals = [[1,2],[2,3],[2,4],[4,5]]
Output: 5
Explanation: let nums = [1, 2, 3, 4, 5].
It can be shown that there cannot be any containing array of size 4.
 

Constraints:

1 <= intervals.length <= 3000
intervals[i].length == 2
0 <= starti < endi <= 108
'''

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort intervals by their end ascending. If end are equal, sort by start descending (this helps minimize additions).
        intervals.sort(key=lambda x: (x[1], -x[0]))

        # Keep two variables a and b for the last two chosen integers (initialize to very small values).
        a = float('-inf')
        b = float('-inf')
        ans = 0

        # For every interval [l, r]:
        for l, r in intervals:
            # If l > b: neither a nor b are in [l,r]. I add two numbers r-1 and r. Update a = r-1, b = r, and increase answer by 2.
            if l > b:
                ans += 2
                a = r - 1
                b = r
            # Else if l > a: only b is in [l,r]. I add one number r. Update a = b, b = r, and increase answer by 1.
            elif l > a:
                ans += 1
                a = b
                b = r
            # Else: both a and b are in [l,r]. Do nothing.
            else:
                pass
        return ans