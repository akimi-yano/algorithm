# 1776. Car Fleet II
# Hard

# 49

# 2

# Add to List

# Share
# There are n cars traveling at different speeds in the same direction along a one-lane road. You are given an array cars of length n, where cars[i] = [positioni, speedi] represents:

# positioni is the distance between the ith car and the beginning of the road in meters. It is guaranteed that positioni < positioni+1.
# speedi is the initial speed of the ith car in meters per second.
# For simplicity, cars can be considered as points moving along the number line. Two cars collide when they occupy the same position. Once a car collides with another car, they unite and form a single car fleet. The cars in the formed fleet will have the same position and the same speed, which is the initial speed of the slowest car in the fleet.

# Return an array answer, where answer[i] is the time, in seconds, at which the ith car collides with the next car, or -1 if the car does not collide with the next car. Answers within 10-5 of the actual answers are accepted.

 

# Example 1:

# Input: cars = [[1,2],[2,1],[4,3],[7,2]]
# Output: [1.00000,-1.00000,3.00000,-1.00000]
# Explanation: After exactly one second, the first car will collide with the second car, and form a car fleet with speed 1 m/s. After exactly 3 seconds, the third car will collide with the fourth car, and form a car fleet with speed 2 m/s.
# Example 2:

# Input: cars = [[3,4],[5,4],[6,3],[9,1]]
# Output: [2.00000,1.00000,1.50000,-1.00000]
 

# Constraints:

# 1 <= cars.length <= 105
# 1 <= positioni, speedi <= 106
# positioni < positioni+1

# This solution works:

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        '''
        key insight:
        if the one on your right is smaller in speed, you will catch up so will collide but need to also check the colliding time
        if the colliding time is larger, the colliding is not prioritized
        need to keep track of these two things
        
        we need to check from behind because collision can be checked from behind
        
        iterate through the array from behind and do like monoq/ stack 
        by popping if its too small (speed) or too big (colliding time)
        '''
        # set the default ans to be -1
        ans = [-1 for _ in range(len(cars))]
        stack = []
        for i in range(len(cars)-1, -1, -1):
            cur_pos, cur_speed = cars[i]
            
            # we check from back and if the current speed is slower than or equal to the previous speed in the stack, we can pop
            # also we can pop if the current one's colliding time is larger than or equal to the previous ones
            # it means the previous collidion happens before this current one
            while stack and (cur_speed <= stack[-1][2] or (stack[-1][1]-cur_pos)/(cur_speed-stack[-1][2]) >= stack[-1][0]):
                stack.pop()
            if not stack:
                stack.append((float('inf'), cur_pos, cur_speed))
            else:
                colliding_time = (stack[-1][1]-cur_pos)/(cur_speed-stack[-1][2])
                stack.append((colliding_time, cur_pos, cur_speed))
                # only update the ans array if its stack is non empty
                ans[i] = colliding_time
            
        return ans
                
