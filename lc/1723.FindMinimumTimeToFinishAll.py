# 1723. Find Minimum Time to Finish All Jobs
# Hard

# 45

# 4

# Add to List

# Share
# You are given an integer array jobs, where jobs[i] is the amount of time it takes to complete the ith job.

# There are k workers that you can assign jobs to. Each job should be assigned to exactly one worker. The working time of a worker is the sum of the time it takes to complete all jobs assigned to them. Your goal is to devise an optimal assignment such that the maximum working time of any worker is minimized.

# Return the minimum possible maximum working time of any assignment.

 

# Example 1:

# Input: jobs = [3,2,3], k = 3
# Output: 3
# Explanation: By assigning each person one job, the maximum time is 3.
# Example 2:

# Input: jobs = [1,2,4,7,8], k = 2
# Output: 11
# Explanation: Assign the jobs the following way:
# Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
# Worker 2: 4, 7 (working time = 4 + 7 = 11)
# The maximum working time is 11.
 

# Constraints:

# 1 <= k <= jobs.length <= 12
# 1 <= jobs[i] <= 107


# This solution works - binary search + recursion + lru cache with tuple + sort (reverse = True)

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        left, right = max(jobs), sum(jobs)
        
        jobs.sort(reverse=True)
        self.jobs = jobs
        self.k = k

        while left < right:
            mid = (left+right) // 2
            if self.valid(mid):
                right = mid
            else:
                left = mid + 1
        return left
    
    def valid(self, limit):
        workers = [0] * self.k
        workers[0] = self.jobs[0]
        return self.helper(limit, tuple(workers), 1)
    
    @lru_cache(None)
    def helper(self, limit, workers, job_idx):
        if job_idx >= len(self.jobs):
            return True

        workers = list(workers)
        cur_job = self.jobs[job_idx]
        for i in range(len(workers)):
            if workers[i] + cur_job <= limit:
                workers[i] += cur_job
                if self.helper(limit, tuple(sorted(workers, reverse=True)), job_idx+1):
                    return True
                workers[i] -= cur_job
        return False
                