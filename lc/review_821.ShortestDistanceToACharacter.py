# 821. Shortest Distance to a Character
# Easy

# 1465

# 93

# Add to List

# Share
# Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the shortest distance from s[i] to the character c in s.



# Example 1:

# Input: s = "loveleetcode", c = "e"
# Output: [3,2,1,0,1,0,0,1,2,2,1,0]
# Example 2:

# Input: s = "aaab", c = "b"
# Output: [3,2,1,0]

# Constraints:

# 1 <= s.length <= 104
# s[i] and c are lowercase English letters.
# c occurs at least once in s.

# This solution works - optimization:
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        '''
        check forwards and backwards :)
        '''
        ans = [float('inf') for _ in range(len(s))]
        
        prevc = float('-inf')
        for i in range(len(s)):
            if s[i] == c:
                prevc = i
            ans[i] = min(ans[i], i-prevc)
            
        prevc = float('inf')
        for i in range(len(s)-1,-1,-1):
            if s[i] == c:
                prevc = i
            ans[i] = min(ans[i], prevc-i)
                    
        return ans
    
# This solution works:
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = [float('inf') for _ in range(len(s))]
        zeros = []
        for i in range(len(s)):
            if s[i] == c:
                zeros.append(i)
                
        for i in zeros:
            ans[i] = 0
            left = i-1
            right = i+1
            cur = 1
            while -1 < left < len(ans) and ans[left]!=0:
                ans[left] = min(cur, ans[left])
                left -=1
                cur+=1
                
            cur = 1
            while len(ans) > right > -1 and ans[right]!=0:
                ans[right] = min(cur, ans[right])
                right +=1
                cur+=1
                
        return ans