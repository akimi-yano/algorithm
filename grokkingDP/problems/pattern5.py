# pattern 5: Longest Common Substring
# A: Longest Common Substring
# Problem Statement #
# Given two strings ‘s1’ and ‘s2’, find the length of the longest substring which is common in both the strings.

# Example 1:

# Input: s1 = "abdca"
#        s2 = "cbda"
# Output: 2
# Explanation: The longest common substring is "bd".
# Example 2:

# Input: s1 = "passport"
#        s2 = "ppsspt"
# Output: 3
# Explanation: The longest common substring is "ssp".

# B: Longest Common Subsequence
# Problem Statement #
# Given two strings ‘s1’ and ‘s2’, find the length of the longest subsequence which is common in both the strings.

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

# Example 1:

# Input: s1 = "abdca"
#        s2 = "cbda"
# Output: 3
# Explanation: The longest common subsequence is "bda".
# Example 2:

# Input: s1 = "passport"
#        s2 = "ppsspt"
# Output: 5
# Explanation: The longest common subsequence is "psspt".

# C: Minimum Deletions & Insertions to Transform a String into another
# Problem Statement #
# Given strings s1 and s2, we need to transform s1 into s2 by deleting and inserting characters. Write a function to calculate the count of the minimum number of deletion and insertion operations.

# Example 1:

# Input: s1 = "abc"
#        s2 = "fbc"
# Output: 1 deletion and 1 insertion.
# Explanation: We need to delete {'a'} and insert {'f'} to s1 to transform it into s2.
# Example 2:

# Input: s1 = "abdca"
#        s2 = "cbda"
# Output: 2 deletions and 1 insertion.
# Explanation: We need to delete {'a', 'c'} and insert {'c'} to s1 to transform it into s2.
# Example 3:

# Input: s1 = "passport"
#        s2 = "ppsspt"
# Output: 3 deletions and 1 insertion
# Explanation: We need to delete {'a', 'o', 'r'} and insert {'p'} to s1 to transform it into s2.

# D: Longest Increasing Subsequence

# Problem Statement #
# Given a number sequence, find the length of its Longest Increasing Subsequence (LIS). In an increasing subsequence, all the elements are in increasing order (from lowest to highest).

# Example 1:

# Input: {4,2,3,6,10,1,12}
# Output: 5
# Explanation: The LIS is {2,3,6,10,12}.
# Example 1:

# Input: {-4,10,3,7,15}
# Output: 4
# Explanation: The LIS is {-4,3,7,15}.

# E: Maximum Sum Increasing Subsequence
# Problem Statement #
# Given a number sequence, find the increasing subsequence with the highest sum. Write a method that returns the highest sum.

# Example 1:

# Input: {4,1,2,6,10,1,12}
# Output: 32
# Explanation: The increaseing sequence is {4,6,10,12}. 
# Please note the difference, as the LIS is {1,2,6,10,12} which has a sum of '31'.
# Example 2:

# Input: {-4,10,3,7,15}
# Output: 25
# Explanation: The increaseing sequences are {10, 15} and {3,7,15}.


# F: Shortest Common Super-sequence
# Problem Statement #
# Given two sequences ‘s1’ and ‘s2’, write a method to find the length of the shortest sequence which has ‘s1’ and ‘s2’ as subsequences.

# Example 2:

# Input: s1: "abcf" s2:"bdcf" 
# Output: 5
# Explanation: The shortest common super-sequence (SCS) is "abdcf". 
# Example 2:

# Input: s1: "dynamic" s2:"programming" 
# Output: 15
# Explanation: The SCS is "dynprogrammicng". 
# G: Minimum Deletions to Make a Sequence Sorted

# Problem Statement #
# Given a number sequence, find the minimum number of elements that should be deleted to make the remaining sequence sorted.

# Example 1:

# Input: {4,2,3,6,10,1,12}
# Output: 2
# Explanation: We need to delete {4,1} to make the remaing sequence sorted {2,3,6,10,12}.
# Example 2:

# Input: {-4,10,3,7,15}
# Output: 1
# Explanation: We need to delete {10} to make the remaing sequence sorted {-4,3,7,15}.
# Example 3:

# Input: {3,2,1,0}
# Output: 3
# Explanation: Since the elements are in reverse order, we have to delete all except one to get a 
# sorted sequence. Sorted sequences are {3}, {2}, {1}, and {0}

# H: Longest Repeating Subsequence

