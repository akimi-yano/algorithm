# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def helper(cur, chars):
            if cur.val not in chars:
                chars[cur.val] = 1
            else:
                chars[cur.val] += 1
    
            # just base case (leaf node) // we need to know if its a leaf node or not so so we check cur.left and cur.right
            if cur.left is None and cur.right is None:
                found_odd = False
                for char in chars:
                    if chars[char] % 2 != 0:
                        if found_odd:
                            
                            # cleaning up by updating the dict in the global scope for the previous scope to use the dict again (have to do this clearn up before any kind of return statement)
                            chars[cur.val] -= 1
                            if chars[cur.val] == 0:
                                del chars[cur.val]
                                
                            return 0
                        found_odd = True
                        
                # cleaning up by updating the dict in the global scope for the previous scope to use the dict again (have to do this clearn up before any kind of return statement)
                chars[cur.val] -= 1
                if chars[cur.val] == 0:
                    del chars[cur.val]
                    
                return 1
            
            # counting the total # of palindrome / recursive part !
            total = 0
            if cur.left is not None:
                total += helper(cur.left, chars)
            if cur.right is not None:
                total += helper(cur.right, chars)
                
            # cleaning up by updating the dict in the global scope for the previous scope to use the dict again (have to do this clearn up before any kind of return statement)
            chars[cur.val] -= 1
            if chars[cur.val] == 0:
                del chars[cur.val]
                
            return total
        
        return helper(root, {})
            