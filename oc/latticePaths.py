
# Complete the 'latticePaths' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER n
#

def latticePaths(m, n):
    if m == 0 and n == 0:
        return 1
    elif m<0 or n<0:
        return 0
    return latticePaths(m-1, n) + latticePaths(m,n-1)
    # Write your code here
print(latticePaths(2,2))
print(latticePaths(2,3))
