# 1041. Robot Bounded In Circle
# Medium

# 477

# 159

# Add to List

# Share
# On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degress to the right.
# The robot performs the instructions given in order, and repeats them forever.

# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

# Example 1:

# Input: "GGLLGG"
# Output: true
# Explanation: 
# The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
# When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
# Example 2:

# Input: "GG"
# Output: false
# Explanation: 
# The robot moves north indefinitely.
# Example 3:

# Input: "GL"
# Output: true
# Explanation: 
# The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
 

# Note:

# 1 <= instructions.length <= 100
# instructions[i] is in {'G', 'L', 'R'}


# THIS SOLUTION WORKS !!!
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        row = col = 0
        i = 0
        directions = ((-1,0),(0,1),(1,0),(0,-1))
        '''
        R -1,0 -> 0,1 -> 1,0 -> 0,-1
        L -1,0 -> 0,-1 -> 1,0 -> 0,1
        '''
        for elem in instructions:
            if elem == 'L':
                i-=1
            elif elem == 'R':
                i+=1
            else:
                r,c = directions[i%4]
                row += r
                col += c
        # Need both conditions ! if it returns back to the starting position after the loop ends then there is cycle
        # Even if it does not go back to the original position, if it is not the same direction then one day goes back to the
        # original position at some point 
        return row == 0 and col == 0 or directions[i%4] != directions[0]
    

    