'''
1267. Count Servers that Communicate
Medium
Topics
Companies
Hint
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

 

Example 1:



Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.
Example 2:



Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.
Example 3:



Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
'''

from collections import defaultdict
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        rows = defaultdict(list)
        cols = defaultdict(list)
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col]:
                    rows[row].append((row, col))
                    cols[col].append((row, col))
        
        ans = set([])
        for v in rows.values():
            if len(v) >= 2:
                for tup in v:
                    ans.add(tup)
        
        for v in cols.values():
            if len(v) >= 2:
                for tup in v:
                    ans.add(tup)
        
        return len(ans)

# Another approach

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        
        comps_per_rows = Counter()
        comps_per_cols = Counter()
        points = []
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col]:
                    points.append((row, col))
                    comps_per_rows[row] += 1
                    comps_per_cols[col] += 1

        ans = 0
        for row, col in points:
            if comps_per_rows[row] > 1 or comps_per_cols[col] > 1:
                ans += 1
        return ans