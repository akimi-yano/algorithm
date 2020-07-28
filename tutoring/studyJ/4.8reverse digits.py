# 4.8 reverse digits
# reverse digits:
# 1 solve it as string 

# 2 use div mod

def reverse_digits(num):
    ans =0
    is_negative = False
    if num<0:
        is_negative = True
        num=num*(-1)
    while num:
        ans=ans*10
        ans+=(num%10)
        num=num//10
    if is_negative:
        return ans*(-1)
    else:
        return ans  
    
# print(reverse_digits(123456))
print(reverse_digits(-42))
# print(reverse_digits(314))
