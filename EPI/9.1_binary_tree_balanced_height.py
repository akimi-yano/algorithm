# 9.1 test if a binary tree is a height-balanced
class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
class BinaryTree:
    def __init__(self):
        self.root = None 
        
    def insert(self,val, current): 
        if self.root is None:
            self.root = Node(val)
            return self
    
        if not current:
            current = self.root
    
        if val > current.val and current.right != None:
            self.insert(val, current.right)
        
        if val > current.val and current.right == None:
            current.right = Node(val)
        
        if val < current.val and current.left != None: 
            self.insert(val, current.left)

        if val < current.val and current.left == None:
            current.left = Node(val)
        return self

    def inorder(self,current):
        if current is None:
            return
        
        self.inorder(current.left)
        print(current.val)
        self.inorder(current.right)
    



new_tree = BinaryTree()
new_tree.insert(2,new_tree.root).insert(1,new_tree.root).insert(3,new_tree.root)
new_tree.inorder(new_tree.root)

def is_selfbalancing_tree(root):
    def helper(cur):
        if root is None:
            return 0
        l_count = 1 + helper(cur.left)
        r_count = 1 + helper(cur.right)
        check =  abs(l_count-r_count)
        if check >1:
            return False
        else:
            return check
        
    ans = helper(root) 
    if ans == False:
        return False
    elif ans >1 :
        return False
    else:
        return True

print(is_selfbalancing_tree(new_tree.root))

        #     2
        #     /\
        #    1  3
        #   /\  /\
        #       4 5 