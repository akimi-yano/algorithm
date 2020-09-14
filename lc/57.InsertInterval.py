# 57. Insert Interval
# Hard

# 1963

# 203

# Add to List

# Share
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.



# This approach does not work:

# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         start, end = newInterval
#         # print(start,end)
        
#         lo, hi = 0, len(intervals)-1
#         while lo < hi:
#             mi = (lo+hi)//2 +1
#             s, e = intervals[mi]
   
#             if s<= start:
#                 lo = mi
#             else:
#                 hi = mi - 1
#         fin_start, e = intervals[lo]
#         start_idx = lo
#         while e<end:
#             s, e = intervals[lo]
#             intervals
#             lo+=1
#         _, fin_end = intervals[lo-1]
#         end_idx = lo-1
#         i = 0
#         ans = []
#         interval = False
#         limit = len(intervals)
#         # print(start_idx,end_idx)
#         while i<limit:
#             if not start_idx<=i<=end_idx:
#                 if interval:
#                     ans.append([fin_start,fin_end])
#                     interval = False
#             else:
#                 interval = True
#             ans.append(intervals[i])
#             i+=1
#         return ans


# This approach works !:
import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        # print(start,end)
        merged = set([])
        # find all the intervals that overlap and save the index in the set
        for i, interval in enumerate(intervals):
            s, e = interval
            if s <= new_end and e >= new_start:
                merged.add(i)
        lowest, highest = new_start, new_end
        # find the min start and max end 
        for i in merged:
            s, e = intervals[i]
            lowest = min(lowest, s)
            highest = max(highest, e)
        ans = []
        # append all the non-overlapping ones in the list
        for i, interval in enumerate(intervals):
            if i in merged:
                continue
            ans.append(interval)
        # ans.append([lowest, highest])
        # return ans
        
        # find the index (left side) for the target list [lowest, highest] using binary search and slice the array to make a new one 
        idx = bisect.bisect_left(ans, [lowest, highest])
        ans = ans[:idx] + [[lowest, highest]] + ans[idx:]
        return ans