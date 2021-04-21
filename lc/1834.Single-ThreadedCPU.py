# 1834. Single-Threaded CPU
# Medium

# 199

# 53

# Add to List

# Share
# You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.

# You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

# If the CPU is idle and there are no available tasks to process, the CPU remains idle.
# If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
# Once a task is started, the CPU will process the entire task without stopping.
# The CPU can finish a task then start a new one instantly.
# Return the order in which the CPU will process the tasks.

 

# Example 1:

# Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
# Output: [0,2,3,1]
# Explanation: The events go as follows: 
# - At time = 1, task 0 is available to process. Available tasks = {0}.
# - Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
# - At time = 2, task 1 is available to process. Available tasks = {1}.
# - At time = 3, task 2 is available to process. Available tasks = {1, 2}.
# - Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
# - At time = 4, task 3 is available to process. Available tasks = {1, 3}.
# - At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
# - At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
# - At time = 10, the CPU finishes task 1 and becomes idle.
# Example 2:

# Input: tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
# Output: [4,3,2,0,1]
# Explanation: The events go as follows:
# - At time = 7, all the tasks become available. Available tasks = {0,1,2,3,4}.
# - Also at time = 7, the idle CPU starts processing task 4. Available tasks = {0,1,2,3}.
# - At time = 9, the CPU finishes task 4 and starts processing task 3. Available tasks = {0,1,2}.
# - At time = 13, the CPU finishes task 3 and starts processing task 2. Available tasks = {0,1}.
# - At time = 18, the CPU finishes task 2 and starts processing task 0. Available tasks = {1}.
# - At time = 28, the CPU finishes task 0 and starts processing task 1. Available tasks = {}.
# - At time = 40, the CPU finishes task 1 and becomes idle.
 

# Constraints:

# tasks.length == n
# 1 <= n <= 105
# 1 <= enqueueTimei, processingTimei <= 109



# This approach does not work as by the time we pop from heap, all the valid candidates need to be in the heap (use while loop):

# import heapq
# class Solution:
#     def getOrder(self, tasks: List[List[int]]) -> List[int]:
#         tasks = [(enqueueTime, processingTime, i) for i,(enqueueTime,processingTime) in enumerate(tasks)]
#         tasks.sort()
#         minheap = []
#         ans = []
#         wait_time = 0
#         print(tasks)
#         for task in tasks:
#             enqueue_time, processing_time, i = task
#             heapq.heappush(minheap, (processing_time, i, enqueue_time))
#             if enqueue_time >= wait_time and minheap:
#                 new_processing_time, i, new_enqueue_time = heapq.heappop(minheap)
#                 wait_time = new_processing_time + new_enqueue_time
#                 ans.append(i)
            
#         while minheap:
#             _, i, _ = heapq.heappop(minheap)
#             ans.append(i)
        
#         return ans

# This approach does not work as by the time we pop from heap, all the valid candidates need to be in the heap (use while loop):

# import heapq
# class Solution:
#     def getOrder(self, tasks: List[List[int]]) -> List[int]:
#         tasks = [(enqueueTime, processingTime, i) for i,(enqueueTime,processingTime) in enumerate(tasks)]
#         tasks.sort()
#         minheap = []
#         ans = []
#         cur_time = 0
        
#         for task in tasks:
#             enqueue_time, processing_time, i = task
#             if not minheap and cur_time < enqueue_time:
#                 cur_time = enqueue_time
#             heapq.heappush(minheap, (processing_time, i, enqueue_time))
#             if enqueue_time >= cur_time and minheap:
#                 new_processing_time, i, new_enqueue_time = heapq.heappop(minheap)
#                 cur_time += new_processing_time
#                 ans.append(i)
            
#         while minheap:
#             _, i, _ = heapq.heappop(minheap)
#             ans.append(i)
        
#         return ans



# This solution works!!!:
'''
I should think how I would do this manually. Use while loop to put all the valid candidates into heap
'''

import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(enqueueTime, processingTime, i) for i,(enqueueTime,processingTime) in enumerate(tasks)]
        tasks.sort()
        tasks = deque(tasks)
        minheap = []
        ans = []
        cur_time = 0
        
        while minheap or tasks:
            if not minheap and tasks and tasks[0][0] > cur_time:
                cur_time = tasks[0][0]
            
            while tasks and tasks[0][0] <= cur_time:
                et, pt, i = tasks.popleft()
                heapq.heappush(minheap,(pt, i))
            
            new_pt, idx = heapq.heappop(minheap)
            ans.append(idx)
            cur_time += new_pt
        
        return ans