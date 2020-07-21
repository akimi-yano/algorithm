# Given a binary tree, collect a tree's nodes as if you were doing this: 
# Collect and remove all leaves, repeat until the tree is empty.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Example:

# Input: [1,2,3,4,5]
  
#           1
#          / \
#         2   3
#        / \     
#       4   5    

# Output: [[4,5,3],[2],[1]]
 
# Explanation:

# 1. Removing the leaves [4,5,3] would result in this tree:

#           1
#          / 
#         2          
 
# 2. Now removing the leaf [2] would result in this tree:

#           1          

# 3. Now removing the leaf [1] would result in the empty tree:

#           []         
# [[3,5,4],[2],[1]], [[3,4,5],[2],[1]], etc, are also consider correct answers
#  since per each level it doesn't matter the order on which elements are returned.

"""
while not none
dfs to find leaf append and remove 4 
output is array of array
"""

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        ans = [] 
        def helper(cur,temp):
            if not cur:
                return
            if cur.left == None and cur.right == None:
                temp.append(cur.val)
                cur = None
                return 
            cur.left = helper(cur.left,temp)
            cur.right = helper(cur.right,temp)
            return cur
        while root:
            temp = []
            root = helper(root,temp)
            ans.append(temp)
        return ans
      
      
s = Solution()
print(s.findLeaves([1,2,3,4,5]))
      
      
    
    
    