'''
3363. Find the Maximum Number of Fruits Collected
Hard
Topics
premium lock icon
Companies
Hint
There is a game dungeon comprised of n x n rooms arranged in a grid.

You are given a 2D array fruits of size n x n, where fruits[i][j] represents the number of fruits in the room (i, j). Three children will play in the game dungeon, with initial positions at the corner rooms (0, 0), (0, n - 1), and (n - 1, 0).

The children will make exactly n - 1 moves according to the following rules to reach the room (n - 1, n - 1):

The child starting from (0, 0) must move from their current room (i, j) to one of the rooms (i + 1, j + 1), (i + 1, j), and (i, j + 1) if the target room exists.
The child starting from (0, n - 1) must move from their current room (i, j) to one of the rooms (i + 1, j - 1), (i + 1, j), and (i + 1, j + 1) if the target room exists.
The child starting from (n - 1, 0) must move from their current room (i, j) to one of the rooms (i - 1, j + 1), (i, j + 1), and (i + 1, j + 1) if the target room exists.
When a child enters a room, they will collect all the fruits there. If two or more children enter the same room, only one child will collect the fruits, and the room will be emptied after they leave.

Return the maximum number of fruits the children can collect from the dungeon.

 

Example 1:

Input: fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]

Output: 100

Explanation:



In this example:

The 1st child (green) moves on the path (0,0) -> (1,1) -> (2,2) -> (3, 3).
The 2nd child (red) moves on the path (0,3) -> (1,2) -> (2,3) -> (3, 3).
The 3rd child (blue) moves on the path (3,0) -> (3,1) -> (3,2) -> (3, 3).
In total they collect 1 + 6 + 11 + 16 + 4 + 8 + 12 + 13 + 14 + 15 = 100 fruits.

Example 2:

Input: fruits = [[1,1],[1,1]]

Output: 4

Explanation:

In this example:

The 1st child moves on the path (0,0) -> (1,1).
The 2nd child moves on the path (0,1) -> (1,1).
The 3rd child moves on the path (1,0) -> (1,1).
In total they collect 1 + 1 + 1 + 1 = 4 fruits.

 

Constraints:

2 <= n == fruits.length == fruits[i].length <= 1000
0 <= fruits[i][j] <= 1000
'''

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        '''
        n-1回しか動けない。つまり、左上のやつは、斜め下にしか行けない。
        '''
        self.N = len(fruits)
        self.fruits = fruits
        # Child1: Diagonal that we go through for sure
        first = sum(fruits[i][i] for i in range(self.N))
        return first + self.helper1(0, self.N-1) + self.helper2(self.N-1, 0)
    
    # Child2
    @cache
    def helper1(self, r, c):
        if r >= self.N or c >= self.N:
            return 0
        if r >= c:
            return 0
        return self.fruits[r][c] + max(self.helper1(r+1, c-1), self.helper1(r+1, c), self.helper1(r+1, c+1))

    # Child3
    @cache
    def helper2(self, r, c):
        if r >= self.N or c >= self.N:
            return 0
        if c >= r:
            return 0
        return self.fruits[r][c] + max(self.helper2(r-1, c+1), self.helper2(r, c+1), self.helper2(r+1, c+1))