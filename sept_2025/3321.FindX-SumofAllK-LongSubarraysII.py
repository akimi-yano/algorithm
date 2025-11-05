'''
3321. Find X-Sum of All K-Long Subarrays II
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given an array nums of n integers and two integers k and x.

The x-sum of an array is calculated by the following procedure:

Count the occurrences of all elements in the array.
Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
Calculate the sum of the resulting array.
Note that if an array has less than x distinct elements, its x-sum is the sum of the array.

Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].

 

Example 1:

Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2

Output: [6,10,12]

Explanation:

For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence, answer[0] = 1 + 1 + 2 + 2.
For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence, answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence, answer[2] = 2 + 2 + 2 + 3 + 3.
Example 2:

Input: nums = [3,8,7,8,7,5], k = 2, x = 2

Output: [11,15,15,15,12]

Explanation:

Since k == x, answer[i] is equal to the sum of the subarray nums[i..i + k - 1].

 

Constraints:

nums.length == n
1 <= n <= 105
1 <= nums[i] <= 109
1 <= x <= k <= nums.length
'''

from sortedcontainers import SortedList
from collections import defaultdict

class Solution:
    def findXSum(self, nums, k, x):
        n = len(nums)
        freq = defaultdict(int)
        ans = []

        # Step 1: Initialize structures
        def key(val):
            return (freq[val], val)

        topX = SortedList(key=key)
        rest = SortedList(key=key)
        sumTop = 0

        # Step 2: Ordering / comparator defined via key above

        def rebalance():
            nonlocal sumTop
            # Step 4
            while len(topX) < min(x, len(freq)) and rest:
                best = rest.pop(-1)
                topX.add(best)
                sumTop += freq[best] * best
            while len(topX) > x:
                worst = topX.pop(0)
                sumTop -= freq[worst] * worst
                rest.add(worst)
            while topX and rest:
                worstTop = topX[0]
                bestRest = rest[-1]
                if (freq[bestRest] > freq[worstTop] or
                   (freq[bestRest] == freq[worstTop] and bestRest > worstTop)):
                    topX.remove(worstTop)
                    rest.remove(bestRest)
                    topX.add(bestRest)
                    rest.add(worstTop)
                    sumTop += freq[bestRest] * bestRest - freq[worstTop] * worstTop
                else:
                    break

        # Step 3, 5, 6 and Step 7: Main sliding-window loop
        for i, v in enumerate(nums):
            # Remove-before-update for incoming
            if freq[v] > 0:
                if v in topX:
                    topX.remove(v)
                    sumTop -= freq[v] * v
                else:
                    rest.remove(v)
            # Update freq and insert
            freq[v] += 1
            rest.add(v)
            rebalance()

            if i >= k:
                u = nums[i - k]
                # Remove outgoing
                if u in topX:
                    topX.remove(u)
                    sumTop -= freq[u] * u
                else:
                    rest.remove(u)
                if freq[u] == 1:
                    del freq[u]
                else:
                    freq[u] -= 1
                    rest.add(u)
                rebalance()

            if i >= k - 1:
                ans.append(sumTop)

        # Step 9: Return result
        return ans