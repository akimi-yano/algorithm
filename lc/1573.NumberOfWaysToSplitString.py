# 1573. Number of Ways to Split a String
# Medium

# 40

# 6

# Add to List

# Share
# Given a binary string s (a string consisting only of '0's and '1's), we can split s into 3 non-empty strings s1, s2, s3 (s1+ s2+ s3 = s).

# Return the number of ways s can be split such that the number of characters '1' is the same in s1, s2, and s3.

# Since the answer may be too large, return it modulo 10^9 + 7.

 

# Example 1:

# Input: s = "10101"
# Output: 4
# Explanation: There are four ways to split s in 3 parts where each part contain the same number of letters '1'.
# "1|010|1"
# "1|01|01"
# "10|10|1"
# "10|1|01"
# Example 2:

# Input: s = "1001"
# Output: 0
# Example 3:

# Input: s = "0000"
# Output: 3
# Explanation: There are three ways to split s in 3 parts.
# "0|0|00"
# "0|00|0"
# "00|0|0"
# Example 4:

# Input: s = "100100010100110"
# Output: 12
 

# Constraints:

# s[i] == '0' or s[i] == '1'
# 3 <= s.length <= 10^5



# Solution I had  during the comp ! This solution ACed !!!

from math import comb
class Solution:
    def numWays(self, s: str) -> int:
        '''
        count 1 -> if count of 1 is not 3's multiplier -> return 0
        '''
        if not s:
            return 0
        count = {}
        for c in s:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1
        # print(count)
        
        if '1' in count:
            if count['1'] % 3!=0:
                return 0
            else:
                target = count['1'] // 3
        else:
            target = 0
        if not target:
            return math.comb(count['0'] -1,2) % ((10**9) + 7)

        parts = []
        cur1 = 0
        cur0 = 0
        countzero = False
        for i, c in enumerate(s):
            if countzero == True and c =='0':
                cur0+=1
            elif c =='1':
                if countzero:
                    parts.append(cur0 +1)
                    countzero = False
                    cur0=0
                    cur1 = 0
                cur1 +=1
                if cur1 == target:
                    countzero = True
        ans = 1
        for p in parts:
            ans*=p
        return ans % ((10**9) + 7)