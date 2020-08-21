def permulation(s):
    if len(s)<=1:
        return [s]
    ans = []
    for i in range(len(s)):
        arr = permulation(s[:i]+s[i+1:])
        for elem in arr:
            ans.extend([s[i]+elem])
        # print(arr)
    return ans  
    # return set(ans)  
# permulation("PETE")
print(permulation("PETE"))
'''
aki
arr = helper(ki)
 - > arr = helper(i)
 [ki]
'''
'''
# set -> 12 - for each  dups devide by perm 
N!/ (c1!*c2!*c3!..)
where N = # of characters total
where ci = # of characters for a given character

for ex: "PEET"
N = 4
[P] c1 = 1!
[E] c2 = 2!
[T] c3 = 1!
4!/(1!*2!*1!) = 24/2 = 12
'''
# list -> 24 - 4*3*2*1




'''
PETE
0123

PE ET - 
'''

def permulation2(s):
    def helper(sub,i,s):
        if i>len(s)-1:
            return [sub]
        ans = []
        ans.extend(helper(sub+s[i],i+1,s))
        return ans
    res = []
    for i in range(len(s)): 
        res.append(helper("",i,s))
    return res
  

print(permulation2("PETE"))