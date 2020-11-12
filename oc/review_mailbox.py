'''
  Input: houses = [1,4,8,10,20], k = 3
  Output: 5
  Explanation: Allocate mailboxes in position 3, 9 and 20.
  Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + 

  |10-9| + |20-20| = 5 
'''

class Solution:
      def minDistance(self, houses: List[int], k: int) -> int:
          
          if not houses or k<1: return None
          
          size = len(houses)
          if k>= size: return 0
          houses = sorted(houses)
          
          distance = [[0 for _ in range(size)] for _ in range(size)]
          for row in range(size):
              for col in range(size):
                  median_index = (row+col)//2
                  for h in range(row, col+1):
                      distance[row][col] += abs(houses[h] - houses[median_index])
          
          dp = [[float('inf') for _ in range(k)] for _ in range(size)] 
          for i in range(size):
              dp[i][0] = distance[0][i]
          
          
          for i in range(size):
              for j in range(i):
                  for mb in range(1, k):
                      # dp[i][k] = dp[j][k-1] + distance[j+1][i]
                      dp[i][mb] = min(dp[i][mb], dp[j][mb-1] + distance[j+1][i])
                      
          return dp[-1][-1]
      
      #dp[i][k] = dp[-1][-1]


                




  # [1,4,8,10,20], k = 1


  # class Solution:
  #     def minDistance(self, houses: List[int], k: int) -> int:
          
          
  #         [2,3,5,12,18] k = 1
          
  #         1 2 3 50 100 k = 1
          
  #         30
  #         29 + 28 + 27 + 20 + 70 = 174
          
  #         3
  #         1+2+0+47+97 = 147
          
  #         50
  #         49+48+47+0+50 = 194
          
  #         odd num of items:
  #             H   H  H  H H
  #                    |
  #             2,3,5,12,18
  #                 |
                  
  #                 ->1
  #             +1+1+1 -1-1 = 1 > minimum distance
              
  #                <- 1
  #             -1-1+1+1+1 = 1 > minimum distance
              
                  
  #             1 2 3 50 100
  #                 |
  #                 * position for minimum distance
                  
                  
  #         even num of items:
              
  #             H H H H H H
  #                  |
  #                  * position for minimum distance between middle index
              
              
  #             iterate i
  #             iterate j
  #             itereate k 
  #             dp[i][k] = dp[j][]k-1 + cost[]j+1[i]      
              
              
  #             1, 4, 8
  #                |
                
  #      2nd dp table
  #     [1,4,8,10,20]
  # k=1  0 2 4 
  # k=2
  # k=3
      
      


