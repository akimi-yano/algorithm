# 1306. Jump Game III
# Medium

# 816

# 29

# Add to List

# Share
# Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

# Notice that you can not jump outside of the array at any time.

 

# Example 1:

# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# Explanation: 
# All possible ways to reach at index 3 with value 0 are: 
# index 5 -> index 4 -> index 1 -> index 3 
# index 5 -> index 6 -> index 4 -> index 1 -> index 3 
# Example 2:

# Input: arr = [4,2,3,0,3,1,2], start = 0
# Output: true 
# Explanation: 
# One possible way to reach at index 3 with value 0 is: 
# index 0 -> index 4 -> index 1 -> index 3
# Example 3:

# Input: arr = [3,0,2,1,2], start = 2
# Output: false
# Explanation: There is no way to reach at index 1 with value 0.
 

# Constraints:

# 1 <= arr.length <= 5 * 10^4
# 0 <= arr[i] < arr.length
# 0 <= start < arr.length



# This solution works !

# This is in fact graph traversal problem: given start position and moving rules, 
# we need to check if we can reach node with value 0. There are as usual 3 classical approaches how you can do it:

# bfs, using queue
# dfs, using stack
# dfs, using recursion

from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        seen = set([])
        
        while queue:
            idx = queue.popleft()
            if arr[idx] == 0:
                return True
            if idx in seen:
                continue
            seen.add(idx)
            moveup = idx + arr[idx]
            movedown = idx - arr[idx]
            if 0 <= moveup <= len(arr)-1:
                queue.append(moveup)
            if 0 <= movedown <= len(arr)-1:
                queue.append(movedown)
                
        return False
        