# 171. Excel Sheet Column Number
# Easy

# 2657

# 246

# Add to List

# Share
# Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 

# Example 1:

# Input: columnTitle = "A"
# Output: 1
# Example 2:

# Input: columnTitle = "AB"
# Output: 28
# Example 3:

# Input: columnTitle = "ZY"
# Output: 701
 

# Constraints:

# 1 <= columnTitle.length <= 7
# columnTitle consists only of uppercase English letters.
# columnTitle is in the range ["A", "FXSHRXW"].


# This solution works:


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        '''
        "A" -> 1
        "B" -> 2
        ord(columnTitle) - ord('A') + 1
        
        "AA" -> 27
        26+1
        z + 1
        
        AZ -> 26 +26
        
        BA -> 26+26 +1
        
        26*(number of this digit) + 1
        
        ZZ -> 26*26 +26=702
        
        AAA->703
        26**2*(number of this digit) = 26 ** 2 * 1 = 676
        26**1*(number of this digit) = 26 ** 1 * 1 = 26
        26**0*(number of this digit) = 1
        
        703
        '''
        ans = 0
        for i in range(len(columnTitle)):
            ans += (ord(columnTitle[i]) - ord('A') + 1) * 26 ** (len(columnTitle)-1-i)
        return ans