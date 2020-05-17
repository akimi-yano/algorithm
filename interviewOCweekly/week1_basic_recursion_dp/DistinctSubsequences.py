# 501 - Distinct Subsequences

# Given a string S and a string T, count the number of distinct subsequences of S which equals T.

# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
# (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

# ```
# Input: 	 String, String
# Output:  Int
# ```

# # Example
# ```
# Input 1:  "rabbbit", "rabbit"
# Output 1: 3    

# Subsequences:
# rabbbit --> rabbit
# ^^^^ ^^
# rabbbit --> rabbit
# ^^ ^^^^
# rabbbit --> rabbit
# ^^^ ^^^

# Input 2:  "a", "" 	           
# Output 2: 1 ("a" --> "")   

# ```


# # Constraints

# ```
# Time Complexity: O(N * M) with N being the length of string, and M being the length of the subsequence.
# Auxiliary Space Complexity: O(N)     
# ```
