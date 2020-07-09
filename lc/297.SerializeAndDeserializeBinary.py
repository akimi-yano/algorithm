# 297. Serialize and Deserialize Binary Tree
# Hard

# 2963

# 145

# Add to List

# Share
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Example: 

# You may serialize the following tree:

#     1
#    / \
#   2   3
#      / \
#     4   5

# as "[1,2,3,null,null,4,5]"
# Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

    # THIS DOESNT WORK - see below for the code that works !
# class Codec:
#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         self.ans = "["
#         def find_height(cur):
#             if not cur:
#                 return 0
#             return 1+find_height(cur.left)+find_height(cur.right)
#         self.height = find_height(root)
#         def helper(cur,h):
#             if not cur:
#                 self.ans+="null"+ ","
#             if cur:
#                 self.ans+=str(cur.val) + ","
#                 helper(cur.left,h+1)
#                 helper(cur.right,h+1)
        
#         helper(root,0)
#         self.ans = self.ans[:len(self.ans)-1] + "]"
#         print(self.ans)
#         return self.ans
    
#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
        

# # Your Codec object will be instantiated and called as such:
# # codec = Codec()
# # codec.deserialize(codec.serialize(root))


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




# This code works !!!! really clean solution !!!
class Codec:
    # cheatRoot = None
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # Codec.cheatRoot = root
        if root is None:
            return ''
        output = []
        def helper(node):
            if node is None:
                output.append('')
            else:
                output.append(str(node.val))
                helper(node.left)
                helper(node.right)
        helper(root)
        return ','.join(output)
                
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # return Codec.cheatRoot
    
        if data == '':
            return None

        nodes = data.split(',')
        nodes.reverse()
        # print(nodes)

        root = TreeNode(nodes.pop())
        # print(nodes)

        def helper(node):
            left = nodes.pop()
            if left == '':
                node.left = None
            else:
                node.left = TreeNode(left)
                helper(node.left)
            right = nodes.pop()
            if right == '':
                node.right = None
            else:
                node.right = TreeNode(right)
                helper(node.right)
        helper(root)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))