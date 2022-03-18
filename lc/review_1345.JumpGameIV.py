# 1345. Jump Game IV
# Hard

# 960

# 54

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
# Explanation: Start index is the last index. You do not need to jump.
# Example 3:

# Input: arr = [7,6,9,6,9,6,9,7]
# Output: 1
# Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
 

# Constraints:

# 1 <= arr.length <= 5 * 104
# -108 <= arr[i] <= 108


# This solution works:


from collections import deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        queue = deque([])
        seen = set([])
        shortcuts = {}
        for i, val in enumerate(arr):
            if val not in shortcuts:
                shortcuts[val] = []
            shortcuts[val].append(i)
        
        queue.append((0, 0))
        while queue:
            i, step = queue.popleft()
            if i == len(arr)-1:
                return step
            seen.add(i)
            if i+1 < len(arr) and i+1 not in seen:
                queue.append((i+1, step+1))
            if i-1 >= 0 and i-1 not in seen:
                queue.append((i-1, step+1))
            if arr[i] in shortcuts:
                for nexti in reversed(shortcuts[arr[i]]):
                    if nexti != i and nexti not in seen:
                        queue.append((nexti, step+1))
                # since the same numbers are connected, you only need one - so delete after using it once
                del shortcuts[arr[i]]
                