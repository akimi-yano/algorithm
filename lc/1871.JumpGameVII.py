# 1871. Jump Game VII
# Medium

# 245

# 15

# Add to List

# Share
# You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

# i + minJump <= j <= min(i + maxJump, s.length - 1), and
# s[j] == '0'.
# Return true if you can reach index s.length - 1 in s, or false otherwise.

 

# Example 1:

# Input: s = "011010", minJump = 2, maxJump = 3
# Output: true
# Explanation:
# In the first step, move from index 0 to index 3. 
# In the second step, move from index 3 to index 5.
# Example 2:

# Input: s = "01101110", minJump = 2, maxJump = 3
# Output: false
 

# Constraints:

# 2 <= s.length <= 105
# s[i] is either '0' or '1'.
# s[0] == '0'
# 1 <= minJump <= maxJump < s.length

# This solution works:

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        idxs = []
        for i, c in enumerate(s):
            if c == '0':
                idxs.append(i)
        # print(s, idxs)
        if idxs[-1] != len(s) - 1:
            return False
        
        leftmost = rightmost = 0
        while rightmost != len(idxs) - 1:
            # try to find the next leftmost
            lmin, rmin = leftmost + 1, len(idxs) - 1
            while lmin < rmin:
                m = (lmin + rmin) // 2
                if idxs[m] - idxs[leftmost] < minJump:
                    lmin = m + 1
                else:
                    rmin = m
            if not idxs[leftmost] + minJump <= idxs[lmin] <= idxs[rightmost] + maxJump:
                return False
            
            # try to find the next rightmost
            lmax, rmax = rightmost + 1, len(idxs) - 1
            while lmax < rmax:
                m = (lmax + rmax + 1) // 2
                if idxs[m] - idxs[rightmost] > maxJump:
                    rmax = m - 1
                else:
                    lmax = m
            if not idxs[leftmost] + minJump <= idxs[lmax] <= idxs[rightmost] + maxJump:
                return False
            
            leftmost = lmin
            rightmost = lmax
        
        return True
            