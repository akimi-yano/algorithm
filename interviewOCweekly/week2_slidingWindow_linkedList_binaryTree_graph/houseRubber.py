
# # 208 - House Robber

# A house robber has a map of houses and the amount of gold in each home.  The robber knows that if two adjacent homes are robbed, then the neighborhood security system will sound.  Determine the total amount of gold the robber can get without setting off the alarm.

# ```
# Input: 	 Array of Nonnegative Integers
# Output: 	Integer
# ```

# # Example
# ```
# Input: [1, 2, 3]				 =>	Output: 4
# Input: [1, 2, 4, 1, 5, 12, 5]	=>	Output: 17

# Explanation:
# Knowing you can't rob from two adjacent houses
# The maximum gold you can steal in each case:

# Example 1
# 1 + 3 = 4

# Example 2
# 1 + 4 + 12 = 17

# ```


# # Constraints

# ```
# Time Complexity: O(N)
# Auxiliary Space Complexity: Intermediate O(N), Advanced O(1)
# ```

# # Notes

# Think about how you might be able to do this with just two variables instead of an additional array.

# # Solution
# This can be solved using tabulation (iteratively).

# * 1) Instantiate a new ‘max’ array to hold the max gold that can be accumulated up to each house.
# * 2) Loop through the input array with, i.
# * 3) For each house, the max gold (max[i]) will be the greater of:
#   * The previous house’s max
#   * The max two houses back + the current house value
# * 4) After the loop, return the last value in the max array

# ```Javascript
# let test1 = [1, 2, 3];
# let test2 = [1, 2, 4, 1, 5, 12, 5];

# // solution described from above
# function houseRobber(houses) {
#   if (houses.length === 1) {
#     return houses[0];
#   }
#   if (houses.length === 2) {
#     return Math.max(houses[0], houses[1]);
#   }

#   let max = [houses[0], houses[1]];

#   for (let i = 2; i < houses.length; i++) {
#     max[i] = Math.max(houses[i] + max[i - 2], max[i-1]);
#   }

#   return max[max.length - 1];
# }

# // constant auxiliary space approach
# function houseRobberConstantSpace(houses) {
#   if (houses.length === 1) {
#     return houses[0];
#   }
#   if (houses.length === 2) {
#     return Math.max(houses[0], houses[1]);
#   }

#   let max1 = houses[0];
#   let max2 = houses[1];

#   for (let i = 2; i < houses.length; i++) {
#     let temp = Math.max(houses[i] + max1, max2);
#     max1 = max2;
#     max2 = temp;
#   }

#   return max2;
# }

# console.log(houseRobber(test2));
# console.log(houseRobberConstantSpace(test2));
# ```

# # Resources
# [House Robber on Geeks for Geeks](https://leetcode.com/problems/house-robber/)
