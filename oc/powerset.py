
#
# Complete the 'powerset' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING word as parameter.
#given a string S return the powerset P(S) which is an array of all the combinations of the S

def powerset(word):
    # Write your code here
    def helper(sub, left):
        ans = set([sub])
        for i in range(len(left)):
            new_sub = sub + left[i]
            new_left = left[:i] + left[i+1:]
            ans = ans.union(helper(new_sub, new_left))
        return ans
    
    return list(helper('', word))
            
print(powerset('abc'))