# Problem Statement #
# Given a sequence, find the length of its longest repeating subsequence (LRS). A repeating subsequence will be the one that appears at least twice in the original sequence and is not overlapping (i.e. none of the corresponding characters in the repeating subsequences have the same index).

# Example 1:

# Input: “t o m o r r o w”
# Output: 2
# Explanation: The longest repeating subsequence is “or” {tomorrow}.

# Example 2:

# Input: “a a b d b c e c”
# Output: 3
# Explanation: The longest repeating subsequence is “a b c” {a a b d b c e c}.

# Example 3:

# Input: “f m f f”
# Output: 2
# Explanation: The longest repeating subsequence is “f f” {f m f f, f m f f}. Please note the second last character is shared in LRS.


# I: Subsequence Pattern Matching
# Problem Statement #
# Given a string and a pattern, write a method to count the number of times the pattern appears in the string as a subsequence.

# Example 1: Input: string: “baxmx”, pattern: “ax”
# Output: 2
# Explanation: {baxmx, baxmx}.

# Example 2:

# Input: string: “tomorrow”, pattern: “tor”
# Output: 4
# Explanation: Following are the four occurences: {tomorrow, tomorrow, tomorrow, tomorrow}.

# J: Longest Bitonic Subsequence
# Problem Statement #
# Given a number sequence, find the length of its Longest Bitonic Subsequence (LBS). A subsequence is considered bitonic if it is monotonically increasing and then monotonically decreasing.

# Example 1:

# Input: {4,2,3,6,10,1,12}
# Output: 5
# Explanation: The LBS is {2,3,6,10,1}.
# Example 2:

# Input: {4,2,5,9,7,6,10,3,1}
# Output: 7
# Explanation: The LBS is {4,5,9,7,6,3,1}.

# K: Longest Alternating Subsequence
# Problem Statement #
# Given a number sequence, find the length of its Longest Alternating Subsequence (LAS). A subsequence is considered alternating if its elements are in alternating order.

# A three element sequence (a1, a2, a3) will be an alternating sequence if its elements hold one of the following conditions:

# {a1 > a2 < a3 } or { a1 < a2 > a3}. 
# Example 1:

# Input: {1,2,3,4}
# Output: 2
# Explanation: There are many LAS: {1,2}, {3,4}, {1,3}, {1,4}
# Example 2:

# Input: {3,2,1,4}
# Output: 3
# Explanation: The LAS are {3,2,4} and {2,1,4}.
# Example 3:

# Input: {1,3,2,4}
# Output: 4
# Explanation: The LAS is {1,3,2,4}.

# L: Edit Distance
# Problem Statement #
# Given strings s1 and s2, we need to transform s1 into s2 by deleting, inserting, or replacing characters. Write a function to calculate the count of the minimum number of edit operations.

# Example 1:

# Input: s1 = "bat"
#        s2 = "but"
# Output: 1
# Explanation: We just need to replace 'a' with 'u' to transform s1 to s2.
# Example 2:

# Input: s1 = "abdca"
#        s2 = "cbda"
# Output: 2
# Explanation: We can replace first 'a' with 'c' and delete second 'c'.
# Example 3:

# Input: s1 = "passpot"
#        s2 = "ppsspqrt"
# Output: 3 
# Explanation: Replace 'a' with 'p', 'o' with 'q', and insert 'r'.

# M: Strings Interleaving

# Problem Statement #
# Give three strings ‘m’, ‘n’, and ‘p’, write a method to find out if ‘p’ has been formed by interleaving ‘m’ and ‘n’. ‘p’ would be considered interleaving ‘m’ and ‘n’ if it contains all the letters from ‘m’ and ‘n’ and the order of letters is preserved too.

# Example 1:

# Input: m="abd", n="cef", p="abcdef"
# Output: true
# Explanation: 'p' contains all the letters from 'm' and 'n' and preserves their order too. 
# Example 2:

# Input: m="abd", n="cef", p="adcbef"
# Output: false
# Explanation: 'p' contains all the letters from 'm' and 'n' but does not preserve the order. 
# Example 3:

# Input: m="abc", n="def", p="abdccf"
# Output: false
# Explanation: 'p' does not contain all the letters from 'm' and 'n'. 
# Example 4:

# Input: m="abcdef", n="mnop", p="mnaobcdepf"
# Output: true
# Explanation: 'p' contains all the letters from 'm' and 'n' and preserves their order too. 
