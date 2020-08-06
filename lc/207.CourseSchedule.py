# 207. Course Schedule

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
 

# Constraints:

# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 1 <= numCourses <= 10^5

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        remaining = set([n for n in range(numCourses)])
        
        adj = {}
        rev = {}
        for t, f in prerequisites:
            if f not in adj:
                adj[f] = set([])
            if t not in rev:
                rev[t] = set([])
            adj[f].add(t)
            rev[t].add(f)
        # print(adj)
        # print(rev)
        
        can_take = []
        for course in remaining:
            if course not in rev:
                can_take.append(course)
        
        while len(can_take) > 0:
            course = can_take.pop()
            remaining.remove(course)
            if course in adj:
                next_courses = adj[course]
                for next_course in next_courses:
                    rev[next_course].remove(course)
                    if len(rev[next_course]) < 1:
                        can_take.append(next_course)
        return len(remaining) < 1