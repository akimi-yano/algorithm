# 1792. Maximum Average Pass Ratio
# Medium

# 52

# 27

# Add to List

# Share
# There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

# You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

# The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

# Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.

 

# Example 1:

# Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
# Output: 0.78333
# Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.
# Example 2:

# Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
# Output: 0.53485
 

# Constraints:

# 1 <= classes.length <= 105
# classes[i].length == 2
# 1 <= passi <= totali <= 105
# 1 <= extraStudents <= 105

# This solution works:


import heapq
class Solution:
    Diff = 10 ** (-5)
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        maxheap = []
        for prev_pass_n, prev_total_n in classes:
            prev_pass_ratio = prev_pass_n/prev_total_n
            new_pass_ratio = (prev_pass_n+1)/(prev_total_n+1)
            diff = new_pass_ratio - prev_pass_ratio
            heapq.heappush(maxheap, (-diff, prev_pass_n+1, prev_total_n+1))
            
        while extraStudents:
            diff, prev_pass_n, prev_total_n = heapq.heappop(maxheap)
            prev_pass_ratio = prev_pass_n/prev_total_n
            new_pass_ratio = (prev_pass_n+1)/(prev_total_n+1)
            new_diff = new_pass_ratio - prev_pass_ratio
            heapq.heappush(maxheap, (-new_diff, prev_pass_n+1, prev_total_n+1))
            extraStudents -= 1
        
        N = len(classes)
        total_passratio = 0
        while maxheap:
            _,  pass_n, total_n = heapq.heappop(maxheap)
            pass_ratio = (pass_n-1)/(total_n-1)
            total_passratio += pass_ratio
        
        return total_passratio/ N
        # 1/2, 3/5, 2/2
        # 0.5  0.6   1
        # 2/3
        # 0.6
        # 3/4or3/5 


# This approach does not work:

# import heapq
# class Solution:
#     Diff = 10 ** (-5)
#     def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
#         minheap = []
#         for pass_n, total_n in classes:
#             pass_ratio = pass_n/total_n
#             heapq.heappush(minheap, (pass_ratio, pass_n, total_n))
            
#         while extraStudents:
#             print(minheap)
#             pass_ratio, pass_n, total_n = heapq.heappop(minheap)
#             pass_n += 1
#             total_n += 1
#             pass_ratio = pass_n/total_n
#             heapq.heappush(minheap, (pass_ratio, pass_n, total_n))
#             extraStudents -= 1
        
#         N = len(classes)
#         total_passratio = 0
#         while minheap:
#             pass_ratio, _, _ = heapq.heappop(minheap)
#             total_passratio += pass_ratio
        
#         return total_passratio/ N
#         # 1/2, 3/5, 2/2
#         # 0.5  0.6   1
#         # 2/3
#         # 0.6
#         # 3/4or3/5 