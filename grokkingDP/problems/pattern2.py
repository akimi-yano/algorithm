# Pattern 2: Unbounded Knapsack

# A: Unbounded Knapsack

# Introduction #
# Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack which has a capacity ‘C’. The goal is to get the maximum profit from the items in the knapsack. The only difference between the 0/1 Knapsack problem and this problem is that we are allowed to use an unlimited quantity of an item.

# Let’s take the example of Merry, who wants to carry some fruits in the knapsack to get maximum profit. Here are the weights and profits of the fruits:

# Items: { Apple, Orange, Melon }
# Weights: { 1, 2, 3 }
# Profits: { 15, 20, 50 }
# Knapsack capacity: 5

# Let’s try to put different combinations of fruits in the knapsack, such that their total weight is not more than 5.

# 5 Apples (total weight 5) => 75 profit
# 1 Apple + 2 Oranges (total weight 5) => 55 profit
# 2 Apples + 1 Melon (total weight 5) => 80 profit
# 1 Orange + 1 Melon (total weight 5) => 70 profit

# This shows that 2 apples + 1 melon is the best combination, as it gives us the maximum profit and the total weight does not exceed the capacity.

# Problem Statement #
# Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C’. We can assume an infinite supply of item quantities; therefore, each item can be selected multiple times.

# B: Rod Cutting

# Problem Statement #
# Given a rod of length ‘n’, we are asked to cut the rod and sell the pieces in a way that will maximize the profit. We are also given the price of every piece of length ‘i’ where ‘1 <= i <= n’.

# Example:

# Lengths: [1, 2, 3, 4, 5]
# Prices: [2, 6, 7, 10, 13]
# Rod Length: 5

# Let’s try different combinations of cutting the rod:

# Five pieces of length 1 => 10 price
# Two pieces of length 2 and one piece of length 1 => 14 price
# One piece of length 3 and two pieces of length 1 => 11 price
# One piece of length 3 and one piece of length 2 => 13 price
# One piece of length 4 and one piece of length 1 => 12 price
# One piece of length 5 => 13 price

# This shows that we get the maximum price (14) by cutting the rod into two pieces of length ‘2’ and one piece of length ‘1’.

# C: Coin Change

# Introduction #
# Given an infinite supply of ‘n’ coin denominations and a total money amount, we are asked to find the total number of distinct ways to make up that amount.

# Example:

# Denominations: {1,2,3}
# Total amount: 5
# Output: 5
# Explanation: There are five ways to make the change for '5', here are those ways:
#   1. {1,1,1,1,1} 
#   2. {1,1,1,2} 
#   3. {1,2,2}
#   4. {1,1,3}
#   5. {2,3}
# Problem Statement #
# Given a number array to represent different coin denominations and a total amount ‘T’, we need to find all the different ways to make a change for ‘T’ with the given coin denominations. We can assume an infinite supply of coins, therefore, each coin can be chosen multiple times.

# This problem follows the Unbounded Knapsack pattern.

# D: Minimum Coin Change

# Introduction #
# Given an infinite supply of ‘n’ coin denominations and a total money amount, we are asked to find the minimum number of coins needed to make up that amount.

# Example 1:

# Denominations: {1,2,3}
# Total amount: 5
# Output: 2
# Explanation: We need minimum of two coins {2,3} to make a total of '5'
# Example 2:

# Denominations: {1,2,3}
# Total amount: 11
# Output: 4
# Explanation: We need minimum four coins {2,3,3,3} to make a total of '11'
# Problem Statement #
# Given a number array to represent different coin denominations and a total amount ‘T’, we need to find the minimum number of coins needed to make change for ‘T’. We can assume an infinite supply of coins, therefore, each coin can be chosen multiple times.

# This problem follows the Unbounded Knapsack pattern.

# E: Maximum Ribbon Cut
# Introduction #
# We are given a ribbon of length ‘n’ and a set of possible ribbon lengths. Now we need to cut the ribbon into the maximum number of pieces that comply with the above-mentioned possible lengths. Write a method that will return the count of pieces.

# Example 1:

# n: 5
# Ribbon Lengths: {2,3,5}
# Output: 2
# Explanation: Ribbon pieces will be {2,3}.
# Example 2:

# n: 7
# Ribbon Lengths: {2,3}
# Output: 3
# Explanation: Ribbon pieces will be {2,2,3}.
# Example 3:

# n: 13
# Ribbon Lengths: {3,5,7}
# Output: 3
# Explanation: Ribbon pieces will be {3,3,7}.
# Problem Statement #
# Given a number array to represent possible ribbon lengths and a total ribbon length ‘n’, we need to find the maximum number of pieces that the ribbon can be cut into.

# This problem follows the Unbounded Knapsack pattern and is quite similar to Minimum Coin Change (MCC). The only difference is that in MCC we were asked to find the minimum number of coin changes, whereas in this problem we need to find the maximum number of pieces.