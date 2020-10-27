# 799. Champagne Tower
# Medium

# 604

# 44

# Add to List

# Share
# We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.

# Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)

# For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.



# Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is (both i and j are 0-indexed.)



# Example 1:

# Input: poured = 1, query_row = 1, query_glass = 1
# Output: 0.00000
# Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.
# Example 2:

# Input: poured = 2, query_row = 1, query_glass = 1
# Output: 0.50000
# Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.
# Example 3:

# Input: poured = 100000009, query_row = 33, query_glass = 17
# Output: 1.00000


# Constraints:

# 0 <= poured <= 109
# 0 <= query_glass <= query_row < 100



# This solution works but it is not the optimal 

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
            
        glasses = [[0 for i in range(k+1)] for k in range(0, 101)]
        glasses[0][0] += poured
        
        each = 0 
        for row in range(100):
            for col in range(len(glasses[row])):
                if row == 99 and col == 99 and glasses[row][col] > 1:
                    glasses[row][col] = 1
                    break
                if glasses[row][col] > 1:
                    carryover = glasses[row][col] - 1
                    each = carryover/2
                    glasses[row+1][col] += each
                    glasses[row+1][col+1] += each
                    glasses[row][col] = 1
                
                
        return glasses[query_row][query_glass]



# This solution works ! 

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        '''
        input : row, col poured
        output: the status at [row][col]
        to get this [row][col] we look at upper left + upper right (and add them)
        upper left: [row-1][col-1]
        upper right: [row-1][col]
        the helper if going take each row and col of the upper ones and maybe poured (?)
        this helper returns --- how many carryover from each uppers
        answer is the answer between 0< real <1
        '''
        self.P = poured
        self.memo = {}
        if query_row == 0 and query_glass == 0:
            return poured >= 1 
        return min(1, self.helper(query_row-1, query_glass-1)/2 + self.helper(query_row-1, query_glass)/2)
    
    
    def helper(self, row, col):
        if (row, col) in self.memo:
            return self.memo[(row, col)]
        if row == 0 and col == 0:
            self.memo[(row, col)] = max(0, self.P -1) 
            return max(0, self.P -1) 
        elif col < 0 or row < 0 or row+1 <= col:  
            self.memo[(row, col)] = 0
            return 0
        ans = max(0, (self.helper(row-1, col-1)/2 + self.helper(row-1, col)/2) -1 ) 
        self.memo[(row, col)] = ans
        return ans
    
    
# Optimization - reduced memo assignment and return statement by using if-elif-else condition

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        '''
        input : row, col poured
        output: the status at [row][col]
        to get this [row][col] we look at upper left + upper right (and add them)
        upper left: [row-1][col-1]
        upper right: [row-1][col]
        the helper if going take each row and col of the upper ones and maybe poured (?)
        this helper returns --- how many carryover from each uppers
        answer is the answer between 0< real <1
        '''
        self.P = poured
        self.memo = {}
        if query_row == 0 and query_glass == 0:
            return poured >= 1 
        return min(1, self.helper(query_row-1, query_glass-1)/2 + self.helper(query_row-1, query_glass)/2)
    
    
    def helper(self, row, col):
        key = (row, col)
        if key in self.memo:
            return self.memo[key]
        
        ans = 0
        
        if col < 0 or row < 0 or row+1 <= col:  
            pass
        elif row == 0 and col == 0:
            ans = max(0, self.P -1) 
        else:
            ans = max(0, (self.helper(row-1, col-1)/2 + self.helper(row-1, col)/2) -1 ) 
            
        self.memo[key] = ans
        return ans
    
    
