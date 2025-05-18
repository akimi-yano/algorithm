'''
1931. Painting a Grid With Three Different Colors
Hard
Topics
Companies
Hint
You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.

Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:


Input: m = 1, n = 1
Output: 3
Explanation: The three possible colorings are shown in the image above.
Example 2:


Input: m = 1, n = 2
Output: 6
Explanation: The six possible colorings are shown in the image above.
Example 3:

Input: m = 5, n = 5
Output: 580986
 

Constraints:

1 <= m <= 5
1 <= n <= 1000
'''

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        C = [c for c in product([0,1,2], repeat = m) if all(x!=y for x,y in zip(c, c[1:]))]

        MOD, dp, d = 10**9 + 7, Counter(C), defaultdict(list)

        for c1, c2 in product(C, C):
            if all(x != y for x, y in zip(c1, c2)):
                d[c1].append(c2)

        for _ in range(n-1):
            dp2 = Counter()
            for c1 in C:
                for c2 in d[c1]:
                    dp2[c2] = (dp2[c2] + dp[c1]) % MOD
            dp = dp2

        return sum(dp.values()) % MOD
