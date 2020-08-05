# Given an array of meeting time intervals consisting of start and
# end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number
# of conference rooms required.

# Example 1:

# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# 0                        30 -> 1
#       5 10  15 20           -> 1
#                                2

# Input: [[0, 14],[5, 16],[15, 20],[17,20]]
                                #   i
# [[0,14], [5,16]]
#    [qs,qe]  

# c = 3

# Example 2:

# Input: [[7,10],[2,4]]
# Output: 1

# [[2,4],[7,10]]
# 2   4<->7

from collections import deque
class Solution:
    def minMeetingRooms(self, intervals):
        queue = deque([])
        intervals.sort()
        for start, end in intervals:
            if not queue:
                queue.append((start,end))
            else:
                for i in range(len(queue)):
                    q_s,q_e = queue[i] 
                    if q_s<start and start<q_e:
                        queue.append((start,end))
                        break
                    elif q_e<=start:
                        queue.pop(i)
                        break
        return len(queue)
                    

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        queue = []
        intervals.sort()
        for start, end in intervals:
            if not queue:
                queue.append((start,end))
            else:
                for i in range(len(queue)):
                    q_s,q_e = queue[i] 
                    if q_e <= start:
                        queue.pop(i)
                        queue.append((start, end))
                        break
                else:
                    queue.append((start, end))
        return len(queue)

s = Solution()
s.minMeetingRooms([[5,0],[0,11],[0,10]])