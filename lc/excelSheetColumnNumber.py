# 171. Excel Sheet Column Number

class Solution:
    def titleToNumber(self, s: str) -> int:
        memo={}
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(len(alpha)):
            memo[alpha[i]]=i+1

        ans=0
        for i in range(len(s)):
            if s[i] in memo:
                ans += memo[s[i]]*26**(len(s)-1-i)
        return ans
    

# class Solution:
#     def titleToNumber(self, s: str) -> int:
#         memo={}
#         alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#         for i in range(len(alpha)):
#             memo[alpha[i]]=i+1
#         # for key, value in memo.items():
#         #     print(key, value)
#         if len(s) == 1:
#             if s in memo:
#                 return memo[s]
#         if len(s)==2:
#             if s[0] in memo:
#                 ans= memo[s[0]]*26 
#                 if s[1] in memo:
#                     ans+=memo[s[1]]
#                     return ans
#         if len(s)==3:
#              if s[0] in memo:
#                 ans= memo[s[0]]*26*26
#                 if s[1] in memo:
#                     ans+= memo[s[1]]*26
#                     if s[2] in memo:
#                         ans+=memo[s[2]]
#                         return ans
                    
#         if len(s)==4:
#             if s[0] in memo:
#                 ans= memo[s[0]]*26*26*26
#                 if s[1] in memo:
#                     ans+= memo[s[1]]*26*26
#                     if s[2] in memo:
#                         ans+=memo[s[2]]*26
#                         if s[3] in memo:
#                             ans+=memo[s[3]]
#                             return ans
                
#         ans=0
#         for i in range(len(s)):
#             if s[i] in memo:
#                 ans += memo[s[i]]*26**(len(s)-1-i)