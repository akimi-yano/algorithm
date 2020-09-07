# 131. Palindrome Partitioning
# Medium

# 2103

# 73

# Add to List

# Share
# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return all possible palindrome partitioning of s.

# Example:

# Input: "aab"
# Output:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

# # THIS APPROACHED DOES NOT WORK _ LOOK BELOW 
# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
        
#         '''
#         Input: "aab"

#         Output:

#         [
#           ["aa","b"],
#           ["a","a","b"]
#         ]

#         aab - original
#         a ab - x - 
#         aa b - o - 
#         a a b - o - 

#         1 generate all possible substrings
#         2 loops to see if they are palinsrome 
#         '''
#         def helper(sub):
#             if len(sub) <= 1:
#                 return sub
#             temp = []
#             for i in range(len(sub)):
#                 array = helper(sub[i+1:])
#                 # print([sub[:i]])
#                 # print(array)
#                 # [for arr in ]
#                 for arr in array:
#                     temp.append(sub[:i]+arr) 
#             # print(temp)
#             return temp
#         return helper(s)

# THIS works xD !!!
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(st):
            for i in range(len(st)//2):
                if st[i]!=st[len(st)-1-i]:
                    return False
            return True
        
        @lru_cache(None)
        def helper(sub):
            ans = []
            if len(sub) < 1:
                return [[]]
            for end in range(1, len(sub)+1):
                cur = sub[:end]
                rest = sub[end:]
                # print(cur, rest)
                if is_palindrome(cur):
                    partitions = helper(rest)
                    for partition in partitions:
                        ans.append([cur] + partition)
            return ans
        return helper(s)

# Cleaned up code x) :
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(st):
            for i in range(len(st)//2):
                if st[i]!=st[len(st)-1-i]:
                    return False
            return True
        
        @lru_cache(None)
        def helper(sub):
            ans = []
            if len(sub) < 1:
                return [[]]
            for end in range(1, len(sub)+1):
                first_partition = sub[:end]
                rest_substr = sub[end:]
                if is_palindrome(first_partition):
                    results = helper(rest_substr)
                    for rest_partitions in results:
                        # fist_partition is a single (palin) string  and rest_partitions are the list of (palin) strings
                        ans.append([first_partition] + rest_partitions)
            return ans
        return helper(s)