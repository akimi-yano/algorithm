# 1345. Jump Game IV
# Hard

# 447

# 32

# Add to List

# Share
# Given an array of integers arr, you are initially positioned at the first index of the array.

# In one step you can jump from index i to index:

# i + 1 where: i + 1 < arr.length.
# i - 1 where: i - 1 >= 0.
# j where: arr[i] == arr[j] and i != j.
# Return the minimum number of steps to reach the last index of the array.

# Notice that you can not jump outside of the array at any time.

 

# Example 1:

# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
# Example 2:

# Input: arr = [7]
# Output: 0
# Explanation: Start index is the last index. You don't need to jump.
# Example 3:

# Input: arr = [7,6,9,6,9,6,9,7]
# Output: 1
# Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
# Example 4:

# Input: arr = [6,1,9]
# Output: 2
# Example 5:

# Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
# Output: 3
 

# Constraints:

# 1 <= arr.length <= 5 * 10^4
# -10^8 <= arr[i] <= 10^8


# This solution works !

from collections import deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        memo = {}
        for i in range(len(arr)):
            if arr[i] not in memo:
                memo[arr[i]] = []
            memo[arr[i]].append(i)
        
        # IMPORTANT - keep seen set so that you dont TLE
        seen = set([])
        queue = deque([(0, 0)])
        while queue:
            i, step = queue.popleft()
            if i == len(arr)-1:
                return step
            if i in seen:
                continue
            seen.add(i)
            if i != 0:
                queue.append((i-1, step+1))
            queue.append((i+1, step+1))
            if arr[i] in memo:
                for next_idx in memo[arr[i]]:
                    if next_idx != i:
                        queue.append((next_idx, step+1))
                # IMPORTANT - delete the key so that you dont TLE
                del memo[arr[i]]