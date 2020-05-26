def validBST(arr):
    i = 0
    def helper(lo, hi):
        # a way to set this i to use local i set outside of this  function - can also do "global i"
        nonlocal i
        if i == len(arr): return True
        val = arr[i]
        if val < lo or val > hi: return False
        i += 1
        return helper(lo, val) or helper(val, hi)
    return "YES" if helper(float('-inf'), float('inf')) else "NO"
# should be YES, YES, YES, NO, NO
tests = [[1,2,3],
[2,1,3],
[3,2,1,5,4,6],
[1,3,4,2],
[3,4,5,1,2]]
for test in tests:
    print(validBST(test))

# "lo" and "hi" are the boundaries of the legal values range at each step/tree node
# used dfs pre-order and compared the range at each level of recursion
