'''
6. Zigzag Conversion
Medium
6.7K
13.2K
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

# Solution 1: 

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        N = len(s)
        ROW = numRows
        arr = [[' ' for _ in range(ROW)]]
        row = 0
        col = 0
        isGoingUp = False
        for char in s:
            arr[col][row] = char
            if row >= ROW-1:
                isGoingUp = True
            elif row <= 0:
                isGoingUp = False
            if not isGoingUp:
                row += 1
            else:
                row -= 1
                col += 1 
                arr.append([' ' for _ in range(ROW)])
        ans = []
        newROW = len(arr)
        newCOL = len(arr[0])
        for col in range(newCOL):
            for row in range(newROW):
                if arr[row][col] != ' ':
                    ans.append(arr[row][col])
        return ''.join(ans)

            
# Solution 2: mutating string every time we add a new char but the worst case is numRows * length of the string

class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        
        curRow, step = 0, 1
        rows = [''] * numRows # ['', '', '']
        
        for ch in s:
            rows[curRow] += ch
            if curRow == numRows - 1:
                step = -1
            elif curRow == 0:
                step = 1
            curRow += step
        
        return ''.join(rows) #['PAHN', 'APLSIIG', 'YIR'] -> "PAHNAPLSIIGYIR"