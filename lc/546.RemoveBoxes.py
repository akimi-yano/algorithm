# 546. Remove Boxes
# Hard

# 1169

# 74

# Add to List

# Share
# You are given several boxes with different colors represented by different positive numbers.

# You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (i.e., composed of k boxes, k >= 1), remove them and get k * k points.

# Return the maximum points you can get.

 

# Example 1:

# Input: boxes = [1,3,2,2,2,3,4,3,1]
# Output: 23
# Explanation:
# [1, 3, 2, 2, 2, 3, 4, 3, 1] 
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
# ----> [1, 3, 3, 3, 1] (1*1=1 points) 
# ----> [1, 1] (3*3=9 points) 
# ----> [] (2*2=4 points)
# Example 2:

# Input: boxes = [1,1,1]
# Output: 9
# Example 3:

# Input: boxes = [1]
# Output: 1
 

# Constraints:

# 1 <= boxes.length <= 100
# 1 <= boxes[i] <= 100


# This solution works:


class Solution:
    def removeBoxes(self, B):
        '''
        We need to consider states dp(i, j, k) is answer for the following problem: 
        given substring B[i:j+1] and we added k symbols B[i] before the start. 
        Taking into account all what we have before we can have two options:

        Interval which is covering element B[i] has length 1, then we have (k+1)**2 + dp(i+1, j, 0).
        Interval has length more than one, then we can say that problem for interval i+1, 
        m-1 is independent and we can split our problem into two subproblems again: 
        look at 1--------1112231 case once again.
        '''
        
        @lru_cache(None)
        def dp(i, j, k):
            if i > j: return 0
            indx = [m for m in range(i+1, j+1) if B[m] == B[i]]
            ans = (k+1)**2 + dp(i+1, j, 0)
            return max([ans] + [dp(i+1, m-1, 0) + dp(m, j, k+1) for m in indx])   
            
        return dp(0, len(B)-1, 0)