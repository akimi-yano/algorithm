# 621. Task Scheduler

# You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task. Tasks could be done without the original order of the array. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

# You need to return the least number of units of times that the CPU will take to finish all the given tasks.

 

# Example 1:

# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: 
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.
# Example 2:

# Input: tasks = ["A","A","A","B","B","B"], n = 0
# Output: 6
# Explanation: On this case any permutation of size 6 would work since n = 0.
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# And so on.
# Example 3:

# Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# Output: 16
# Explanation: 
# One possible solution is
# A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
 

# Constraints:

# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].





# this solution does not work - see below for the solution that works 

# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:

#         memo = {}
#         for task in tasks:
#             if task not in memo:
#                 memo[task]=1
#             else:
#                 memo[task]+=1
       
#         count = 0
#         while memo:
#             while n:
#                 nprev = None
#                 for k,v in memo.items():
#                     v-=1
#                     if v<1:
#                         del memo[k]
#                     n-=1
#                     count+=1
                        
#                 if n:
#                     count+=1
#                     n-=1
#         return count


# this solution works 

import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        memo = {}
        for task in tasks:
            if task not in memo:
                memo[task]=1
            else:
                memo[task]+=1

        count = 0
        ready_tasks = []
        for task in memo:
            heapq.heappush(ready_tasks, (-memo[task], task))
        waiting_tasks = []
        while len(waiting_tasks) > 0 or len(ready_tasks) > 0:
            # If there is something ready, process it
            if len(ready_tasks) > 0:
                tasks_left, task = heapq.heappop(ready_tasks)
                tasks_left += 1
                # print("[{}]: Processed task {}, {} left to do".format(count, task, -tasks_left))
                if tasks_left < 0:
                    heapq.heappush(waiting_tasks, (count+n, tasks_left, task))
            # else, Idle
            # else:
                # print("[{}]: IDLE".format(count))
            self.update_tasks(count, ready_tasks, waiting_tasks)
            count += 1
        return count
    
    def update_tasks(self, count, ready_tasks, waiting_tasks):
        while len(waiting_tasks) > 0 and waiting_tasks[0][0] <= count:
            _, tasks_left, task = heapq.heappop(waiting_tasks)
            # print("        [{}]: task {} is ready, moving to ready_task".format(count, task))
            heapq.heappush(ready_tasks, (tasks_left, task))