# 1041. Robot Bounded In Circle
# Medium

# 2263

# 539

# Add to List

# Share
# On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degrees to the right.
# The robot performs the instructions given in order, and repeats them forever.

# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

# Example 1:

# Input: instructions = "GGLLGG"
# Output: true
# Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
# When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
# Example 2:

# Input: instructions = "GG"
# Output: false
# Explanation: The robot moves north indefinitely.
# Example 3:

# Input: instructions = "GL"
# Output: true
# Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
 

# Constraints:

# 1 <= instructions.length <= 100
# instructions[i] is 'G', 'L' or, 'R'.


# This solution works:


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        '''
        conditions:
        1) ends with a direction that is not north after completing the instrucion
        because if we do the same instruction 4 times, we end up at the same place
        or 
        2) ends at a position (0,0)
        because it already ends at the same position it means, we did not move, so even if we repeat, we will end up at (0,0) again
        if either of them is true, we can draw a circle
        '''
        row, col = 0, 0
        directions = [(0,-1), (1,0), (0,1), (-1,0)]
        i = 0
        for instruction in instructions:
            if instruction == 'L':
                i += 1
            elif instruction == 'R':
                i -= 1
            else:
                r, c = directions[i%4]
                row += r
                col += c
        return (directions[i%4]!= directions[0]) or (row==0 and col == 0) 
        