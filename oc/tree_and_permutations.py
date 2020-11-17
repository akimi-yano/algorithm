
'''
https://leetcode.com/problems/binary-tree-maximum-path-sum/
'''

def maxPathSum(self, root: TreeNode) -> int:
    
    def gain(node):
        nonlocal total
        
        if node is None: return 0
        
        L = max(gain(node.left),0)
        R = max(gain(node.right),0)
        third = L+R+node.val
        
        total = max(total, third)
        
        return max(L, R) + node.val
    
    total = float('-inf')
    gain(root)
    return total

  
'''
https://leetcode.com/problems/permutations-ii/
'''
    
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    
    def mutation(build, index_set):
    
        if len(build) == len(nums):
            result.append(build)
            return
        
        item_set = set()
        for i in range(len(nums)):
            if i not in index_set and nums[i] not in item_set:
                index_set.add(i)
                item_set.add(nums[i])
                mutation(build + [nums[i]], index_set)
                index_set.remove(i)
    
    if not nums: return None
    result = [] q
    mutation([], set())
    return result

