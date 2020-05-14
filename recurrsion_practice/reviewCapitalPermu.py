# next day review for capital permu
def capitalPermu(s):
    def helper(subs, i):
        ans = set([])
        if i>len(s)-1:
            ans.add(subs)
            return ans
        ans  = ans.union(helper(subs+s[i], i+1))
        ans = ans.union(helper(subs+s[i].upper(), i+1))
        return ans 
    return helper("",0)
print(capitalPermu("abc"))