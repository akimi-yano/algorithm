# 1007. Minimum Domino Rotations For Equal Row
# Medium

# 997

# 178

# Add to List

# Share
# In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

# We may rotate the ith domino, so that A[i] and B[i] swap values.

# Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

# If it cannot be done, return -1.

 

# Example 1:


# Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
# Output: 2
# Explanation: 
# The first figure represents the dominoes as given by A and B: before we do any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
# Example 2:

# Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
# Output: -1
# Explanation: 
# In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

# Constraints:

# 2 <= A.length == B.length <= 2 * 104
# 1 <= A[i], B[i] <= 6

# This solution works - before modularization

from collections import Counter
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        a_counter = Counter(A)
        b_counter = Counter(B)
        
        if len(a_counter) == 1 or len(b_counter) == 1:
            return 0
        
        num1 = A[0]
        num2 = B[0]
        
        min_change = float('inf')
        
        valid = True
        change = 0
        for i in range(1, len(A)):
            if A[i] != num1:
                if B[i] == num1:
                    change += 1
                else:
                    valid = False
                    break

        if change and valid:
            min_change = min(min_change, change)
            
        valid = True
        change = 1
        for i in range(1, len(A)):
            if A[i] != num2:
                if B[i] == num2:
                    change += 1
                else:
                    valid = False
                    break

        if change and valid:
            min_change = min(min_change, change)    
        
        
        valid = True
        change = 0
        for i in range(1, len(B)):
            if B[i] != num2:
                if A[i] == num2:
                    change += 1
                else:
                    valid = False
                    break
 
        if change and valid:
            min_change = min(min_change, change)
            
        valid = True
        change = 1
        for i in range(1, len(B)):
            if B[i] != num1:
                if A[i] == num1:
                    change += 1
                else:
                    valid = False
                    break
  
        if change and valid:
            min_change = min(min_change, change)
            
        return min_change if min_change != float('inf') else -1
    
    
# This solution works - after modularization 

from collections import Counter
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # edge case: A or B is already complete
        if len(Counter(A)) == 1 or len(Counter(B)) == 1:
            return 0
        
        # there are only 2 options for the numbers to be matched
        num1 = A[0]
        num2 = B[0]
        
        self.min_change = float('inf')
        self.update_min_change(num1, A, B, 0, True)
        self.update_min_change(num2, A, B, 1, True)
        self.update_min_change(num2, B, A, 0, True)
        self.update_min_change(num1, B, A, 1, True)
        
        return self.min_change if self.min_change != float('inf') else -1
    
    # this method updates the min_change
    def update_min_change(self, target, arr1, arr2, change, valid):

        for i in range(1, len(arr1)):
            if arr1[i] != target:
                if arr2[i] == target:
                    change += 1
                else:
                    valid = False
                    break
        
        if change and valid:
            self.min_change = min(self.min_change, change)
        
        
'''
possibilities are limited:

- as for the first elem in arrays,
    A) use the first elem from array 1 -> all elements of array 1 or array 2 need to become this element
    B) use the first elem from array 2 -> all elements of array 1 or array 2 need to become this element
    C) return -1 because we cannot do none of the 4 options above
    

'''