# 129. Sum Root to Leaf Numbers
# Medium

# 3194

# 67

# Add to List

# Share
# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

# A leaf node is a node with no children.

 

# Example 1:


# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
# Example 2:


# Input: root = [4,9,0,5,1]
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 9
# The depth of the tree will not exceed 10.


# This solution works:

'''
The idea is traverse our tree, using any tree traversal algorighm. I choose dfs, and also I directly change the values of our tree.

If we reach non-existing node (None), we just return back.
If we reached leaf, that is it do not have any children, return value of this node.
Update values for left and right children if they exist.
Finally, call function recursively for left and right children and return sum of results for left and right.
image

We start traverse from root, and we replace its children 9 and 0 with 49 and 40.
Then for 49 we replace its children 5 and 1 with 495 and 491.
Finally, we evaluate sum of all leafs: 40 + 495 + 491.

Complexity: time complexity can be potentially O(nh), where n is number of nodes and h is number of levels, because at each step our numbers become bigger and bigger. If we assume that number we met will always be in 32int range, then can say that complexity is O(n). Space complexity is O(h) to keep the stack of recursion.
'''

class Solution:
    def sumNumbers(self, root):
        if not root: return 0
        
        if not root.left and not root.right:
            return int(root.val)
        
        if root.left: root.left.val = 10*root.val + root.left.val
        if root.right: root.right.val = 10*root.val + root.right.val
            
        return self.sumNumbers(root.left) + self.sumNumbers(root.right)


# This solution works:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root):
        
        def helper(cur, nums):
            nonlocal ans
            if not cur.left and not cur.right:
                new_nums = list(nums)
                new_nums.append(cur.val)
                i = 0
                total = 0
                while new_nums:
                    val = new_nums.pop()
                    total += val*10**i
                    i += 1
                ans += total
                return
            if cur.left:
                helper(cur.left, nums + [cur.val])
            if cur.right:
                helper(cur.right, nums + [cur.val])
        
        ans = 0
        helper(root, [])
        return ans