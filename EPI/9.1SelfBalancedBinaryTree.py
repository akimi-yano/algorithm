# 9.1 Self Balanced Binary Tree

#       A
#     /   \
#   B      K
#   /\     /\
#  C  H   L  O
#  /\ /\  /\
# D G I J M N
# /\
# E F
# yay passed all the test cases !!!!!

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    def helper(cur):
        if not cur:
            return 0
        left = helper(cur.left)
        right = helper(cur.right)
        if abs(left-right)<=1:
            return 1 + max(left,right) 
        return float('inf')
    return helper(tree) !=float('inf')
    
    

#       A
#     /   \
#   4B      K
#   /\     /\
#  3C  H   L  O
#  /\ /\  /\
# 2D G1 I J M N
# /\
#1 E F1
# 00 

# another solution

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight',('balanced','height'))
    # First value of the return value indicates if tree is balanced, and if 
    # balanced the second value of the return valie is the height of tree.
    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(balanced=True, height=-1)
        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return left_result
        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return right_result

        is_balanced= abs(left_result.height-right_result.height) <= 1
        height = max(left_result.height,right_result.height)+1
        return BalancedStatusWithHeight(is_balanced,height)
    return check_balanced(tree).balanced

    
    