# 1302. Deepest Leaves Sum
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root is None:
            return 0

        # 1 find height -> 4
        
        def find_height(current):
            if not current:
                return 0
            left = find_height(current.left)
            right = find_height(current.right)
            if left>right:
                return left+1
            else:
                return right+1
        height = find_height(root)
   
        # 2 add 4th 
        
        def count_deepest(deepest, current, cur_height):
            if current.left is None and current.right is None:
                if cur_height >= deepest:
                    return current.val
                else:
                    return 0
            sum_children = 0
            
            if current.left is not None:
                sum_children += count_deepest(deepest, current.left, cur_height+1)
            if current.right is not None:
                sum_children += count_deepest(deepest, current.right, cur_height+1)
            return sum_children
        
        return count_deepest(height, root, 1)
    
    