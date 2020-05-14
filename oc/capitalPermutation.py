# interview - capitalPermutation

def capitalPermutation(word):
    def helper(sub, i):
        ans = set([])
        if i>len(word)-1:
            ans.add(sub)
            return ans
        ans = ans.union(helper(sub+word[i],i+1)) 
        ans = ans.union(helper(sub+word[i].upper(),i+1)) 
        return ans
    return helper('', 0)  
print(capitalPermutation('abc'))