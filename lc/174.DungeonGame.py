# 174. Dungeon Game

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # this donest work 
        
        # # -10 + 4 = -6 (+1) - need 7
        # # - > abs+1
        # # + just abs
        # memo = {}
        # def helper(row,col):
        #     if (row,col) in memo:
        #         return memo[(row,col)]
        #     if row == len(dungeon)-1 and col == len(dungeon[0])-1:
        #         return dungeon[row][col]
        #     elif row<0 or col<0 or row>len(dungeon)-1 or col>len(dungeon[0])-1:
        #         return float('inf')
        #     # print(dungeon[row][col])

        #     min_path = float('inf')
        #     min_path = min(min_path,dungeon[row][col]+helper(row+1,col))
        #     min_path = min(min_path,dungeon[row][col]+helper(row,col+1))
        #     memo[(row,col)]=min_path
        #     print(min_path)
        #     return min_path
        # ans = helper(0,0)
        # return ans if ans >0 else abs(ans)+1
    
# this works
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon[0])
        need = [2**31] * (n-1) + [1]
        for row in dungeon[::-1]:
            for j in range(n)[::-1]:
                need[j] = max(min(need[j:j+2]) - row[j], 1)
        return need[0]
            
            
# think more about how I can solve it more intuitively 
# min and max
