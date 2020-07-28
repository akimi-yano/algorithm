# 4.9 if dicimal integer is palindrome 

# # this does not work
# def is_palin(num):
#     temp =  num
#     num_d =  0
#     while temp>0:
#         temp = temp//10
#         num_d+=1
#     # print(digits)
#     digits = num_d
#     # i=0
#     while digits:
#         # prev = num
#         # print(digits)
#         # digits-=i
#         d = digits-1
#         temp = num 
#         # print(d)
#         right=num%10
#         # print(right)
#         while d:
#             # print(temp)
#             temp=temp//10
#             # print(temp)
#             d-=1
#         # print(temp)
#         # right=prev%10
#         # print(temp)
#         left = temp%10
#         # print(left)
#         # print(left)
#         num = num//10
#         # prev = num
#         digits-=2
#         # i+=1
#         # print(digits)
#         # print(right,left)
#         if right!=left:
#             # if digits<=1:
#             #     break 
#             return False
#     return True
    
# print(is_palin(121))
# # print(is_palin(12))

import math
# solution that works
def is_palindrome(x):
    if x<=0:
        return x==0
    
    num_digits = math.floor(math.log10(x))+1
    msd_mask = 10**(num_digits-1)
    for _ in range(num_digits//2):
        if x//msd_mask!=x%10:
            return False
        x%=msd_mask 
        x//=10
        msd_mask//=100
    return True

print(is_palindrome(12121))