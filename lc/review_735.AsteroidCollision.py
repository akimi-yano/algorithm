# 735. Asteroid Collision
# Medium

# 1422

# 135

# Add to List

# Share
# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
# Example 2:

# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# Example 3:

# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
# Example 4:

# Input: asteroids = [-2,-1,1,2]
# Output: [-2,-1,1,2]
# Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving right. Asteroids moving the same direction never meet, so no asteroids will meet each other.
 

# Constraints:

# 1 <= asteroids <= 104
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        else statement after while loop is only triggered once the while condition becomes False
        and not when it breaks out of while loop due to break
        we only append the num when num's absolute value is larger than that of the last elem of the 
        stack. otherwise it keeps poping and append at the end
        '''
        stack = []
        for num in asteroids:
            # num will be appended if it does not hit the break condition before the while 
            # condition becomes False
            while stack and stack[-1] > 0 and num < 0:
                if abs(stack[-1]) < abs(num):
                    stack.pop()
                # don't remove but don't append either: break so that we don't append num at the end
                elif abs(stack[-1]) > abs(num):
                    break
                # tie - remove both: break so that we don't append num at the end
                else:
                    stack.pop()
                    break
            else:
                stack.append(num)
        return stack