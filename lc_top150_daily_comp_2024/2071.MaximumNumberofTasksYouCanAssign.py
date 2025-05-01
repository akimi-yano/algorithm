'''
2071. Maximum Number of Tasks You Can Assign
Hard
Topics
Companies
Hint
You have n tasks and m workers. Each task has a strength requirement stored in a 0-indexed integer array tasks, with the ith task requiring tasks[i] strength to complete. The strength of each worker is stored in a 0-indexed integer array workers, with the jth worker having workers[j] strength. Each worker can only be assigned to a single task and must have a strength greater than or equal to the task's strength requirement (i.e., workers[j] >= tasks[i]).

Additionally, you have pills magical pills that will increase a worker's strength by strength. You can decide which workers receive the magical pills, however, you may only give each worker at most one magical pill.

Given the 0-indexed integer arrays tasks and workers and the integers pills and strength, return the maximum number of tasks that can be completed.

 

Example 1:

Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
Output: 3
Explanation:
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 2 (0 + 1 >= 1)
- Assign worker 1 to task 1 (3 >= 2)
- Assign worker 2 to task 0 (3 >= 3)
Example 2:

Input: tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
Output: 1
Explanation:
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 0 (0 + 5 >= 5)
Example 3:

Input: tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
Output: 2
Explanation:
We can assign the magical pills and tasks as follows:
- Give the magical pill to worker 0 and worker 1.
- Assign worker 0 to task 0 (0 + 10 >= 10)
- Assign worker 1 to task 1 (10 + 10 >= 15)
The last pill is not given because it will not make any worker strong enough for the last task.
 

Constraints:

n == tasks.length
m == workers.length
1 <= n, m <= 5 * 104
0 <= pills <= m
0 <= tasks[i], workers[j], strength <= 109
'''

from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks = sorted(tasks)
        workers = sorted(workers)

        def check(k):
            W = SortedList(workers[-k:])
            tries = pills

            for elem in tasks[:k][::-1]:
                place = W.bisect_left(elem)
                if place < len(W):
                    W.pop(place)
                elif tries > 0:
                    place2 = W.bisect_left(elem - strength)
                    if place2 < len(W):
                        W.pop(place2)
                        tries -= 1
                else:
                    return False

            return len(W) == 0

        beg, end = 0, min(len(workers), len(tasks)) + 1
        while beg + 1 < end:
            mid = (beg + end)//2
            if check(mid):
                beg = mid
            else:
                end = mid

        return beg