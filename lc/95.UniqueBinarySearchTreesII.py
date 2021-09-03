# 95. Unique Binary Search Trees II
# Medium

# 3772

# 244

# Add to List

# Share
# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

# Example 1:


# Input: n = 3
# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
# Example 2:

# Input: n = 1
# Output: [[1]]
 

# Constraints:

# 1 <= n <= 8


# This solution works:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(left, right):
            if left > right:
                return [None]
            
            ans = []
            for mid in range(left, right + 1):
                left_trees = helper(left, mid - 1)
                right_trees = helper(mid + 1, right)
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(val=mid)
                        root.left = left_tree
                        root.right = right_tree
                        ans.append(root)
            return ans
                
        return helper(1, n)
        
        
        '''
        [
        [1,null,2,null,3],
        [1,null,3,2],
        [2,1,3],
        [3,1,null,null,2],
        [3,2,null,1]
        ]
        '''
        '''
           1
        null 2
            null 3
            
           1
        null 3
            2
          
          2
        1  3
        
          3
        1  null
    null 2
    
          3
        2 null
      1
      
      
      1
      
      left_subtrees: [None]
      right_subtrees: [[2, None, 3], [3, 2, None]
      
      
      trees = []
      for middle_value in range(left, right )
      for left_subtree in left_subtrees:
          for right_subtree in right_subtrees:
              # make sure to copy!
              root = TreeNode(1)
              root.left = copy(left_subtree)
              root.right = copy(right_subtree)
              trees.append(root)
      return trees
      
      trees:
         1) [1, None, [2, None, 3]]
         2) [1, None, [3, 2, None]]
      return [[1, None, [2, None, 3]], [1, None, [3, 2, None]]]
      
        '''