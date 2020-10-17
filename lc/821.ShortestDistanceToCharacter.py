# 821. Shortest Distance to a Character
# Easy

# 1173

# 79

# Add to List

# Share
# Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

# Example 1:

# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


# Note:

# S string length is in [1, 10000].
# C is a single character, and guaranteed to be in string S.
# All letters in S and C are lowercase.


# This solution works !:

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        arr = [float('inf') for _ in range(len(S))]
        for i, elem in enumerate(S):
            if elem == C:
                arr[i] = 0
                
                left = i -1
                right = i +1 
                cur = 1
                while left >= 0 and right <= len(arr)-1:
                    arr[left] = min(arr[left], cur)
                    arr[right] = min(arr[right], cur)
                    left -= 1
                    right += 1
                    cur += 1
                    
                while left >=0:
                    arr[left] = min(arr[left], cur)
                    left -= 1
                    cur += 1
                
                while right <= len(arr)-1:
                    arr[right] = min(arr[right], cur)
                    right += 1
                    cur += 1
        return arr 
                    
                    
# This solution works !!! faster !!!

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        arr = [float('inf') for _ in range(len(S))]

        cur = float('inf') 
        for i, elem in enumerate(S):
            if elem == C:
                cur = 0
            arr[i] = cur
            cur += 1
        
        cur = float('inf') 
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == 0:
                cur = 1
            else:
                arr[i] = min(cur, arr[i])
                cur += 1
                
        return arr 
                    
