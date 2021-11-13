# 739. Daily Temperatures
# Medium

# 5516

# 143

# Add to List

# Share
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100


# This solution works:


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        [73,74,75,71,69,72,76,73]
         0  1  2  3  4  5  6  7
        arr = [(73,7), (76,6), //(72,5)//, //(69,4)//, //(71,3)//] - append always (peak to compare - if the peaked elem is emaller, pop to see the next one -> empty means 0)
        ans = [0, 0, 1, 1, 4]
        expected: [1,1,4,2,1,1,0,0]
        
        [89,62,70,58,47,47,46,76,100,70]
         0  1. 2. 3. 4. 5. 6. 7. 8.  9

        [8,1,5,4,3,2,1,1,0,0]
        
        arr = [(70,9),(100,8),(76,7),//(46,6)//, (47,5)]
        ans = [0, 0, 1, 1, 2]
        '''
        ans = []
        arr = []
        for i in range(len(temperatures)-1,-1,-1):

            while arr:
                if arr[-1][0] <= temperatures[i]:
                    arr.pop()
                else:
                    ans.append(arr[-1][1]-i)
                    break
            if not arr:
                ans.append(0)    
            arr.append((temperatures[i], i))
        ans.reverse()
        return ans