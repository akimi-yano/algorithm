# [In Progress]
# 6.1 interconvert strings and integers

# "123"->123
# input str
# output int
# no casting

def str_to_int(s):
    nums = set([])
    memo = {'0':0,1:1,2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
    for i in s:
        if i in nums:
            

print(str_to_int("+123"))

def int_to_str(n):
    memo = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}

print(int_to_str(123))