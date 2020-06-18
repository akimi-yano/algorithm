# [Completed]
# 6.1 interconvert strings and integers

# "123"->123
# input str
# output int
# no casting

def str_to_int(s):
    memo = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    ans = 0
    for i in range(len(s)-1,-1,-1):
        if s[i] in memo:
            if ans ==0:
                ans+= memo[s[i]] 
            else:
                ans+= memo[s[i]] *10**(len(s)-1-i)
        elif i==0 and s[i] == "-":
            ans *=(-1)
    return ans

print(str_to_int("+123"))
print(str_to_int("0"))
print(str_to_int("+001"))
print(str_to_int("-123"))

def int_to_str(n):
    memo = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
    
    is_negative = None
    if n == 0:
        return "0"
    if n<0:
        is_negative = True
        n *= -1
    temp = []
    while n!=0:       
        temp.append(memo[n%10])
        n=n//10
    ans = ""
    if is_negative:
        ans+="-"
    # reverse the list and concat to str
    # print(temp)
    for i in range(len(temp)-1,-1,-1):
        ans+=temp[i]
    return ans
# print(int_to_str(-123456))
print(int_to_str(9))

# to get ichinokurai, do %10
# to shift number by 10 do //10

# so check first by doing %10 and then in loop until n == 0 (n will become 0 at some point)
# you repeat check %10 and //10
