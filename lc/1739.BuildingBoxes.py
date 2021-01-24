# 1739. Building Boxes
# Hard

# 61

# 6

# Add to List

# Share
# You have a cubic storeroom where the width, length, and height of the room are all equal to n units. You are asked to place n boxes in this room where each box is a cube of unit side length. There are however some rules to placing the boxes:

# You can place the boxes anywhere on the floor.
# If box x is placed on top of the box y, then each side of the four vertical sides of the box y must either be adjacent to another box or to a wall.
# Given an integer n, return the minimum possible number of boxes touching the floor.

 

# Example 1:



# Input: n = 3
# Output: 3
# Explanation: The figure above is for the placement of the three boxes.
# These boxes are placed in the corner of the room, where the corner is on the left side.
# Example 2:



# Input: n = 4
# Output: 3
# Explanation: The figure above is for the placement of the four boxes.
# These boxes are placed in the corner of the room, where the corner is on the left side.
# Example 3:



# Input: n = 10
# Output: 6
# Explanation: The figure above is for the placement of the ten boxes.
# These boxes are placed in the corner of the room, where the corner is on the back side.
 

# Constraints:

# 1 <= n <= 109

# This solution works:
class Solution:
    def minimumBoxes(self, n: int) -> int:
        '''
        there is a pattern
        every time you put 1 block on the floor and you have +1 (every time) you can add in the air
        which increases
        '''
        cur_boxes = 0
        cur_floors = 0
        cur_limit = 1

        while True:
            # print("Adding up to " + str(cur_limit))
            for add_boxes in range(1, cur_limit+1):
                # print("  adding " + str(add_boxes))
                if cur_boxes >= n:
                    return cur_floors
                cur_boxes += add_boxes
                cur_floors += 1
            cur_limit += 1