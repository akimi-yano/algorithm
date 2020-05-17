# 230 - Non-Consecutive Ones

# Given a positive integer `n`, return an array of all the binary strings of 
# length n that *DO NOT* contain consecutive `1`s.

# Input: n (Integer)
# Output: [Str] (Array of Strings)

# # Example

# Input: 2
# Output: ["00", "01", "10"]

# Input: 3
# Output: ["000", "001", "010", "100", "101"]

# # Constraints
# Time Complexity: O(2^N)
# Auxiliary Space Complexity: O(2^N)

# The order of the strings in the array does not matter.
# Use recursion to solve this problem. 


# in - int n
# out - [str]

def noConsecOnes(n):
    def helper(sub):
        if len(sub)>= n:
            return set([sub])
        results = helper(sub+"0")
        if len(sub) == 0 or sub[len(sub)-1]!="1":
            results = results.union(helper(sub + "1"))
        return results
    return list(helper(""))
print(noConsecOnes(2))


def noConsecOnes2(n):
    def helper(sub):
        if len(sub)>= n:
            return set([sub])
        results0 = helper(sub+"0")
        if len(sub) == 0 or sub[len(sub)-1]!="1":
            results1 = helper(sub + "1")
        else:
            results1 = set([])
        results = results0.union(results1)
        
        return results
    return list(helper(""))
print(noConsecOnes2(2))

# 2
# 00 01 10 (x11)

# 3
# 000 001 010 100 101 (x111)   

# takeaway:
#     input and output are different and assign the result of variable to not a input sub but to results
#     the second pattern set needs to be add together with .union 