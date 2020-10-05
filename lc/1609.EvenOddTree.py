# 1609. Even Odd Tree
# Medium

# 12

# 0

# Add to List

# Share
# A binary tree is named Even-Odd if it meets the following conditions:

# The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
# For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
# For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
# Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

 

# Example 1:



# Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
# Output: true
# Explanation: The node values on each level are:
# Level 0: [1]
# Level 1: [10,4]
# Level 2: [3,7,9]
# Level 3: [12,8,6,2]
# Since levels 0 and 2 are all odd and increasing, and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.
# Example 2:



# Input: root = [5,4,2,3,3,7]
# Output: false
# Explanation: The node values on each level are:
# Level 0: [5]
# Level 1: [4,2]
# Level 2: [3,3,7]
# Node values in the level 2 must be in strictly increasing order, so the tree is not Even-Odd.
# Example 3:



# Input: root = [5,9,1,3,5,7]
# Output: false
# Explanation: Node values in the level 1 should be even integers.
# Example 4:

# Input: root = [1]
# Output: true
# Example 5:

# Input: root = [11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17]
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [1, 105].
# 1 <= Node.val <= 106



# This approach works but trials and errors, and there are some unnecessary parts:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if not root:
            return False
        if root.val %2==0:
            return False
        queue = deque([(root, 0)])
        temp = deque([])
        evenidx = True
        
        while queue or temp:
            while queue:
                cur, idx = queue.popleft()
                # print(cur.val, idx)
                if idx %2 == 0:
                    evenidx = True
                else:
                    evenidx = False
                if evenidx and cur.val%2==0:
                    return False
                elif not evenidx and cur.val%2!=0:
                    return False
                if cur.left:
                    temp.append((cur.left, idx+1))

                if cur.right:
                    temp.append((cur.right, idx+1))
            
            # print([elem[0].val for elem in temp])
                
            if not temp:
                continue
            if evenidx:
                prev = float('inf')
            else:
                prev = float('-inf')
            for num in [elem[0].val for elem in temp]:
                if evenidx and num%2!=0:
                    return False
                elif not evenidx and num%2==0:
                    return False
                if evenidx and prev<=num:
                    return False
                elif not evenidx and prev>=num:
                    return False
                prev = num
            
            while temp:
                cur, idx = temp.popleft()
                # print(cur.val, idx)
                if idx %2 == 0:
                    evenidx = True
                else:
                    evenidx = False
                if evenidx and cur.val%2==0:
                    return False
                elif not evenidx and cur.val%2!=0:
                    return False
                if cur.left:
                    queue.append((cur.left, idx+1))
                if cur.right:
                    queue.append((cur.right, idx+1))
            # print([elem[0].val for elem in queue])
                  
            if not queue:
                continue
            if evenidx:
                prev = float('inf')
            else:
                prev = float('-inf')
            for num in [elem[0].val for elem in queue]:
                if evenidx and num%2!=0:
                    return False
                elif not evenidx and num%2==0:
                    return False
                if evenidx and prev<=num:
                    return False
                elif not evenidx and prev>=num:
                    return False
                prev = num
            
             
                # if not temp:
                #     continue
                # if evenidx:
                #     prev = float('inf')
                # else:
                #     prev = float('-inf')
                # print([elem[0].val for elem in temp])
                # for num in [elem[0].val for elem in temp]:
                #     if evenidx and num%2!=0:
                #         return False
                #     elif not evenidx and num%2==0:
                #         return False
                    # if evenidx and prev<=num:
                    #     return False
                    # elif not evenidx and prev>=num:
                    #     return False
                    # prev = num
            
        return True
    

# This solution works ! Cleaned up ver:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if not root:
            return False
        if root.val %2==0:
            return False
        queue = deque([(root, 0)])
        temp = deque([])
        evenidx = True
        
        while queue or temp:
            while queue:
                cur, idx = queue.popleft()
                # print(cur.val, idx)
                if idx %2 == 0:
                    evenidx = True
                else:
                    evenidx = False
                if evenidx and cur.val%2==0:
                    return False
                elif not evenidx and cur.val%2!=0:
                    return False
                if cur.left:
                    temp.append((cur.left, idx+1))

                if cur.right:
                    temp.append((cur.right, idx+1))
                
            if not temp:
                continue
            if evenidx:
                prev = float('inf')
            else:
                prev = float('-inf')
            for num in [elem[0].val for elem in temp]:
                if evenidx and num%2!=0:
                    return False
                elif not evenidx and num%2==0:
                    return False
                if evenidx and prev<=num:
                    return False
                elif not evenidx and prev>=num:
                    return False
                prev = num
            
            while temp:
                cur, idx = temp.popleft()
                # print(cur.val, idx)
                if idx %2 == 0:
                    evenidx = True
                else:
                    evenidx = False
                if evenidx and cur.val%2==0:
                    return False
                elif not evenidx and cur.val%2!=0:
                    return False
                if cur.left:
                    queue.append((cur.left, idx+1))
                if cur.right:
                    queue.append((cur.right, idx+1))

            if not queue:
                continue
            if evenidx:
                prev = float('inf')
            else:
                prev = float('-inf')
            for num in [elem[0].val for elem in queue]:
                if evenidx and num%2!=0:
                    return False
                elif not evenidx and num%2==0:
                    return False
                if evenidx and prev<=num:
                    return False
                elif not evenidx and prev>=num:
                    return False
                prev = num
            
        return True


# This solution works ! This is much shorter and intuitive !!!! love this conciseness

'''
keep track of the even or odd in a global state and flip it in each new list
this way we don't have to check every time we pop !

We don't actually need queue because we can just append valid elements in a new array and swap at the end.
Can do xor with boolean values !
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        level = [root]
        even_idx = True
        while len(level) > 0:
            new_level = []
            prev = float('-inf') if even_idx else float('inf')
            for elem in level:
                if elem is None:
                    continue
                if even_idx:
                    if prev >= elem.val or not elem.val % 2:
                        return False
                else:
                    if prev <= elem.val or elem.val % 2:
                        return False
                prev = elem.val
                new_level.append(elem.left)
                new_level.append(elem.right)

            level = new_level
            even_idx ^= True
        return True