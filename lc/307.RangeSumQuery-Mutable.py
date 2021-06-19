# 307. Range Sum Query - Mutable
# Medium

# 2034

# 113

# Add to List

# Share
# Given an integer array nums, handle multiple queries of the following types:

# Update the value of an element in nums.
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# void update(int index, int val) Updates the value of nums[index] to be val.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

# Example 1:

# Input
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# Output
# [null, 9, null, 8]

# Explanation
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
# numArray.update(1, 2);   // nums = [1, 2, 5]
# numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# 0 <= index < nums.length
# -100 <= val <= 100
# 0 <= left <= right < nums.length
# At most 3 * 104 calls will be made to update and sumRange.

# This solution works:

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.total = 0
        self.left_node = self.right_node = None
        
        self.mid = (self.left + self.right) // 2
        if self.left < self.right:
            self.left_node = Node(left, self.mid)
            self.right_node = Node(self.mid + 1, right)
    
    def update_total(self, i, val):
        if not self.left <= i <= self.right:
            return self.total
        if self.left == i == self.right:
            self.total = val
            return self.total
        self.total = self.left_node.update_total(i, val) + self.right_node.update_total(i, val)
        return self.total
    
    def get_total(self, range_left, range_right):
        if self.left == range_left and self.right == range_right:
            return self.total
        sub_total = 0
        if range_left > self.mid:
            return self.right_node.get_total(range_left, range_right)
        if range_right <= self.mid:
            return self.left_node.get_total(range_left, range_right)
        return self.left_node.get_total(range_left, self.mid) + self.right_node.get_total(self.mid + 1, range_right)

class NumArray:
    def __init__(self, nums: List[int]):
        self.root = Node(0, len(nums) - 1)
        for i, num in enumerate(nums):
            self.update(i, num)

    def update(self, index: int, val: int) -> None:
        self.root.update_total(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.root.get_total(left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)