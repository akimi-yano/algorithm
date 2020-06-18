# [In Progress]
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

# print(str_to_int("+123"))
# print(str_to_int("-123"))

def int_to_str(n):
    memo = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
    # ans = n%=10
    # while n>0:
   
  
        
    #     print(n)
    # # if n<0:
    #     ans+="-"
    # # 1 
    # if n//10 in memo:
    #     ans+= memo[n//10]
   
    # 3
    # ans+=n%10
    return ans
print(int_to_str(123))