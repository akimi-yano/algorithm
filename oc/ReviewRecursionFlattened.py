# Review - recursion
# 2e. Flatten a nested list
#
# Input:    {List}
# Output:   {List}
#
# Example: flatten([1, [2, 3, [4]], 5, [[6]]]) => [1, 2, 3, 4, 5, 6]

def flattenNestedList(arr):
    def helper(subArr):
        if type(subArr) != list:
            return [subArr]
        else:
            temp = []
            for i in range(len(subArr)):
                temp.extend(helper(subArr[i]))
        return temp                    
    return helper(arr)
        
print(flattenNestedList([1, [2, 3, [4]], 5, [[6]]]))

# input [1, [2, 3, [4]], 5, [[6]]]
# arr - > length 4

# 1
# [2, 3, [4]]
# 5
# [[6]]

# output [1, 2, 3, 4, 5, 6]