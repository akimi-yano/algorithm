# pattern 1 : 0/1 knapsack
# A: 0/1 Knapsack

# Introduction #
# Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack which has a capacity ‘C’. The goal is to get the maximum profit from the items in the knapsack. Each item can only be selected once, as we don’t have multiple quantities of any item.

# Let’s take the example of Merry, who wants to carry some fruits in the knapsack to get maximum profit. Here are the weights and profits of the fruits:

# Items: { Apple, Orange, Banana, Melon }
# Weights: { 2, 3, 1, 4 }
# Profits: { 4, 5, 3, 7 }
# Knapsack capacity: 5

# Let’s try to put different combinations of fruits in the knapsack, such that their total weight is not more than 5:

# Apple + Orange (total weight 5) => 9 profit
# Apple + Banana (total weight 3) => 7 profit
# Orange + Banana (total weight 4) => 8 profit
# Banana + Melon (total weight 5) => 10 profit

# This shows that Banana + Melon is the best combination, as it gives us the maximum profit and the total weight does not exceed the capacity.

# Problem Statement #
# Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C’. Each item can only be selected once, which means either we put an item in the knapsack or we skip it.


# code here

# B: Equal Subset Sum Partition

# Problem Statement #
# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both the subsets is equal.

# Example 1: #
# Input: {1, 2, 3, 4}
# Output: True
# Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}
# Example 2: #
# Input: {1, 1, 3, 4, 7}
# Output: True
# Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}
# Example 3: #
# Input: {2, 3, 4, 6}
# Output: False
# Explanation: The given set cannot be partitioned into two subsets with equal sum.

# code here

# C: Subset Sum

# Problem Statement #
# Given a set of positive numbers, determine if there exists a subset whose sum is equal to a given number ‘S’.

# Example 1: #
# Input: {1, 2, 3, 7}, S=6
# Output: True
# The given set has a subset whose sum is '6': {1, 2, 3}
# Example 2: #
# Input: {1, 2, 7, 1, 5}, S=10
# Output: True
# The given set has a subset whose sum is '10': {1, 2, 7}
# Example 3: #
# Input: {1, 3, 4, 8}, S=6
# Output: False
# The given set does not have any subset whose sum is equal to '6'.

# D: Minimum Subset Sum Difference

# Problem Statement #
# Given a set of positive numbers, partition the set into two subsets with a minimum difference between their subset sums.

# Example 1: #
# Input: {1, 2, 3, 9}
# Output: 3
# Explanation: We can partition the given set into two subsets where minimum absolute difference 
# between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.
# Example 2: #
# Input: {1, 2, 7, 1, 5}
# Output: 0
# Explanation: We can partition the given set into two subsets where minimum absolute difference 
# between the sum of number is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.
# Example 3: #
# Input: {1, 3, 100, 4}
# Output: 92
# Explanation: We can partition the given set into two subsets where minimum absolute difference 
# between the sum of numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.


# E: Count of Subset Sum

# Problem Statement #
# Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.

# Example 1: #
# Input: {1, 1, 2, 3}, S=4
# Output: 3
# The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
# Note that we have two similar sets {1, 3}, because we have two '1' in our input.
# Example 2: #
# Input: {1, 2, 7, 1, 5}, S=9
# Output: 3
# The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}

# F: Target Sum

# Problem Statement #
# Given a set of positive numbers (non zero) and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign. We need to find out total ways to assign symbols to make the sum of numbers equal to target ‘S’.

# Example 1: #
# Input: {1, 1, 2, 3}, S=1
# Output: 3
# Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}
# Example 2: #
# Input: {1, 2, 7, 1}, S=9
# Output: 2
# Explanation: The given set has '2' ways to make a sum of '9': {+1+2+7-1} & {-1+2+7+1}

