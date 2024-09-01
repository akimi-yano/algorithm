'''
6. Zigzag Conversion
Solved
Medium
Topics
Companies
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''

# This Solution works !

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        MAXROW = numRows-1
        MINROW = 0
        isGoingDown = True
        ans = [[] for _ in range(numRows)]
        row = 0
        
        for char in s:
            ans[row].append(char)
            if isGoingDown:
                row+=1
                if row > MAXROW:
                    isGoingDown = False
                    row-=2
            else:
                row-=1
                if row < MINROW:
                    isGoingDown = True
                    row+=2

        to_return = []           
        for row in ans:
            to_return.append("".join(row))
        return "".join(to_return)
