# 605. Can Place Flowers

# Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

# Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
# Note:
# The input array won't violate no-adjacent-flowers rule.
# The input array size is in the range of [1, 20000].
# n is a non-negative integer which won't exceed the input array size.


# at frist i was thinking like this way but it didnt work (see below)

    # def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    #    can_plant = True
     #   left = 0 
      #  right = len(flowerbed)-1
       # while left<=right:
        #    if flowerbed[left] ==1:
         #       left+=1
          #  if flowerbed[right] == 1:
           #     right-=1
            #if flowerbed[left]== 0 and flowerbed[right] == 0:
             #   can_plant = True
              #  left+=1
               # right-=1
                #while can_plant:
                 #   if flowerbed[left]== 0 and flowerbed[right] == 0:
                  #      can_plant = False
                   # left+=1
                    #right-=1
    #    if n == 0:
     #       return True
      #  else:
       #     return False
        
# flowerbed = [1,0,0,0,1], n = 1
# count the number of 0 whose neighber is not 1
# and compare it with n if n is smaller than or equal to it, return True else False




# so since the approach above didnt work, I spent more time to think of a different solution 
# ans i came up with this solution - it works but it is slow !

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter = 0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                if i ==0:
                    if len(flowerbed)==1 or flowerbed[i+1]==0:
                        counter+=1
                        flowerbed[i]=1
                elif i == len(flowerbed)-1:
                    if flowerbed[i-1]==0:
                        counter+=1
                        flowerbed[i]=1
                else:
                    if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                        counter+=1
                        flowerbed[i]=1
        return counter>=n
                    
                    
                    
                    
                    
