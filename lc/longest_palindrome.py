# Longest Palindrome
class Solution:
    def longestPalindrome(self, s: str) -> int:
        memo = {}
        for c in s:
            if c not in memo:
                memo[c] = 1
            else:
                memo[c] += 1
        # print(memo)
        use = 0
        odd = False
        for v in memo.values():
            if v%2==0:
                use+=v
            else:
                use+=(v-1)
                odd = True
        return use+1 if odd else use
    

# cool way 
# count how many letters appear an odd number of times. 
# Because we can use all letters, except for each odd-count letter we must leave one, 
# except one of them we can use.

def longestPalindrome(self, s):
    odds = sum(v & 1 for v in collections.Counter(s).values())
    return len(s) - odds + bool(odds)