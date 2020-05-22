    # Write your code here
    arr = []
    def helper(current):
        if current is None:
            return 
        helper(current.left)
        arr.append(current.value)
        helper(current.right)

    helper(root)
    return arr 