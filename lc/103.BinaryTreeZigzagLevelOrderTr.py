# 103. Binary Tree Zigzag Level Order Traversal

# Share
# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# this doesnt  work - the below one works
# from collections import deque
# class Solution:
#     def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root: return []
#         ans = []
#         queue = deque([(root,1)])
#         left = False
#         prev = 2
#         while queue:

#             cur,level = queue.popleft()
#             if len(ans)<level:
#                 while temp:
#                     queue.append(temp.pop())
#                 ans.append([])
#                 temp = []
#             ans[len(ans)-1].append(cur.val)
#             temp.append(cur)
            
#             if not cur.left and not cur.right:
#                 continue
#             if left:
#                 if cur.left:
#                     queue.append((cur.left,level+1))
#                 if cur.right:
#                     queue.append((cur.right,level+1))
            
#             else:
#                 if cur.right:
#                     queue.append((cur.right,level+1))
#                 if cur.left:
#                     queue.append((cur.left,level+1))
#             # print(queue[len(queue)-1][1],prev)
#             if level+1 > prev:
                
#                 # print(queue)
#                 # queue.reverse()
#                 # print(queue)
#                 if left:
#                     left = False
#                 else:
#                     left = True
#             prev=level+1
#         return ans



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        ans = []
        queue = deque([(root,0)])
        cur_level = 0
        while queue:
            # if even, go left->right
            if cur_level % 2 == 0:
                if cur_level != queue[0][1]:
                    # print("moving from level {} to level {}, queue: {}".format(cur_level, queue[0][1], queue))
                    cur_level = queue[0][1]
                    continue
                node, level = queue.popleft()
                if level >= len(ans):
                    ans.append([])
                ans[level].append(node.val)
                if node.left is not None:
                    queue.append((node.left, level+1))
                if node.right is not None:
                    queue.append((node.right, level+1))
            # if odd, go right->left
            else:
                if cur_level != queue[-1][1]:
                    # print("moving from level {} to level {}, queue: {}".format(cur_level, queue[0][1], queue))
                    cur_level = queue[-1][1]
                    continue
                node, level = queue.pop()
                if level >= len(ans):
                    ans.append([])
                ans[level].append(node.val)
                if node.right is not None:
                    queue.appendleft((node.right, level+1))
                if node.left is not None:
                    queue.appendleft((node.left, level+1))
        return ans