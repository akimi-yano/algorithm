# Binary Tree Level Order Traversal II

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = deque([(root,1)])
        new = []
        seen = set([root])
        while len(queue)>0:
            current, level = queue.popleft()
            new.append((current.val, level))
            left = current.left
            if left is not None and left not in seen:
                queue.append((left, level+1))
                seen.add(left)
            right = current.right
            if right is not None and right not in seen:
                queue.append((right, level+1))
                seen.add(right)
        
        now = new[len(new)-1][1]
        ans = [deque([]) for _ in range(now)]
        # print(ans)
        for i in range(len(new)-1,-1,-1):
            value,cur = new[i]
            ans[cur-1].appendleft(value)
        return reversed(ans)
    
    
    # bfs + queue - more efficient ver 
    def levelOrderBottom(self, root):
        queue, res = collections.deque([(root, 0)]), []
        while queue:
            node, level = queue.popleft()
            if node:
                if len(res) < level+1:
                    res.insert(0, [])
                res[-(level+1)].append(node.val)
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
        return res