# 1589. Maximum Sum Obtained of Any Permutation
# Medium

# 40

# 10

# Add to List

# Share
# We have an array of integers, nums, and an array of requests where requests[i] = [starti, endi]. The ith request asks for the sum of nums[starti] + nums[starti + 1] + ... + nums[endi - 1] + nums[endi]. Both starti and endi are 0-indexed.

# Return the maximum total sum of all requests among all permutations of nums.

# Since the answer may be too large, return it modulo 109 + 7.

 

# Example 1:

# Input: nums = [1,2,3,4,5], requests = [[1,3],[0,1]]
# Output: 19
# Explanation: One permutation of nums is [2,1,3,4,5] with the following result: 
# requests[0] -> nums[1] + nums[2] + nums[3] = 1 + 3 + 4 = 8
# requests[1] -> nums[0] + nums[1] = 2 + 1 = 3
# Total sum: 8 + 3 = 11.
# A permutation with a higher total sum is [3,5,4,2,1] with the following result:
# requests[0] -> nums[1] + nums[2] + nums[3] = 5 + 4 + 2 = 11
# requests[1] -> nums[0] + nums[1] = 3 + 5  = 8
# Total sum: 11 + 8 = 19, which is the best that you can do.
# Example 2:

# Input: nums = [1,2,3,4,5,6], requests = [[0,1]]
# Output: 11
# Explanation: A permutation with the max total sum is [6,5,4,3,2,1] with request sums [11].
# Example 3:

# Input: nums = [1,2,3,4,5,10], requests = [[0,2],[1,3],[1,1]]
# Output: 47
# Explanation: A permutation with the max total sum is [4,10,5,3,2,1] with request sums [19,18,10].
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 0 <= nums[i] <= 105
# 1 <= requests.length <= 105
# requests[i].length == 2
# 0 <= starti <= endi < n



# This solution does not work :

# import heapq
# class Solution:
#     mod = 10 ** 9 + 7 
#     def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
#         '''
#         iterate throught request arr to get num of requests
#         from the largest number you use from nums
#         '''
        
# #         maxheap = []
# #         for num in nums:
# #             heapq.heappush(maxheap,num*(-1))
#         count = {}
#         for start, end in requests:
#             for k in range(start,end+1):
#                 if k not in count:
#                     count[k] = 1
#                 else:
#                     count[k] += 1
#         # print(count)
#         ans = 0
#         sorted_nums = sorted(nums)
#         numcount = sorted(list(count.values()))
#         # print(numcount)
#         # while maxheap and numcount:
#         #     times = numcount.pop()
#         #     popped = heapq.heappop(maxheap)
#         #     popped*=(-1)
#         #     ans = (ans + (popped* times)) % Solution.mod
#         while sorted_nums and numcount:
#             times = numcount.pop()
#             val = sorted_nums.pop()
#             ans = (ans + (val* times)) % Solution.mod
            
#         return ans % Solution.mod


# This solution works !
# Instead of making counter dictionary with 2 nested loops, prepopulate an array with index using start arr and end arr :

'''
Sweep Line:

1 calculate the frequency for intervals
2 assign large num to most frequent one
'''

from collections import deque

class Solution:
    mod = 10 ** 9 + 7

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        starts = [req[0] for req in requests]
        ends = [req[1] for req in requests]
        starts.sort()
        ends.sort()
        starts = deque(starts)
        ends = deque(ends)
        
        results = []
        count = 0

        for _ in range(len(requests) * 2):
            if len(starts) > 0 and starts[0] <= ends[0]:
                start = starts.popleft()
                
                while len(results) < start:
                    results.append(count)
                count += 1
                # print('[count={}] start: {}'.format(count, start))
            else:
                end = ends.popleft()

                while len(results) < end+1:
                    results.append(count)

                count -= 1
                # print('[count={}] end: {}'.format(count, end))
        # print(results)
        results.sort()
        nums.sort()
        ans = 0
        while results and nums:
            times = results.pop()
            val = nums.pop()
            ans += val*times
        return ans % Solution.mod
    
'''
Sweep Line Algorithm 

Intuition: 
calculate the frequency for intervals


Explanation:
For each request [start,end],
we set count[start] +1 and count[end] -1,

Then we sweep once the whole count,
we can find the frequency for count[i].


Other problems
1109. Corporate Flight Bookings
253. Meeting Rooms II

'''
def maxSumRangeQuery(self, A, req):
    n = len(A)
    count = [0] * (n + 1)
    for i, j in req:
        count[i] += 1
        count[j + 1] -= 1
    for i in xrange(1, n + 1):
        count[i] += count[i - 1]
    res = 0
    for v, c in zip(sorted(count[:-1]), sorted(A)):
        res += v * c
    return res % (10**9 + 7)



# THIS SOLUTION WORKS !!! Rewrote the code  using  swipe line !

class Solution:
    mod = 10 ** 9 + 7

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # prepopulate the counts arr with an extra slots 
        # add 1 for start and subtract 1 for end +1
        counts = [0 for _ in range(len(nums)+1)] 
        for start, end in requests:
            counts[start] +=1
            counts[end+1] -=1
        # print(counts)
        # update the counts arr with the accumulated val 
        num = 0
        for i, elem in enumerate(counts):
            num += elem
            counts[i] = num
        # print(counts)
        # sort both so that largest vals comes at the end
        nums.sort()
        counts.sort()
        ans = 0
        while counts and nums:
            ans += counts.pop() * nums.pop()
        
        return ans % Solution.mod