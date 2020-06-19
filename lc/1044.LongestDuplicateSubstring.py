# 1044. Longest Duplicate Substring
# Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

# Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)

# Example 1:

# Input: "banana"
# Output: "ana"
# Example 2:

# Input: "abcd"
# Output: ""

# Note:

# 2 <= S.length <= 10^5
# S consists of lowercase English letters.


# brute force - doesnt work !!!!!
# class Solution:
#     def longestDupSubstring(self, S: str) -> str:
#         seen = set([])
#         longest = None
#         for i in range(len(S)):
#             for k in range(i,len(S)):
#                 sub = S[i:k+1]
#                 if sub not in seen:
#                     seen.add(sub)
#                 else:
#                     if longest is None:
#                         longest = sub
#                     else:                    
#                         if len(longest)< len(sub):
#                             longest = sub
#         return "" if longest is None else longest
                    
'''                 
Input: "banana"
''
b ba ban bana banan banana
a an ana anan anana
n na nan nana
a an ana
n na
a
Output: "ana"
'''


# Solution

# Intuition
# Suffix array is typical solution for this problem.
# The fastest way is to copy a template form the Internet.
# The code will be quite long.
# Here I want to share a binary search solution.


# Explanation
# Binary search the length of longest duplicate substring and call the help function test(L).
# test(L) slide a window of length L,
# rolling hash the string in this window,
# record the seen string in a hashset,
# and try to find duplicated string.

# I give it a big mod for rolling hash and it should be enough for this problem.
# Actually there could be hash collision.
# One solution is to have two different mod for hash.
# Or we can use a hashmap to record the index of string.


# Complexity
# Binary Search in range 1 and N, so it's O(logN)
# Rolling hash O(N)
# Overall O(NlogN)
# SpaceO(N)


# The current solution has an issue with hash collisions. The code is accepted on LC because there are only 11 testcases and 
# the hash space is very large, meaning collisions are very unlikely. But on a larger test set collisions will happen. 
# I believe there should be a disclaimer about this in the the description.

# The issue is easily fixed using a hashmap to track prev occurrences of a hash, instead of just a set. It is a lot slower though, 
# by about 50%.


# This works

def longestDupSubstring(self, s: str) -> str:
    low, high = 2, len(s) - 1
    best = ''

    while low <= high:
        mid = low + (high - low) // 2
        v = self.find_duplicate_substr_of_len_k(s, mid)

        if v != '':
            best = v
            low = mid + 1
        else:
            high = mid - 1

    return best


def find_duplicate_substr_of_len_k(self, s, k):
    MOD = (1 << 61) - 1
    BASE = 26
    D = pow(BASE, k - 1, MOD)
    chash = 0
    seen = collections.defaultdict(list)

    for i in range(len(s)):
        if i >= k:
            l_chval = ord(s[i - k]) - ord('a')
            chash = (chash - l_chval * D) % MOD

        chval = ord(s[i]) - ord('a')
        chash = (chash * BASE + chval) % MOD

        if i >= k - 1:
            if chash in seen:
                substr_i = s[i - k + 1:i + 1]
                for j in seen[chash]:
                    substr_j = s[j - k + 1:j + 1]
                    if substr_i == substr_j:
                        return substr_i

            seen[chash].append(i)

    return ''