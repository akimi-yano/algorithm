# 337. House Robber III
# Medium

# 3366

# 63

# Add to List

# Share
# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

# Determine the maximum amount of money the thief can rob tonight without alerting the police.

# Example 1:

# Input: [3,2,3,null,3,null,1]

#      3
#     / \
#    2   3
#     \   \ 
#      3   1

# Output: 7 
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# Example 2:

# Input: [3,4,5,1,3,null,1]

#      3
#     / \
#    4   5
#   / \   \ 
#  1   3   1

# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.



# This approach does not work !
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# from collections import deque
# class Solution:
#     def rob(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         odd = even = 0
#         queue = deque([(root, True)])
#         while queue:
#             new_queue = deque([])
#             while queue:
#                 node, is_odd = queue.popleft()
#                 if is_odd:
#                     odd += node.val
#                 else:
#                     even += node.val
#                 if node.right:
#                     new_queue.append((node.right, is_odd^1))
#                 if node.left:
#                     new_queue.append((node.left, is_odd^1))
#             queue = new_queue
        
#         return max(odd, even)




# This solution works ! DP : recursion + memoization !

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(cur, can_take):
            key = (cur, can_take)
            if key in memo:
                return memo[key]
            max_profit = float('-inf')
            if not cur:
                max_profit = 0
            else:
                if can_take:
                    max_profit = max(max_profit, cur.val + helper(cur.right, False) + helper(cur.left, False))
                max_profit = max(max_profit, helper(cur.right, True) + helper(cur.left, True))
            memo[key] = max_profit
            return max_profit
        memo = {}
        if not root:
            return 0
        return helper(root, True)    

        