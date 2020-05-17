# 315 - Longest Palindromic Subsequence

# Given a string of lowercase characters (a-z), return the
# length of the longest palindromic subsequence.

# Subsequence: 
# a sequence that can be derived from another sequence by deleting some or 
# no elements without changing the order of the remaining elements. 

# For example, the sequence ⟨A, B, D⟩ is a subsequence of ⟨A, B, C, D, E, F⟩ 
# obtained after removal of elements C, E, and F. 

# https://en.m.wikipedia.org/wiki/Subsequence

# ```
# Input: {String}
# Output: {Integer}
# ```

# # Example

# ```
# Input:  "vtvvv"
# Output: 4

# Longest palindromic subsequence here is "vvvv"


# Input:  "pwnnb"
# Output: 2

# Longest palindromic subsequence here is "nn"


# Input:  "ttbtctcbt"
# Output: 7

# Longest palindromic subsequence here is "tbtctbt"
# ```

# # Constraints

# ```
# Time Complexity:			        O(N^2)
# Auxiliary Space Complexity: 		O(N^2)
# ```

# solution v1 - inefficient as there are dublicates so dont use this 
# def longestPalindromeSubseq(s):
#     def helper(left_idx, right_idx, memo):
#         if left_idx < 0 or right_idx >= len(s):
#             return 0
#         if (left_idx, right_idx) in memo:
#             return memo[(left_idx, right_idx)]
#         if s[left_idx] == s[right_idx]:
#             if left_idx == right_idx:
#                 score = 1
#             else:
#                 score = 2
#             best = score + helper(left_idx - 1, right_idx + 1, memo)
#         else:
#             best = max(
#                 helper(left_idx, right_idx + 1, memo),
#                 helper(left_idx - 1, right_idx, memo)
#             )
#         memo[(left_idx, right_idx)] = best
#         return best

#     best = 0
#     memo = {}
#     for left in range(len(s)):
#         for right in range(len(s), left-1, -1):
#             best = max(best, helper(left, right, memo))
#     return best

# solution v2 - better solution than v1 
def longestPalindromeSubseq(s: str) -> int:
        def helper(left_idx, right_idx, memo):
            if (left_idx, right_idx) in memo:
                return memo[(left_idx, right_idx)]

            best = 0
            if left_idx > right_idx:
                pass
            elif left_idx == right_idx:
                best = 1
            elif s[left_idx] == s[right_idx]:
                best = 2 + helper(left_idx + 1, right_idx - 1, memo)
            else:
                best = max(
                    helper(left_idx, right_idx - 1, memo),
                    helper(left_idx + 1, right_idx, memo)
                )
            memo[(left_idx, right_idx)] = best
            return best

        memo = {}
        helper(0, len(s) - 1, memo)
        return max(memo.values())
print(longestPalindromeSubseq('pwnnb'))
print(longestPalindromeSubseq('vtvvv'))
print(longestPalindromeSubseq('ttbtctcbt'))

