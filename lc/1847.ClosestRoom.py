# 1847. Closest Room
# Hard

# 102

# 6

# Add to List

# Share
# There is a hotel with n rooms. The rooms are represented by a 2D integer array rooms where rooms[i] = [roomIdi, sizei] denotes that there is a room with room number roomIdi and size equal to sizei. Each roomIdi is guaranteed to be unique.

# You are also given k queries in a 2D array queries where queries[j] = [preferredj, minSizej]. The answer to the jth query is the room number id of a room such that:

# The room has a size of at least minSizej, and
# abs(id - preferredj) is minimized, where abs(x) is the absolute value of x.
# If there is a tie in the absolute difference, then use the room with the smallest such id. If there is no such room, the answer is -1.

# Return an array answer of length k where answer[j] contains the answer to the jth query.

 

# Example 1:

# Input: rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]
# Output: [3,-1,3]
# Explanation: The answers to the queries are as follows:
# Query = [3,1]: Room number 3 is the closest as abs(3 - 3) = 0, and its size of 2 is at least 1. The answer is 3.
# Query = [3,3]: There are no rooms with a size of at least 3, so the answer is -1.
# Query = [5,2]: Room number 3 is the closest as abs(3 - 5) = 2, and its size of 2 is at least 2. The answer is 3.
# Example 2:

# Input: rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]]
# Output: [2,1,3]
# Explanation: The answers to the queries are as follows:
# Query = [2,3]: Room number 2 is the closest as abs(2 - 2) = 0, and its size of 3 is at least 3. The answer is 2.
# Query = [2,4]: Room numbers 1 and 3 both have sizes of at least 4. The answer is 1 since it is smaller.
# Query = [2,5]: Room number 3 is the only room with a size of at least 5. The answer is 3.
 

# Constraints:

# n == rooms.length
# 1 <= n <= 105
# k == queries.length
# 1 <= k <= 104
# 1 <= roomIdi, preferredj <= 107
# 1 <= sizei, minSizej <= 107
 

# This solution works:

from sortedcontainers import SortedList
class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        new_rooms = []
        for roomId, size in rooms:
            new_rooms.append((-size, roomId))
        new_rooms.sort()
        
        new_queries = []
        for query_idx, (preferred, minSize) in enumerate(queries):
            new_queries.append((-minSize, preferred, query_idx))
        new_queries.sort()
        
        sorted_list = SortedList()
        idx = 0
        ans = [-1 for _ in range(len(queries))]
        for minSize, preferred, query_idx in new_queries:
            while idx < len(new_rooms) and new_rooms[idx][0] <= minSize:
                sorted_list.add(new_rooms[idx][1])
                idx += 1
            option1 = sorted_list.bisect_left(preferred)
            best_room = -1
            if 0 <= option1 < len(sorted_list):
                best_room = sorted_list[option1]
            option2 = option1 - 1
            if 0 <= option2 < len(sorted_list):
                # use "<=" because option2 is smaller than option1 and is preferred when absolute distance is same
                if abs(preferred - sorted_list[option2]) <= abs(preferred - best_room):
                    best_room = sorted_list[option2]
            ans[query_idx] = best_room
        return ans
        '''
        Notes:
        [1,2,3] bisect left will get the 2 at idx at 1
        [1,3,3] bisect left will get the 3 at idx at 1
        that is why we also check bosect left -1 to consider 1 at idx at 0
        '''
            
                