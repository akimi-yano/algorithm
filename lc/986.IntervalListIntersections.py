# 986. Interval List Intersections
# Medium

# 3276

# 73

# Add to List

# Share
# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

 

# Example 1:


# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Example 2:

# Input: firstList = [[1,3],[5,9]], secondList = []
# Output: []
# Example 3:

# Input: firstList = [], secondList = [[4,8],[10,12]]
# Output: []
# Example 4:

# Input: firstList = [[1,7]], secondList = [[3,10]]
# Output: [[3,7]]
 

# Constraints:

# 0 <= firstList.length, secondList.length <= 1000
# firstList.length + secondList.length >= 1
# 0 <= starti < endi <= 109
# endi < starti+1
# 0 <= startj < endj <= 109
# endj < startj+1


# This solution works:


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        idx1 = idx2 = 0
        ans = []
        while idx1 < len(firstList) and idx2 < len(secondList):
            s1, e1 = firstList[idx1]
            s2, e2 = secondList[idx2]
            if s1 <= s2 <= e1 <= e2:
                ans.append([s2,e1])
                idx1 += 1
            elif s2 <= s1 <= e2 <= e1:
                ans.append([s1, e2])
                idx2 += 1
            elif s1 <= s2 <= e2 <= e1:
                ans.append([s2, e2])
                idx2 += 1
            elif s2 <= s1 <= e1 <= e2:
                ans.append([s1, e1])
                idx1 += 1
            else:
                if e1 < e2:
                    idx1 += 1
                else:
                    idx2 += 1
        return ans    


# This solution works - code simplifications:


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        idx1 = idx2 = 0
        ans = []
        while idx1 < len(firstList) and idx2 < len(secondList):
            s1, e1 = firstList[idx1]
            s2, e2 = secondList[idx2]
            start = max(s1, s2)
            end = min(e1, e2)
            if start <= end:
                ans.append([start, end])
            if e1 <= e2:
                idx1 += 1
            if e2 <= e1:
                idx2 += 1
        return ans    