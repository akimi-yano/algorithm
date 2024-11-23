'''
1861. Rotating the Box
Solved
Medium
Topics
Companies
Hint
You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

 

Example 1:



Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]
Example 2:



Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]
Example 3:



Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
 

Constraints:

m == box.length
n == box[i].length
1 <= m, n <= 500
box[i][j] is either '#', '*', or '.'.
'''

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        ROW = len(box)
        COL = len(box[0])

        for row in range(ROW):
            insert_idx = COL-1
            for col in range(COL-1, -1, -1):
                if box[row][col] == '#':
                    box[row][insert_idx] = '#'
                    insert_idx -= 1
                elif box[row][col] == '*':
                    for empty in range(col+1, insert_idx+1):
                        box[row][empty] = '.'
                    insert_idx = col - 1
            for empty in range(insert_idx+1):
                box[row][empty] = '.'
                
        return [[box[row][col] for row in range(ROW-1, -1, -1)] for col in range(COL)]