# pattern4: Longest Palindromic Subsequence
# A: Longest Palindromic Subsequence
# Problem Statement #
# Given a sequence, find the length of its Longest Palindromic Subsequence (LPS). In a palindromic subsequence, elements read the same backward and forward.

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

# Example 1:

# Input: "abdbca"
# Output: 5
# Explanation: LPS is "abdba".
# Example 2:

# Input: = "cddpd"
# Output: 3
# Explanation: LPS is "ddd".
# Example 3:

# Input: = "pqr"
# Output: 1
# Explanation: LPS could be "p", "q" or "r".

# B: Longest Palindromic Substring

# Problem Statement #
# Given a string, find the length of its Longest Palindromic Substring (LPS). In a palindromic string, elements read the same backward and forward.

# Example 1:

# Input: "abdbca"
# Output: 3
# Explanation: LPS is "bdb".
# Example 2:

# Input: = "cddpd"
# Output: 3
# Explanation: LPS is "dpd".
# Example 3:

# Input: = "pqr"
# Output: 1
# Explanation: LPS could be "p", "q" or "r".

# C: Count of Palindromic Substrings
# Problem Statement #
# Given a string, find the total number of palindromic substrings in it. Please note we need to find the total number of substrings and not subsequences.

# Example 1:

# Input: "abdbca"
# Output: 7
# Explanation: Here are the palindromic substrings, "a", "b", "d", "b", "c", "a", "bdb".
# Example 2:

# Input: = "cddpd"
# Output: 7
# Explanation: Here are the palindromic substrings, "c", "d", "d", "p", "d", "dd", "dpd".
# Example 3:

# Input: = "pqr"
# Output: 3
# Explanation: Here are the palindromic substrings,"p", "q", "r".

# D: Minimum Deletions in a String to make it a Palindrome

# Problem Statement #
# Given a string, find the minimum number of characters that we can remove to make it a palindrome.

# Example 1:

# Input: "abdbca"
# Output: 1
# Explanation: By removing "c", we get a palindrome "abdba".
# Example 2:

# Input: = "cddpd"
# Output: 2
# Explanation: Deleting "cp", we get a palindrome "ddd".
# Example 3:

# Input: = "pqr"
# Output: 2
# Explanation: We have to remove any two characters to get a palindrome, e.g. if we 
# remove "pq", we get palindrome "r".

# E: Palindromic Partitioning

# Problem Statement #
# Given a string, we want to cut it into pieces such that each piece is a palindrome. Write a function to return the minimum number of cuts needed.

# Example 1:

# Input: "abdbca"
# Output: 3
# Explanation: Palindrome pieces are "a", "bdb", "c", "a".
# Example 2:

# Input: = "cddpd"
# Output: 2
# Explanation: Palindrome pieces are "c", "d", "dpd".
# Example 3:

# Input: = "pqr"
# Output: 2
# Explanation: Palindrome pieces are "p", "q", "r".
# Example 4:

# Input: = "pp"
# Output: 0
# Explanation: We do not need to cut, as "pp" is a palindrome.