# 449. Serialize and Deserialize BST
# Medium

# 1571

# 82

# Add to List

# Share
# Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

# The encoded string should be as compact as possible.

 

# Example 1:

# Input: root = [2,1,3]
# Output: [2,1,3]
# Example 2:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# 0 <= Node.val <= 104
# The input tree is guaranteed to be a binary search tree.


# This approach does not work :

    # def deserialize(self, data: str) -> TreeNode:
    #     """Decodes your encoded data to tree.
    #     """
    #     def helper(i, cur):
    #         if i > len(data)-1:
    #             return 
    #         target = int(data[i])
    #         if not cur:
    #             return TreeNode(target)
    #         if target < cur.val:
    #             helper(i+1, cur.left)
    #         else:
    #             helper(i+2, cur.right)
    #         # cur = TreeNode(data[i])
    #         # cur.left = helper(i+1, cur)
    #         # cur.right = helper(i+2, cur)
    #         return cur
        
    #     return helper(1,TreeNode(int(data[0])))
    
    
# This approach works !:

'''
break down problem into small simple pieces that can be solved by my current knowledge
since we are turning it all into string, we need a devider that we can use later to split
don't forget to casting to str to int
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def helper(cur):
            if not cur:
                return
            ans.append(cur.val)
            helper(cur.left)
            helper(cur.right)
            return ans 
        ans = []
        helper(root)
        return ",".join([str(elem) for elem in ans])

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def helper(target, cur):
            if not cur:
                return TreeNode(target)
            elif target < cur.val:
                cur.left = helper(target, cur.left)
            elif target > cur.val:
                cur.right = helper(target, cur.right)
            return cur
        if not data:
            return None
        data = data.split(',')
        data = [int(elem) for elem in data]
        root = TreeNode(data[0])
        for i in range(1,len(data)):
            helper(data[i], root)
        return root 
    
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans