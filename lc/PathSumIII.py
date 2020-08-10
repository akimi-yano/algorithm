# Path Sum III

# Solution
# You are given a binary tree in which each node contains an integer value.

# Find the number of paths that sum to a given value.

# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

# Example:

# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1

# Return 3. The paths that sum to 8 are:

# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11


# This solution works -  but there maybe better solutions !

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# this solution works!
class Solution:
    def pathSum(self, root: TreeNode, target_arg: int) -> int:
        if root is None:
            return 0

        def helper(cur, subpaths, target):
            if cur is None:
                return 0

            subpaths.append(0)
            counter = 0
            for i, _ in enumerate(subpaths):
                subpaths[i] += cur.val
                if subpaths[i] == target:
                    counter += 1
            counter += helper(cur.left, subpaths,  target)
            counter += helper(cur.right, subpaths, target)
            
            
            for i, _ in enumerate(subpaths):
                subpaths[i] -= cur.val
            subpaths.pop()
            return counter
            
        return helper(root, [], target_arg)




# another solution - prefix sum !

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target_arg: int) -> int:
        if root is None:
            return 0
        self.total=0
        memo = {0: 1}
        def helper(cur,target,cur_sum):
            if not cur:
                return
            cur_sum += cur.val
            if cur_sum-target in memo:
                self.total += memo[cur_sum-target]

            if cur_sum not in memo:
                memo[cur_sum]=1
            else:
                memo[cur_sum]+=1

            helper(cur.left,target, cur_sum)
            helper(cur.right,target, cur_sum)
            
            memo[cur_sum] -= 1
            if memo[cur_sum] < 1:
                del memo[cur_sum]
            
        helper(root,target_arg,0)
        return self.total

                
            
            
            
            
            
            
            
            
        
        

                
            
            
            
            
            
            
            
            
        
        