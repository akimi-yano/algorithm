# 1531. String Compression II

# Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".

# Notice that in this problem, we are not adding '1' after single characters.

# Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.

# Find the minimum length of the run-length encoded version of s after deleting at most k characters.

 

# Example 1:

# Input: s = "aaabcccd", k = 2
# Output: 4
# Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6. Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.
# Example 2:

# Input: s = "aabbaa", k = 2
# Output: 2
# Explanation: If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.
# Example 3:

# Input: s = "aaaaaaaaaaa", k = 0
# Output: 3
# Explanation: Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.
 

# Constraints:

# 1 <= s.length <= 100
# 0 <= k <= s.length
# s contains only lowercase English letters.







# this solution does not work - check below for the solution that works


# import heapq
# class Solution:
#     def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
#         # somehow needs to figure out if it is better off to delete smaller count or larger digits that are about to become smaller digits -  whichever's smaller ... but then it depends on that the k is ... 
#         memo = {}
#         for c in s:
#             if c not in memo:
#                 memo[c]=1
#             else:
#                 memo[c]+=1
#         # print(memo)
    
#         minheap = []
#         for key,val in memo.items():
#             heapq.heappush(minheap,(val,key))
#         # print(minheap)
#         while k>0:
#             count,char = heapq.heappop(minheap)
#             count-=1
#             if count>0:
#                 heapq.heappush(minheap,(count,char))
#             k-=1
#         counter = 0
#         # print(minheap)
#         while minheap:
#             count,char=heapq.heappop(minheap)
#             if count >1:
#                 counter+=len(str(count))+1
#             else:counter+=1
#         return counter






# this solutions worked ! yay




class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # to do memorization - place above the helper
        @lru_cache(None)
        def helper(s,start,prev,count,remaining):
            # if we run out of k, we end - throw positive infinity
            if remaining <0:
                return float('inf')
            # if we get to the end of string, return 0
            if start>=len(s):
                return 0
            # if the character is the same as previous one
            if s[start]==prev:
                # increase 1 because the length will increase by 1 for below cases
                incr = 1 if count == 1 or count == 9 or count == 99 else 0
                # add the increased amount
                return incr+helper(s,start+1,prev,count+1,remaining)
            # if its not the same as previous one, we have 2 options - 
            # either to keep it or remove it
            elif s[start]!=prev:
                # if we keep,we need to increase the length by 1 
                # if we remove, we decrement the remaining by 1
                return min(1+helper(s,start+1,s[start],1,remaining),helper(s,start+1,prev,count,remaining-1))
        return helper(s,0,"",0,k)