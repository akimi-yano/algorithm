# 1457. Pseudo-Palindromic Paths in a Binary Tree
# Medium

# 487

# 16

# Add to List

# Share
# Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

# Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

 

# Example 1:



# Input: root = [2,3,1,3,1,null,1]
# Output: 2 
# Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
# Example 2:



# Input: root = [2,1,1,1,3,null,null,null,null,null,1]
# Output: 1 
# Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
# Example 3:

# Input: root = [9]
# Output: 1
 

# Constraints:

# The given binary tree will have between 1 and 10^5 nodes.
# Node values are digits from 1 to 9.


# This solution works !
'''
watch out for passed by reference !
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        
        def helper(cur, counts):
            if not cur:
                return 0
            newcounts = Counter(counts)
            newcounts[cur.val] += 1
            if not cur.left and not cur.right:
                odd = 0
                for v in newcounts.values():
                    if v % 2 != 0:
                        odd +=1
                return 1 if odd <= 1 else 0
            return helper(cur.left, newcounts) + helper(cur.right, newcounts)
        
        return helper(root, Counter())
    
    
# This solution works - optimization

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        
        def helper(cur, seen):
            if not cur:
                return 0
            
            if not cur.left and not cur.right:
            
                return 1 if len(seen ^ set([cur.val])) <= 1 else 0
            return helper(cur.left, seen ^ set([cur.val])) + helper(cur.right, seen ^ set([cur.val]))
        
        return helper(root, set([]))