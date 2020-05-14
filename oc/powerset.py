
# POWER SETS !!!
# Complete the 'powerset' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING word as parameter.
#given a string S return the powerset P(S) which is an array of all the combinations of the S

def powerset(word):
    def helper(sub, i):
        ans = set([sub])
        if i>len(word)-1:
            return ans
        ans = ans.union(helper(sub,i+1)) 
        sub +=word[i]
        ans = ans.union(helper(sub,i+1)) 
        return ans
    return helper("",0)  
print(powerset('abc'))