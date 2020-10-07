# 933. Number of Recent Calls
# Easy

# 396

# 1919

# Add to List

# Share
# You have a RecentCounter class which counts the number of recent requests within a certain time frame.

# Implement the RecentCounter class:

# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.



# Example 1:

# Input
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# Output
# [null, 1, 2, 3, 3]

# Explanation
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
# recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3


# Constraints:

# 1 <= t <= 104
# Each test case will call ping with strictly increasing values of t.
# At most 104 calls will be made to ping.



# This solution works !!!
'''
Complexity: even though for each call of ping function we can potentially call a lot of popleft(), 
if we run ping n times we will have O(n) complexity: each element go to queue and from queue only once, 
so we can say amortised time complexity is O(1). Space complexity can be potentially O(3000).
'''

from collections import deque
class RecentCounter:

    def __init__(self):
        self.queue = deque([])

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[-1] - self.queue[0] > 3000:
            self.queue.popleft()
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)