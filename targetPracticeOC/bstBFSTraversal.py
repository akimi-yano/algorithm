
# Node class for a binary tree node
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

#
# Complete the 'treeBFS' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts TreeNode root as parameter.
#

from collections import deque
def treeBFS(root):
    if root is None:
        return []
    queue = deque([])
    arr = []
    queue.append(root)
    while len(queue)>0:
        current = queue.popleft()
        arr.append(current.value)
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return arr 


    
# generate tree from list