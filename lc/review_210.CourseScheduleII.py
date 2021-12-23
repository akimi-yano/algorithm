# 210. Course Schedule II
# Medium

# 5462

# 207

# Add to List

# Share
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
# Example 2:

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:

# Input: numCourses = 1, prerequisites = []
# Output: [0]
 

# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.


# This solution works:


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        all_courses = set([num for num in range(numCourses)])
        adj = {}
        reverse_adj = {}
        for later, first in prerequisites:
            
            if first not in adj:
                adj[first] = set([])
            adj[first].add(later)
            
            if later not in reverse_adj:
                reverse_adj[later] = set([])
            reverse_adj[later].add(first)
        
        can_take = []
        for course in all_courses:
            if course not in reverse_adj:
                can_take.append(course)
        path = []
        while can_take:
            course = can_take.pop()
            path.append(course)
            all_courses.remove(course)
            if course in adj:
                for next_course in adj[course]:
                    reverse_adj[next_course].remove(course)
                    if len(reverse_adj[next_course]) < 1:
                        del reverse_adj[next_course]
                        can_take.append(next_course)
                        
        if not all_courses:
            return path
        else:
            return []