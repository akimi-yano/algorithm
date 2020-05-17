# 203 - Two Sum

# Given an array of integers and a target, 
# return a pair of indices where the corresponding values in the array add up to the target.

# ```
# Input: Array of Integers, Target Integer
# Output: Two element Array of Integers
# Example
# Input: [1, 6, -5, 7, 3], -2      =>	Output: [2,4]
# Input: [1, 9, 10], 8			=>	Output: [-1,-1]
# ```

# # Constraints

# ```
# Time Complexity: O(N)
# Auxiliary Space Complexity: O(N)
# ```

# If the target integer is not found return [-1, -1].

# Values of the array can be positive or negative integers.

def twoSum(arr,target):
    checker = {}
    ans = []
    for i in range(len(arr)):
        if arr[i] not in checker:
            checker[target-arr[i]] = i 
        else:
            ans.append(checker[arr[i]])
            ans.append(i)
            break
    if len(ans)<1:
        ans = [-1,-1]
    return ans
print(twoSum([1, 6, -5, 7, 3],-2))
print(twoSum([1, 9, 10], 8))
