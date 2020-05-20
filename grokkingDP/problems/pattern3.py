# Pattern 3: Fibonacci numbers

# A: Fibonacci numbers
# Problem Statement #
# Write a function to calculate the nth Fibonacci number.

# Fibonacci numbers are a series of numbers in which each number is the sum of the two preceding numbers. First few Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, …

# Mathematically we can define the Fibonacci numbers as:

#     Fib(n) = Fib(n-1) + Fib(n-2), for n > 1

#     Given that: Fib(0) = 0, and Fib(1) = 1

# B: Staircase
# Problem Statement #
# Given a stair with ‘n’ steps, implement a method to count how many possible ways are there to reach the top of the staircase, given that, at every step you can either take 1 step, 2 steps, or 3 steps.

# Example 1:

# Number of stairs (n) : 3
# Number of ways = 4
# Explanation: Following are the four ways we can climb : {1,1,1}, {1,2}, {2,1}, {3} 
# Example 2:

# Number of stairs (n) : 4
# Number of ways = 7
# Explanation: Following are the seven ways we can climb : {1,1,1,1}, {1,1,2}, {1,2,1}, {2,1,1}, 
# {2,2}, {1,3}, {3,1}
# Let’s first start with a recursive brute-force solution.

# C: Number factors
# Problem Statement #
# Given a number ‘n’, implement a method to count how many possible ways there are to express ‘n’ as the sum of 1, 3, or 4.

# Example 1:

# n : 4
# Number of ways = 4
# Explanation: Following are the four ways we can exoress 'n' : {1,1,1,1}, {1,3}, {3,1}, {4} 
# Example 2:

# n : 5
# Number of ways = 6
# Explanation: Following are the six ways we can express 'n' : {1,1,1,1,1}, {1,1,3}, {1,3,1}, {3,1,1}, 
# {1,4}, {4,1}
# Let’s first start with a recursive brute-force solution.


# D: Minimum jumps to reach the end
# Problem Statement #
# Given an array of positive numbers, where each element represents the max number of jumps that can be made forward from that element, write a program to find the minimum number of jumps needed to reach the end of the array (starting from the first element). If an element is 0, then we cannot move through that element.

# Example 1:

# Input = {2,1,1,1,4}
# Output = 3
# Explanation: Starting from index '0', we can reach the last index through: 0->2->3->4
# Example 2:

# Input = {1,1,3,6,9,3,0,1,3}
# Output = 4
# Explanation: Starting from index '0', we can reach the last index through: 0->1->2->3->8
# Let’s first start with a recursive brute-force solution.

# E: Minimum jumps with fee

# Problem Statement #
# Given a staircase with ‘n’ steps and an array of ‘n’ numbers representing the fee that you have to pay if you take the step. Implement a method to calculate the minimum fee required to reach the top of the staircase (beyond the top-most step). At every step, you have an option to take either 1 step, 2 steps, or 3 steps. You should assume that you are standing at the first step.

# Example 1:

# Number of stairs (n) : 6
# Fee: {1,2,5,2,1,2}
# Output: 3
# Explanation: Starting from index '0', we can reach the top through: 0->3->top
# The total fee we have to pay will be (1+2).
# Example 2:

# Number of stairs (n): 4
# Fee: {2,3,4,5}
# Output: 5
# Explanation: Starting from index '0', we can reach the top through: 0->1->top
# The total fee we have to pay will be (2+3).
# Let’s first start with a recursive brute-force solution.

# F: House thief

# There are ‘n’ houses built in a line. A thief wants to steal maximum possible money from these houses. The only restriction the thief has is that he can’t steal from two consecutive houses, as that would alert the security system. How should the thief maximize his stealing?

# Problem Statement #
# Given a number array representing the wealth of ‘n’ houses, determine the maximum amount of money the thief can steal without alerting the security system.

# Example 1:

# Input: {2, 5, 1, 3, 6, 2, 4}
# Output: 15
# Explanation: The thief should steal from houses 5 + 6 + 4
# Example 2:

# Input: {2, 10, 14, 8, 1}
# Output: 18
# Explanation: The thief should steal from houses 10 + 8
# Let’s first start with a recursive brute-force solution.